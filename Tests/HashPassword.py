import hashlib


def my_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()


hash_password = "3d5f0cc0d0f16a54d8eb3c5937a3dfccc92e2147fa6d51cfec2409d6bb2ec455"
input_password = input("Enter password: ")
hash_input_password = my_hash(input_password)

if hash_input_password == hash_password:
    print("You have logged in!")
else:
    print("You have not autorized!")