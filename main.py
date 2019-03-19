chumps = ('renter', 'buyer')

income = 40000
savings = 20000

rent = 770
house_value = 200000  # (177500 + 179900 + 186600) / 3
insurance = ((1020 + 1191 + 1390) / 3) / 12
property_tax = (((0.0089 + 0.00977) / 2) / 12) * house_value
maintenance = (0.02 * house_value) / 12  # Rule of thumb: 2-5%

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

pmi = 0.005 * (house_value - savings)  # Rule of thumb: 0.5-1% of original loan
print(pmi / 12)

# Todo Figure this out
rate_30yr_0_pts = (4.0, 4.0, 4.0, 4.0, 4.0, 4.25, 4.375, 4.0, 4.19, 4.25, 5.125)
apr_30yr_0_pts = (4.269, 4.270, 4.289, 4.310, 4.0, 4.299, 4.375, 4.045, 4.249, 4.25, 5.215)
fees_30yr_0_pts = (234, 253, 641, 1082, 1, 1150, 0, 972, 1258, 0, 1825)

rate_15yr_0_pts = (3.5, 3.625, 3.625, 3.625, 3.5, 3.5, 3.75, 3.625, 3.75, 3.79)
apr_30yr_0_pts = (3.778, 3.824, 3.847, 3.854, 3.5, 3.584, 3.823, 3.656, 3.75, 3.893)
fees_30yr_0_pts = (1095, 134, 410, 493, 1, 1150, 995, 383, 0, 1258)

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


if __name__ == '__main__':

    for chump in chumps:
        compute_monthly_cost(chump)
