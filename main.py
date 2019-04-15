
class Finances:

    def __init__(self):
        self.income = 40000
        self.savings = 20000
        self.housing_budget_percent = 30
        self.housing_budget = (self.income / 12) * (self.housing_budget_percent / 100)

        self.rent = 770
        self.house_value = 200000
        self.housing_appreciation_percent = 4.7


class MonthlyHousing(Finances):

    def __init__(self, loan=None):
        super().__init__()
        self.payment = loan.payment if loan else self.rent
        self.utilities = 200 if loan else 90
        self.maintenance = (0.02 * self.house_value) / 12 if loan else 0  # Rule of thumb: 2-5%
        # Assuming static insurance and property tax rates
        self.insurance = ((1020 + 1191 + 1390) / 3) / 12 if loan else 0
        self.property_tax = (((0.0089 + 0.00977) / 2) / 12) * self.house_value if loan else 0
        self.cost = sum((self.payment, self.utilities, self.maintenance, self.insurance, self.property_tax))


class Loan:

    # Does not consider PMI
    def __init__(self, amount, years=30):
        self.amount = amount
        self.length_in_years = years
        self.length_in_months = self.length_in_years * 12
        self.number_of_payments = self.length_in_months
        self.annual_interest_rate = (sum((4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.19, 4.25, 4.25, 4.375, 5.125)) / 11) / 100
        self.monthly_interest_rate = self.annual_interest_rate / 12
        self.payment = self.compute_monthly_payment()

    def compute_monthly_payment(self):

        numerator = ((1 + self.monthly_interest_rate) ** self.length_in_months) - 1
        denominator = self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.length_in_months
        discount_factor = numerator / denominator
        return self.amount / discount_factor

    def make_payment(self):
        interest = self.amount * self.monthly_interest_rate
        self.amount -= self.payment - interest
        self.number_of_payments -= 1

    def details(self, v=False):
        if v:
            print('Interest rate: ~{:.2f}'.format(self.annual_interest_rate))
            print('Payment: ~{:.2f}'.format(self.payment))
        print('Amount:~{:.2f}'.format(self.amount))
        print('Number of payments:', self.number_of_payments)


class Investment:

    def __init__(self, amount):
        self.annual_rate_percent = 5.7
        self.monthly_rate = (self.annual_rate_percent / 100) / 12
        self.commission_rate_percent = 0.5
        self.fee_rate_percent = 0.2
        self.amount = amount - (amount * (self.commission_rate_percent / 100))

    def compound(self, amount=0):
        self.amount += self.amount * self.monthly_rate
        self.amount -= self.amount * ((self.fee_rate_percent / 100) / 12)
        self.amount += amount

    def sell(self):
        return self.amount - (self.amount * (self.commission_rate_percent / 100))

    def details(self):
        print('Amount: {:.2f}'.format(self.amount))


i = Investment(100)
i.details()
for t in range(12):
    i.compound()
    i.details()
print(i.sell())



# Todo Figure this out
rate_30yr_0_pts = (4.0, 4.0, 4.0, 4.0, 4.0, 4.25, 4.375, 4.0, 4.19, 4.25, 5.125)
apr_30yr_0_pts = (4.269, 4.270, 4.289, 4.310, 4.0, 4.299, 4.375, 4.045, 4.249, 4.25, 5.215)
fees_30yr_0_pts = (234, 253, 641, 1082, 1, 1150, 0, 972, 1258, 0, 1825)

rate_15yr_0_pts = (3.5, 3.625, 3.625, 3.625, 3.5, 3.5, 3.75, 3.625, 3.75, 3.79)
apr_15yr_0_pts = (3.778, 3.824, 3.847, 3.854, 3.5, 3.584, 3.823, 3.656, 3.75, 3.893)
fees_15yr_0_pts = (1095, 134, 410, 493, 1, 1150, 995, 383, 0, 1258)

# todo put this in a mortgage class
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


if __name__ == '__main__':

    loan = Loan(180000)

    mh = MonthlyHousing(loan).cost
    print(mh)

