import os
from datetime import datetime
import random
import time


def clear_screen():
    os.system("clear")


def random_n_digit(n):
    if n < 1:
        raise ValueError("Number of digits must be at least 1")
    return random.randint(10 ** (n - 1), 10**n - 1)


def word_to_number(word):
    number = 0
    for char in word:
        if char in sym2dig.keys():
            number = number * 10 + sym2dig[char]
    return number


def number_to_word(number):
    answer = list()
    for char in str(number):
        answer.append(dig2sym[int(char)])
    return "".join(answer)


def write_summary_to_file(datetime_str, success_rate, avg_speed):
    with open("summary.txt", "a") as file:
        file.write(
            f"{datetime_str} - Success rate: {success_rate:.2f}% - Speed: {avg_speed:.2f} seconds/guess\n"
        )


clear_screen()

dig2sym = {
    1: "м",
    2: "д",
    3: "т",
    4: "к",
    5: "л",
    6: "б",
    7: "г",
    8: "в",
    9: "р",
    0: "н",
}
sym2dig = {val: key for key, val in dig2sym.items()}

n = int(input("Choose number length\n"))

correct_guesses = 0
total_attempts = 0

start_time = time.time()


while True:
    clear_screen()
    number = random_n_digit(n)
    print(number)
    word = input("Write out the correspondence (or type 'exit' to quit):\n")

    if word.lower() == "exit":
        end_time = time.time()  # Record the end time of the program
        total_time = end_time - start_time  # Calculate total runtime
        avg_speed = total_time / total_attempts if total_attempts > 0 else 0

        if total_attempts == 0:
            print("No attempts made.")
        else:
            success_rate = (correct_guesses / total_attempts) * 100
            print(
                f"You guessed correctly {correct_guesses} out of {total_attempts} times."
            )
            print(f"Success rate: {success_rate:.2f}%")
            print(f"Total time: {total_time:.2f} seconds.")
            print(f"Average time per guess: {avg_speed:.2f} seconds.")
            datetime_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_summary_to_file(datetime_str, success_rate, avg_speed)
        break

    input_number = word_to_number(word)
    total_attempts += 1

    if number == input_number:
        print("Correct")
        correct_guesses += 1
    else:
        print("Wrong. Correct sequence is:")
        print(number_to_word(number))

    input("Press Enter to continue...")
