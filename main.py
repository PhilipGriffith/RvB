
class House:

    def __init__(self):
        self.price = 200000
        self.value = self.price
        self.appreciation_rate_percent = 4.7  # 2.53? Also see below.
        self.mortgage_price = self.value + self.compute_closing_cost()

    def appreciate(self):
        self.value += self.value * (self.appreciation_rate_percent / 100)

    @staticmethod
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


class Apartment:

    def __init__(self):
        self.rent = 770
        self.rent_increase_percent = 2  # Approximates the rise from $630 to $770 at Londontown over the past 10 years

    def rent_increase(self):
        self.rent += self.rent * (self.rent_increase_percent / 100)


class MonthlyHousing:

    def __init__(self, loan=None, house_price=None, house_value=None, rent=None):
        super().__init__()
        self.payment = loan.payment if loan else rent
        self.utilities = 180 if loan else 90
        self.maintenance = (0.02 * house_price) / 12 if loan else 0  # Rule of thumb: 2-5%
        # Assuming static insurance and property tax rates
        self.insurance = ((1020 + 1191 + 1390) / 3) / 12 if loan else 0
        self.property_tax = (((0.0089 + 0.00977) / 2) / 12) * house_value if loan else 0
        self.cost = sum((self.payment, self.utilities, self.maintenance, self.insurance, self.property_tax))

    def details(self):
        print('Loan payment:', self.payment)
        print('Utilities:', self.utilities)
        print('Maintenance:', self.maintenance)
        print('Insurance:', self.insurance)
        print('Property tax:', self.property_tax)
        print('Total:', self.cost)


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
        if self.number_of_payments == 0:
            self.payment = 0

    def details(self, v=False):
        if v:
            print('Interest rate: {:.2f}%'.format(self.annual_interest_rate * 100))
            print('Payment: {:.2f}'.format(self.payment))
        print('Amount: {:.2f}'.format(self.amount))
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
        self.amount += amount

    def fee(self):
        self.amount -= self.amount * (self.fee_rate_percent / 100)

    def sell(self):
        return self.amount - (self.amount * (self.commission_rate_percent / 100))

    def details(self):
        print('Amount: {:.2f}'.format(self.amount))


# "Your monthly payment is based on the interest rate and principal balance, not the APR."
rate_30yr_0_pts = (4.0, 4.0, 4.0, 4.0, 4.0, 4.25, 4.375, 4.0, 4.19, 4.25, 5.125)
rate_15yr_0_pts = (3.5, 3.625, 3.625, 3.625, 3.5, 3.5, 3.75, 3.625, 3.75, 3.79)


if __name__ == '__main__':

    balance = 20000
    years = 30

    # House with 30-year Mortgage
    house = House()
    loan_amount = house.mortgage_price - balance
    loan = Loan(loan_amount)
    balance = 0

    # Apartment
    apartment = Apartment()

    # Todo Add investment

    for month in range(years * 12):

        house_cost = MonthlyHousing(loan, house.price, house.value).cost
        rent_cost = MonthlyHousing(rent=apartment.rent).cost
        difference = house_cost - rent_cost

        if loan.number_of_payments > 0:
            loan.make_payment()

        if not month % 12:
            house.appreciate()
            apartment.rent_increase()

    print(house.value)



# Annual Home Price Appreciation Rates
x = (3.69,
     4.36,
     0.27,
     7.33,
     1.48,
     4.78,
     1.50,
     4.38,
     1.00,
     4.43,
     4.73,
     -0.33,
     5.43,
     6.94,
     6.57,
     9.57,
     15.11,
     16.64,
     8.81,
     -0.50,
     -7.06,
     -8.40,
     -5.95,
     -5.89,
     -5.51,
     4.76,
     2.04,
     6.07,
     2.84,
     9.17)
print(sum(x)/len(x))


# Average monthly rent
# Date 	Tallahassee, FLMedian
# 2017 	$977
# 2016 	$958
# 2015 	$930
# 2014 	$920
# 2013 	$863
# 2012 	$899
# 2011 	$939
# 2010 	$969
# 2009 	$922
# 2008 	$957
# 2007 	$926
# 2006 	$934