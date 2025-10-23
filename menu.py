from colorama import Fore, Style, init

init(autoreset=True)

def title():
    print(Fore.CYAN + Style.BRIGHT + r"""
     ________  ___  _____ ______   ________  ___           ___    ___ ________  ________  _________   
|\   ____\|\  \|\   _ \  _   \|\   __  \|\  \         |\  \  /  /|\   __  \|\   __  \|\___   ___\ 
\ \  \___|\ \  \ \  \\\__\ \  \ \  \|\  \ \  \        \ \  \/  / | \  \|\ /\ \  \|\  \|___ \  \_| 
 \ \_____  \ \  \ \  \\|__| \  \ \   ____\ \  \        \ \    / / \ \   __  \ \  \\\  \   \ \  \  
  \|____|\  \ \  \ \  \    \ \  \ \  \___|\ \  \____    \/  /  /   \ \  \|\  \ \  \\\  \   \ \  \ 
    ____\_\  \ \__\ \__\    \ \__\ \__\    \ \_______\__/  / /      \ \_______\ \_______\   \ \__\
   |\_________\|__|\|__|     \|__|\|__|     \|_______|\___/ /        \|_______|\|_______|    \|__|
   \|_________|                                      \|___|/                                      
    """)

def show_menu():
    print("\n" + Fore.YELLOW + "="*60 + "\n")
    print(Fore.GREEN + Style.BRIGHT + "🤖 Welcome to Simplybot!\n")

    print(Fore.WHITE + "Simplybot can perform several actions. Type one of the commands below:\n")

    print(Fore.CYAN + " chat" + Fore.WHITE + "  → Simplybot will greet you back")
    print(Fore.CYAN + " math" + Fore.WHITE + "  → Perform basic mathematical calculations")
    print(Fore.CYAN + " randf" + Fore.WHITE + " → Get a random fact from the internet")
    print(Fore.CYAN + " showweather" + Fore.WHITE + " → Get current weather for a location")
    print(Fore.CYAN + " exit" + Fore.WHITE + " → Exit Simplybot\n")

    print(Fore.YELLOW + "="*60 + "\n")

# Example usage
if __name__ == "__main__":
    title()
    show_menu()
