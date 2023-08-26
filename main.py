#global constants
MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3


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

#Calling main

main()

# to-do:
# check if the balance is enough to cover the total bet.
# a 3x3 slot machine with symbols for matching.
# use symbols with a value to create columns.
# generate random columns.
# see if match and declare win.
# calculate running balance.
