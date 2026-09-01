import time
from base26 import to_base_26

LOOP_NUM = 10000
MIN_WORD_LENGTH = 5
ASSET_DIR = "./assets/"
OUTPUT_FILE = "./fibonacci_words.txt"

word_trie = {}
max_word_length = 0

with open(ASSET_DIR + "words.txt") as word_file:
    for line in word_file:
        word = line.strip()

        if len(word) < MIN_WORD_LENGTH:
            continue

        max_word_length = max(max_word_length, len(word))

        node = word_trie
        for char in word:
            node = node.setdefault(char, {})

        node[None] = word

fibonacci_1 = 0
fibonacci_2 = 1

print("Writing...")
start_time = time.perf_counter()

with open(OUTPUT_FILE, "w") as fib_file:
    fib_file.write(f"English words of {MIN_WORD_LENGTH} characters or more in the first {LOOP_NUM} elements of the base 26 Fibonacci sequence:\n\n")
    for i in range(LOOP_NUM):
        alpha_string = to_base_26(fibonacci_1)
        matching_words = set()

        string_length = len(alpha_string)

        for start in range(string_length):
            node = word_trie

            for pos in range(start, min(start + max_word_length, string_length)):
                node = node.get(alpha_string[pos])

                if node is None:
                    break

                if None in node:
                    matching_words.add(node[None])

        if matching_words:
            fib_file.write(
                f"{i}: {', '.join(matching_words)}\n"
            )

        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2

        if (i + 1) % 100 == 0:
            print(f"{i + 1}/{LOOP_NUM}")

end_time = time.perf_counter()
print("Done.")
print(f"Finished in {end_time - start_time:.2f} seconds.")