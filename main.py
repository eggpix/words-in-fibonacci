import string
import sys

sys.set_int_max_str_digits(0)

DIGITS = string.ascii_lowercase


def decimal_to_base_26(num):
    if num == 0:
        return "a"

    result = []

    while num:
        num, remainder = divmod(num, 26)
        result.append(DIGITS[remainder])

    return "".join(reversed(result))


fibonacci_1 = 0
fibonacci_2 = 1

print("Writing...")
with open("long_number.txt", "w") as file:
    for i in range(25000):
        file.write(
            f"Fibonacci index {i}: {decimal_to_base_26(fibonacci_1)}\n\n"
        )

        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
print("Done.")