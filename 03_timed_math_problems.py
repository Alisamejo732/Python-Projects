import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERATOR = 3
MAX_OPERATOR = 12
TOTAL_PROBLEMS = 10

def generate_problems():
    left = random.randint(MIN_OPERATOR, MAX_OPERATOR)
    right = random.randint(MIN_OPERATOR, MAX_OPERATOR)
    operator = random.choice(OPERATORS)

    expr = f'{left} {operator} {right}'
    answer = eval(expr)
    return expr, answer

if (input('Are you ready to begin y/n: ')) == 'y':
    start = time.time()
    wrong = 0
    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problems()
        while True:
            guess = input(f'Problem #{i + 1}: {expr} = ')
            if guess == str(answer):
                break
            wrong += 1
    end = time.time()
    print(f'You accuracy was {((TOTAL_PROBLEMS - wrong) * 100) / TOTAL_PROBLEMS}%\nYou finsihed all problems in {round(end - start, 2)}s')
else:
    pass

