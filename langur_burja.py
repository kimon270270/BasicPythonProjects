import random

MIN_BALANCE=10

symbol_value={
    1:"Hukum",
    2:"Paan",
    3:"Chidi",
    4:"Itta",
    5:"Jhanda",
    6:"Burja"
}

def choose_your_bet():
    while True:
        bet=input("Choose one Hukum = 1/ Paan = 2/ Chidi = 3/ Itta = 4/ Jhanda = 5/ Burja = 6.\n")
        if bet.isdigit():
            bet=int(bet)
            if 1<=bet<=6:
                break
            else:
                print("Invalid Input")
        elif bet=='q':
            break
        else:
            print("Invalid Input")
            
    return bet
        
        
def place_your_bet():
    print("WELCOME!!!")
    print("Please place your bet.")
    print(f"Minimum Balance to play is ${MIN_BALANCE}")
    while True:
        amount=input("Please enter the amount\n")
        if amount.isdigit():
            amount=int(amount)
            if amount<MIN_BALANCE:
                print(f"Minimum Balance to place your bet is ${MIN_BALANCE}")
                
            elif amount>MIN_BALANCE:
                print(f"Your bet is ${amount}")
                break
                
            else:
                print("Invalid Input. Please enter a number.")
                
    return amount
       
                
                
def dice(value1):
    die=[]
    for i in range (0,6):
        die.append(random.randint(1,6))
        
    count=0
        
    for i in range (0,6):
        if value1 == die[i]:
            count+=1
            
    print(die)       
    return count
            
            
    
    
def check_winnings(re_count, re_amount):
    if re_count>=2:
        winning=re_count*re_amount
        print(f"Congratulations!!! You have won ${winning}.")
        
    else:
        print("You lost.")
                


def main():
    returned_amount=place_your_bet()
    returned_bet=choose_your_bet()
    returned_count=dice(returned_bet)
    check_winnings(returned_count,returned_amount)
    while True:
        answer=input("Do you want to play again?(yes/no)\n").lower()
        if answer=="yes":
            main()
            
        else:
            print("Thank you for playing.")
            quit()
    
main()