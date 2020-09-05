from colorama import Fore, Back, Style, init

init()

def print_red(msg):
    print(Fore.RED + str(msg) + Style.RESET_ALL)

def print_green(msg):
    print(Fore.GREEN + str(msg) + Style.RESET_ALL)
