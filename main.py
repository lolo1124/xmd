import os


versionFile = "C:\\Users\\cokat\\Desktop\\python\\learning\\version.txt"




def change_color(option):
    colors = {
        "1": "1", "2": "2", "3": "3",
        "4": "4", "5": "5", "6": "6", "7": "7",
        "8": "8", "9": "9", "A": "A", "B": "B",
        "C": "C", "D": "D", "E": "E", "F": "F"
    }

    color_code = option.split()[-1]  # Get the last part of input (e.g., "color 2" → "2")
    if color_code.upper() in colors:
        os.system(f'color {colors[color_code.upper()]}')
    elif not color_code.isdigit() or not (1 <= int(color_code) <= 9):
        print("\nInvalid color code, enter a number between 1 and 9 or C, D, E, F\n")

    else:
        print(f"'{option}' is not recognized as an internal or external command.")

help = """For more information on a specific command, type HELP command-name

        CLS         Clears the screen
        COLOR       Changes the color of xmd
        UPDATE      Checks for updates
        CHANGELOG   Outputs the changes made to xmd
        TUTORIAL    Explains how xmd works 
        QUIT        No brainer
        
        DOWNLOAD    Downloads the selected files from X-Force (needs command-name after)
        INJECT      Starts the injector
        GTA         Starts GTA
        REINSTALL   Reinstalls X-Force
        LINKS       Opens the link associated with X-Force
        REMOVE      Removes a specific folder such as headers (needs command-name after)
        ONLINE      Checks if X-Force is online
        LOGIN       Shows your login info
        
        HWID        Provieds a step by step guide on how to fix hwid does not match
        PASSWORD    Explains how you can get your password reseted
        """

def online():
    pass

def versionCheck():
   
    f = open("version.txt", "r")
    version = (f.read())
    f.close()
    

    return version


def main():
    version = versionCheck()
    print(f"X-Force Catpows [{version}]") 
    print("""(c) X-Force Corporation. All rights reserved.\n""") 
    while True:  
        choice = input("C:\\Users\\xforce>")  
        option = choice.strip()
        x = option.lower()

        if x == "tester":  
            print("Debug")
        elif x.startswith("color "):
            change_color(option)
        elif x == ("color"):
            print('Invalid color use please enter "color (number 1-9)"')
        elif x == "cls":
          os.system('cls')
        elif x =="help":
            print(help)
        elif x =="quit":
            break
        elif x == "":
            continue
        else:
            print(f"'{option}' is not recognized as an internal or external command,")
            print("operable program or batch file.")
            
main()
