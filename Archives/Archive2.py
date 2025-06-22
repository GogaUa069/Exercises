import time


def greet():
    while True:
        name = yield
        for let in name:
            time.sleep(0.21)
            print(let, end="", flush=True)
        print(sep="\n")
        time.sleep(1.5)


g = greet()
g.send(None)
g.send("Creators:")
g.send("Goga")
g.send("Alex")
