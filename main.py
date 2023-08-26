#global constants
import random

MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

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
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machines(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()



print("Begin Program")

def deposit():
    while True: 
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"You have deposited ${amount}")
                break
            else: print("amount must be greater than zero")

        else:
            print("please enter a valid numerical value")
    return amount

def number_of_lines():
    while True: 
        lines = input("How many lines would you like to bet on(1 - 3)? ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                print("You have chosen to bet on",lines, "lines")
                #print("amount is a digit")

                break
            else: print(f"lines must be between {MIN_LINES} and {MAX_LINES}")

        else:
            print("please enter a valid value")
    return lines

def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                #print("You have chosen to bet",bet, "on each line")
                break
            else: print(f"bet must be between ${MIN_BET} and ${MAX_BET}")

        else:
            print("please enter a valid value")
    return bet 

def check_winnnigs(columns, lines, bet, values):
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


 

#Defining main
def main():
    balance = deposit()
    lines = number_of_lines()
    #print(balance, lines)
    while True:
        bet = get_bet()
        total = bet * lines
        if total > balance:
            print(f"You have insufficient balance. Current balance: ${balance}")
        else:
            break
    print(f"You have chosen to bet ${bet} on {lines} lines. Total bet: ${total}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machines(slots)
    winnings, winning_lines = check_winnnigs(slots, lines, bet, symbol_value)
    print(f"You won: ${winnings}")
    print(f"You won on lines:", *winning_lines)

#Calling main

main()

# to-do:
# check if the balance is enough to cover the total bet.
# a 3x3 slot machine with symbols for matching.
# use symbols with a value to create columns.
# generate random columns.
# see if match and declare win.
# calculate running balance.
