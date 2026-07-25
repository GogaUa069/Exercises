from time import time
from colorama import Fore, Style
import yaml


def communicate(text, color):
    return getattr(Fore, color) + text + Style.RESET_ALL


with open("data.yaml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)
    the_best_time = data["the_best_time"]

input(communicate("[ENTER] to start", "LIGHTRED_EX"))
print()

start_time = time()
input_text = input(communicate("<<< ", "LIGHTWHITE_EX"))
end_time = time()

time_result = round(end_time - start_time, 3)

if input_text == "hello worl" and time_result <= 3.000:
    print(communicate("\nAttempt passed.\n", "LIGHTGREEN_EX"))
    if time_result < the_best_time:
        print(communicate("New record!", "LIGHTCYAN_EX"))
        print(communicate(f"Old record: {the_best_time} s", "LIGHTWHITE_EX"))
        print(communicate(f"New record: {time_result} s", "LIGHTWHITE_EX"))
        print(communicate(f"\nDifference: {communicate("-" + str(round(the_best_time - time_result, 3)) + " s", "LIGHTGREEN_EX")}", "LIGHTWHITE_EX"))
        with open("data.yaml", "w", encoding="utf-8") as file:
            yaml.dump({"the_best_time": time_result}, file)
    else:
        print(communicate(f"Record: {the_best_time} s", "LIGHTWHITE_EX"))
        print(communicate(f"Time: {time_result} s", "LIGHTWHITE_EX"))
        print(communicate(f"\nDifference: {communicate("+" + str(round(time_result - the_best_time, 3)) + " s", "LIGHTRED_EX")}", "LIGHTWHITE_EX"))
else:
    print(communicate("\nAttempt not passed.", "LIGHTRED_EX"))
