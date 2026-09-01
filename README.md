# words-in-fibonacci

This project converts elements of the Fibonacci sequence to base 26 (`a-z`), then searches the resulting strings for English words.

Run [`find_words.py`](src/find_words.py) to generate a file `fibonacci_words.txt` containing the words found. You can modify the number of Fibonacci elements checked by changing the `LOOP_NUM` variable. By default, words shorter than 5 characters are excluded, but this can be changed by modifying `MIN_WORD_LENGTH`.

Once you've found a list of words, you can inspect the corresponding base-26 strings by running [`generate_sequence.py`](src/generate_sequence.py). The program will ask for a Fibonacci index and then print the raw base-26 string for that element.

## Attribution

English word list: [Google 10,000 English](https://github.com/first20hours/google-10000-english)