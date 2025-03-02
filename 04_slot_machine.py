import random

MAX_LINES = 3
MIN_LINES = 1
MIN_BET = 1
MAX_BET = 1000
ROWS = 3
COLS = 3
symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}
symbol_values = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
        
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            print(column[row], "|" if i != len(columns) -1 else "", end="")
        print()

def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount mus be greater than 0")
        else:
            print("Please enter a valid deposit value..")
    return amount


def get_number_of_lines():
    while True:
        try:
            lines = int(input(f"How many lines you would bet on from {MIN_LINES} to {MAX_LINES}: "))
            if lines >= MIN_LINES and lines <= MAX_LINES:
                break
            else:
                print(f'Enter lines between {MIN_LINES} and {MAX_LINES}...')
        except:
            print('Invalid number of lines..')
    return lines

def get_bet():
    while True:
        try:
            bet = int(input(f"How much would you like to bet on each line: "))
            if bet >= MIN_BET and bet <= MAX_BET:
                break
            else:
                print(f'Enter bet b/w ${MIN_BET} and ${MAX_BET}...')
        except:
            print('Invalid bet..')
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet <= balance > 0:
            break
        else:
            print("Bet amount exceeded balance amount $...")

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to {total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    print("You won on ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play or 'q' to quit ")
        if answer.lower() == 'q':
            break
        balance += spin(balance )
    print(f"You left with ${balance}")
main()

