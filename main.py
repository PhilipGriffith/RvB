chumps = ('renter', 'buyer')

income = 40000
savings = 20000

investment_annual_return_percent = 5.7
housing_annual_return_percent = 4.7

rent = 770
house_value = 200000

# Assuming insurance and property tax rates do not change
insurance = ((1020 + 1191 + 1390) / 3) / 12
property_tax = (((0.0089 + 0.00977) / 2) / 12) * house_value
maintenance = (0.02 * house_value) / 12  # Rule of thumb: 2-5%


pmi = 0.005 * (house_value - savings)  # Rule of thumb: 0.5-1% of original loan
print(pmi / 12)

# Todo Figure this out
rate_30yr_0_pts = (4.0, 4.0, 4.0, 4.0, 4.0, 4.25, 4.375, 4.0, 4.19, 4.25, 5.125)
apr_30yr_0_pts = (4.269, 4.270, 4.289, 4.310, 4.0, 4.299, 4.375, 4.045, 4.249, 4.25, 5.215)
fees_30yr_0_pts = (234, 253, 641, 1082, 1, 1150, 0, 972, 1258, 0, 1825)

rate_15yr_0_pts = (3.5, 3.625, 3.625, 3.625, 3.5, 3.5, 3.75, 3.625, 3.75, 3.79)
apr_15yr_0_pts = (3.778, 3.824, 3.847, 3.854, 3.5, 3.584, 3.823, 3.656, 3.75, 3.893)
fees_15yr_0_pts = (1095, 134, 410, 493, 1, 1150, 995, 383, 0, 1258)

import numpy as np
print(np.mean(rate_15yr_0_pts))

mortgage = 0

# Per month
cost = {'renter': rent, 'buyer': mortgage}
utilities = {'renter': 90, 'buyer': 200}
maintenance = {'renter': 0, 'buyer': maintenance}
property_tax = {'renter': 0, 'buyer': property_tax}
insurance = {'renter': 0, 'buyer': insurance}


def compute_monthly_cost(chump):

    costs = cost[chump] + \
            utilities[chump] + \
            maintenance[chump] + \
            property_tax[chump] + \
            insurance[chump]

    print('Total {} monthly costs: {:.2f}'.format(chump, costs))
    return costs


def compute_closing_cost(years=30):

    boa_closing_cost_30yr = 9934 - 1712  # Includes 1712 in points
    boa_closing_cost_15yr = 9522 - 1328  # Includes 1328 in points
    nerdwallet_closing_cost_30yr = 8824  # No location given, no year (difference in interest rate)
    nerdwallet_closing_cost_15yr = 8786  # No location given, no year (difference in interest rate)
    smart_asset_closing_cost_30yr = 6314  # Location given
    smart_asset_closing_cost_15yr = 6286  # Location given
    navy_federal_closing_cost_30yr = 5018  # No location given
    navy_federal_closing_cost_15yr = 4980  # No location given
    besmartee_closing_cost_30yr = 6891  # No location, no year (difference in interest rate)
    besmartee_closing_cost_15yr = 6850  # No location, no year (difference in interest rate)

    if years == 30:
        return (boa_closing_cost_30yr + nerdwallet_closing_cost_30yr + smart_asset_closing_cost_30yr +
                navy_federal_closing_cost_30yr + besmartee_closing_cost_30yr) / 5
    elif years == 15:
        return (boa_closing_cost_15yr + nerdwallet_closing_cost_15yr + smart_asset_closing_cost_15yr +
                navy_federal_closing_cost_15yr + besmartee_closing_cost_15yr) / 5


def compute_monthly_mortgage_cost(loan_amount, number_of_payments, interest_rate_percent):
    """
    This computes the monthly mortgage payment for a given loan with n remaining payments at a monthly compounded rate.
    """
    interest_rate = interest_rate_percent / 100
    monthly_interest_rate = interest_rate / 12
    numerator = ((1 + monthly_interest_rate) ** number_of_payments) - 1
    denominator = monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments
    discount_factor = numerator / denominator

    return loan_amount / discount_factor


def compute_monthly_investment_gain(amount, annual_rate_percent):
    """
    This computes the amount gained in a single month given an amount and an annual rate.
    """
    monthly_rate = (annual_rate_percent / 100) / 12
    return amount * monthly_rate


def compute_monthly_investment_amount(amount, annual_rate_percent, fee_percent=0.2):
    """
    This computes the total investment amount in a single month given an amount and an annual rate,
    accounting for management fees of 0.2%.
    """
    fee = (fee_percent / 100) / 12
    amount += compute_monthly_investment_gain(amount, annual_rate_percent)
    amount -= amount * fee
    return amount


def compute_investment_amount(years, initial_amount, added_amount, annual_rate_percent):
    """
    This computes the total investment amount in n years given an initial amount, monthly additions,
    and an annual rate, accounting for management fees of 0.2%.
    """
    months = years * 12
    total_amount = initial_amount
    for month in range(months):
        total_amount = compute_monthly_investment_amount(total_amount, annual_rate_percent)
        total_amount += added_amount
    return total_amount


def compute_total_investment(years, initial_amount, added_amount, annual_rate_percent, commission_percent=0.5):
    """
    This may not work for mortgage chump who alters the added amount every month.
    :param years:
    :param initial_amount:
    :param added_amount:
    :param annual_rate_percent:
    :param commission_percent:
    :return:
    """
    global savings
    commission = commission_percent / 100
    buy_commission = initial_amount * commission
    print(buy_commission)
    savings -= buy_commission
    total_amount = compute_investment_amount(years, initial_amount, added_amount, annual_rate_percent)
    sell_commission = total_amount * commission
    print(sell_commission)
    print(total_amount)
    total_amount -= sell_commission
    savings += total_amount


    begin = buy_commission + initial_amount
    print(begin)
    print('Return', ((total_amount - begin) / begin) / 25)

    return savings


if __name__ == '__main__':

    for chump in chumps:
        compute_monthly_cost(chump)

    print(compute_total_investment(25, 100, 0, 8) - 20000)

