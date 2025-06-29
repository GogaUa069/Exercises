import threading

def get_input():
    global user_input
    user_input = input("Masz 5 sekund na odpowiedź: ")

user_input = None
thread = threading.Thread(target=get_input)
thread.start()
thread.join(timeout=5)

if user_input:
    print("Twoja odpowiedź:", user_input)
else:
    print("\nCzas minął!")
