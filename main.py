#global constants
MIN_LINES = 1
MAX_LINES = 3


print("Begin Program")

def deposit():
    while True: 
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print("You have deposited ", amount)
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
 

#Defining main
def main():
    balance = deposit()
    lines = number_of_lines()
    print(balance, lines)

#Calling main

main()
