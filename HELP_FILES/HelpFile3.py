def check_password(password):
    true_password = "1240"
    return password == true_password


import sys
import time

PIN_LENGTH = 4
charset = "0123456789"
guess = None

attempts = 0
start = time.time()

for num in range(10**PIN_LENGTH):
    guess = f"{num:0{PIN_LENGTH}d}"
    attempts += 1

    sys.stdout.write(f"\rTrying: {guess}")
    sys.stdout.flush()

    if check_password(guess):
        break

duration = time.time() - start

print()
print(f"[+] Password found: {guess}")
print(f"Attempts: {attempts}, time: {duration:.4f} secs")
