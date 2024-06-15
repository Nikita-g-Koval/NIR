import decimal
import math


def get_values(left_bound: decimal, right_bound: decimal, step: decimal, margin_of_error: int):
    values = []

    x = left_bound

    while x <= right_bound:
        y = math.sin(x) - math.cos(x)
        values.append((x, round(y, margin_of_error)))

        x += step

    return values
