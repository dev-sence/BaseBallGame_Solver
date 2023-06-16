import random
import time

def generate_possible_numbers():
    possible_numbers = []
    for i in range(1, 10):
        for j in range(1, 10):
            if j != i:
                for k in range(1, 10):
                    if k != i and k != j:
                        for l in range(1, 10):
                            if l != i and l != j and l != k:
                                possible_numbers.append([i, j, k, l])
    return possible_numbers

def get_random_guess(possible_numbers):
    return random.choice(possible_numbers)

def get_feedback(secret, guess):
    strikes = 0
    balls = 0

    for i in range(4):
        if guess[i] == secret[i]:
            strikes += 1
        elif guess[i] in secret:
            balls += 1
    
    return strikes, balls

def filter_possible_numbers(possible_numbers, guess, strikes, balls):
    filtered_numbers = []
    for number in possible_numbers:
        s, b = get_feedback(number, guess)
        if s == strikes and b == balls:
            filtered_numbers.append(number)
    return filtered_numbers

def play_game():
    possible_numbers = generate_possible_numbers()
    attempts = 0

    print("[ ! ] 게임을 시작합니다")

    while True:
        guess = get_random_guess(possible_numbers)
        attempts += 1
        print(f"제시된 숫자: {guess}")
        strikes = int(input("스트라이크 수: "))
        balls = int(input("볼 수: "))
        if strikes == 4:
            print(f" [ ! ] 정답입니다. 시도 횟수: {attempts}")
            time.sleep(5)
            break
        possible_numbers = filter_possible_numbers(possible_numbers, guess, strikes, balls)
        if not possible_numbers:
            print("[ ! ] 상대의 숫자에 모순이 있습니다.")
            time.sleep(5)
            break

play_game()