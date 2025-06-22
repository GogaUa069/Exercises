from tqdm import tqdm
from random import choice
import time


def step_stop():
    print()
    time.sleep(0.5)


best_answers = ("Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом")
good_answers = ("Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да")
middle_answers = ("Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать",
                  "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять")
bad_answers = ("Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие",
               "Весьма сомнительно")

answers = [*best_answers, *good_answers, *middle_answers, *bad_answers]


def magic_circle():
    print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
    step_stop()
    print("Какой у тебя вопрос?")
    step_stop()
    input("-----> ")
    step_stop()
    data = [i for i in range(100)]
    print("Подожди, я думаю...")
    print()

    for _ in tqdm(data):
        time.sleep(0.1)
    print()
    print(f"Hа твой вопрос я отвечу так: {choice(answers)}")


magic_circle()
