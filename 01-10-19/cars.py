"""
Exercise 2.10 (page 81, modified): select between hybrid and regular cars based on
depreciation and gas costs. The class version is a bit better because of the way
it holds all the info and logic together for good cohesion.

Copyright (c) 2019, Sekhar Ravinutala.
"""

# Loop version.
def _choice(years, miles_per_year, gas_price, hybrid, regular):
    for car in [hybrid, regular]:
        car["total_cost"] = car["cost"] - car["resale_value"] +\
            gas_price * years * miles_per_year / car["mpg"]

    return "Hybrid" if hybrid["total_cost"] < regular["total_cost"] else "Regular"

def _pick_with_loop():
    return _choice(
        years=5,
        miles_per_year=12000,
        gas_price=2.9,
        hybrid={
            "cost": 36000,
            "resale_value": 29000,
            "mpg": 34
        },
        regular={
            "cost": 21000,
            "resale_value": 16000,
            "mpg" : 21
        }
    )

# Class version.
class _Car():
    def __init__(self, cost, resale_value, mpg):
        self.cost, self.resale_value, self.mpg = cost, resale_value, mpg

    def total_cost(self, years, miles_per_year, gas_price):
        """
        Return total cost based on depreciation and gas price.
        - years: Years in use.
        - resale_value: Value at end of use.
        - gas_price: Mean gas price over use period.
        """
        return self.cost - self.resale_value +\
            gas_price * years * miles_per_year / self.mpg

def _pick_with_class():
    hybrid_cost = _Car(36000, 29000, 34).total_cost(5, 12000, 2.9)
    regular_cost = _Car(21000, 16000, 21).total_cost(5, 12000, 2.9)

    return "Hybrid" if hybrid_cost < regular_cost else "Regular"

if __name__ == "__main__":
    print(_pick_with_loop(), _pick_with_class())
