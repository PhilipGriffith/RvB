chumps = ('renter', 'buyer')

income = 40000

rent = 770
house_value = (177500 + 179900 + 186600) / 3
insurance = (1020 + 1191 + 1390) / 3
property_tax = ((0.0089 + 0.00977) / 2) * house_value
maintenance = 0.02 * house_value # Rule of thumb: 2-5%

# Todo Figure this out
mortgage = 0


monthly_cost = {'renter': rent, 'buyer': mortgage}
monthly_utilities = {'renter': 90, 'buyer': 200}

yearly_maintenance = {'renter': 0, 'buyer': maintenance}
yearly_property_tax = {'renter': 0, 'buyer': property_tax}
yearly_insurance = {'renter': 0, 'buyer': insurance}

def compute_yearly_cost(chump):

    costs = monthly_cost[chump] * 12 + \
            monthly_utilities[chump] * 12 + \
            yearly_maintenance[chump] + \
            yearly_property_tax[chump] + \
            yearly_insurance[chump]

    print('Total {} yearly costs: {:.2f}'.format(chump, costs))
    return costs


if __name__ == '__main__':

    for chump in chumps:
        compute_yearly_cost(chump)
