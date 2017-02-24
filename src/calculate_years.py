"""Implementation of the Kata Money, Money, Money."""


def calculate_years(principal, interest, tax, desired):
    """Caculate how many years it take to reach desired principle."""
    years = 0
    while (principal < desired):
        accrued = principal * interest
        accrued = accrued - (accrued * tax)
        principal += accrued
        years += 1

    return years
