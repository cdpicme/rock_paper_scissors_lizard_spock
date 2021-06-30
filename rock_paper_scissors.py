import random
from termcolor import colored

welcome = "|        Welcome to         |\n" \
          "|  Rock - Paper - Scissors  |\n" \
          "|       Lizard - Spock      |\n"
banner = "+" + "*" * int((len(welcome)/3)-3) + "+\n"
border = "|" + " " * int((len(welcome)/3)-3) + "|\n"

s1 = 0
scomp = 0
p1 = None
playList = []

choices = {
    1:"Rock",
    2:"Paper",
    3:"Scissors",
    4:"Lizard",
    5:"Spock",
    0:"Quit"
    }

def play_game(p1,p2):
    winner = None
    verb = ''
    if p1 == p2:
        print(colored("\n\nIt's a TIE!\n\n","yellow"))
        playList.append("T - " + choices[p1] + " TIED " + choices[p2])
    elif p1 == 1:
        if p2 == 2:
            winner = p2
            verb = "covered by"
        elif p2 == 3 or p2 == 4:
            winner = p1
            verb = "crushes"
        else:
            winner = p2
            verb = "vaporized by"
    elif p1 == 2:
        if p2 == 1:
            winner = p1
            verb = "covers"
        elif p2 == 3:
            winner = p2
            verb = "cut by"
        elif p2 == 4:
            winner = p2
            verb = "eaten by"
        else:
            winner = p1
            verb = "disproves"
    elif p1 == 3:
        if p2 == 1:
            winner = p2
            verb = "crushed by"
        elif p2 == 2:
            winner = p1
            verb = "cuts"
        elif p2 == 4:
            winner = p1
            verb = "decapitates"
        else:
            winner = p2
            verb = "smashed by"
    elif p1 == 4:
        if p2 == 1:
            winner = p2
            verb = "crushed by"
        elif p2 == 2:
            winner = p1
            verb = "eats"
        elif p2 == 3:
            winner = p2
            verb = "decapitated by"
        else:
            winner = p1
            verb = "poisons"
    elif p1 == 5:
        if p2 == 1:
            winner = p1
            verb = "vaporizes"
        elif p2 == 2:
            winner = p2
            verb = "disproved by"
        elif p2 == 3:
            winner = p1
            verb = "smashes"
        else:
            winner = p2
            verb = "poisoned by"

    if winner != None:
        if winner == p1:
            global s1
            s1 += 1
            print(colored("\n\n" + choices[p1].upper() + " ","green") + colored(verb.upper(),"yellow") + colored(" " + choices[p2].upper() + "\n\nCongrats!!! YOU WIN!\n\n","green"),end='')
            playList.append("W - " + choices[p1] + " " + verb + " " + choices[p2])
        else:
            global scomp
            scomp += 1
            print(colored("\n\n" + choices[p1].upper() + " ","red") + colored(verb.upper(),"yellow") + colored(" " + choices[p2].upper() + "\n\nSorry... YOU LOSE.\n\n","red"),end='')
            playList.append("L - " + choices[p1] + " " + verb + " " + choices[p2])

def print_menu():
    for x, y in choices.items():
        print(f"{x} - {y}")

def print_rules():
    print("\n\n" + " " * 4 + "Scissors CUT Paper.")
    print("" + " " * 4 + "Paper COVERS Rock.")
    print("" + " " * 4 + "Rock CRUSHES Lizard.")
    print("" + " " * 4 + "Lizard POISONS Spock.")
    print("" + " " * 4 + "Spock SMASHES Scissors.")
    print("" + " " * 4 + "Scissors DECAPITATES Lizard.")
    print("" + " " * 4 + "Lizard EATS Paper.")
    print("" + " " * 4 + "Paper DISPROVES Spock.")
    print("" + " " * 4 + "Spock VAPORIZES Rock.")
    print("" + " " * 4 + "And, as it always has,")
    print("" + " " * 4 + "Rock CRUSHES Scissors.\n\n")

def print_playList():
    print(colored("\n\n  ===== Game Results =====","cyan"))
    for x in playList:
        if x[0] == 'W':
            print(colored(x,"green"))
        elif x[0] == "L":
            print(colored(x,"red"))
        else:
            print(colored(x,"yellow"))
    print(colored("  ======  " + str(len(playList)) + " turns  ======", "cyan"))
    print("\n\n")
            

def print_turn(p1,p2):
    print(f"\n\nYou chose: {choices[p1].upper()} <<===>> Computer chose: {choices[p2].upper()}")

def main():
    print(colored("\n\n\n" + banner + border + welcome + border + banner, "cyan"))
    print_rules()
    while True:
        if s1 == 11:
            print_playList()
            print(colored("YOU WIN the GAME " + str(s1) + " - " + str(scomp),"green"))
            input("\n\npress [Enter] to exit...")
            break
        elif scomp == 11:
            print_playList()
            print(colored("COMPUTER WINS the GAME " + str(scomp) + " - " + str(s1),"red"))
            input("\n\npress [Enter] to exit...")
            break
        else:
            if s1 > scomp:
                print(colored("-" * 20 + "\nCurrent Score","white"),colored("\nPlayer 1: " +  str(s1) + "  <<<<","green"),colored("\nComputer: " + str(scomp) + "\n" + "-" * 20,"white"))
            elif s1 < scomp:
                print(colored("-" * 20 + "\nCurrent Score","white"),colored("\nPlayer 1: " +  str(s1),"white"),colored("\nComputer: " + str(scomp) + "  <<<<","green") + "\n" + "-" * 20)
            else:
                print(colored("-" * 20 + "\nCurrent Score - TIED\nPlayer 1: " + str(s1) + "\nComputer: " + str(scomp) + "\n" + "-" * 20,"white"))
            print_menu()
            try:
                p1 = int(input("\n(make a selection [1 - 5] (0 to quit))\n\n" + colored("THREE...","red") + colored("TWO...","yellow") + colored("ONE...","cyan") + colored("SHOOT! ====>>>  ","green")))
                if p1 == 0:
                    print("User selected 0 - (Quit) Thanks for playing!")
                    break
            # elif p1 == 9:
            #     print_rules()
                else:
                    p2 = random.randint(1,5)
                    print_turn(p1,p2)
                    play_game(p1,p2)
            except (ValueError, TypeError, KeyError) as e:
                print_rules()
                print(colored(f"Please enter a value from zero to five [0 - 5].","red"))

if __name__ == "__main__":
    main()