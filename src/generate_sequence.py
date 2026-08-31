import sys
from base26 import to_base_26

sys.set_int_max_str_digits(0)

print("Get an index from the Fibonacci sequence in base 26")
index = int(input("Index: "))

fibonacci_1 = 0
fibonacci_2 = 1

for i in range(index):
    fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2

print(to_base_26(fibonacci_1))