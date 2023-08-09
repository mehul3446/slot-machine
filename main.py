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
                print(amount)
                print("amount is a digit")
                break
            else: print("amount must be greater than zero")

        else:
            print("please enter a valid numerical value")
    return amount

def number_of_lines():
    while True: 
        lines = input("How many lines would you like to bet on? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0:
                print(lines)
                #print("amount is a digit")
                break
            else: print("lines must be greater than zero")

        else:
            print("please enter a valid numerical value")
    return lines
 

#calling the function
def main():
    balance = deposit()
