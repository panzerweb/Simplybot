# This will be my first python project
# A simple chatbot
# This will have very simple features
# But sooner, I intend to update with actual AI integration

# Custom modules
from modules import calculation
from modules import randf
from modules import weather
from modules import chatbot
import menu

# Predefined modules
from typing import List
from colorama import Fore, Style, init

# Variables needed
operations: List[str] = ["add", "subtract", "divide", "multiply"]
    
init(autoreset=True)
# Main function
def main():
    
    # Fetch the JSON file for all knowledge as a dictionary
    knowledge_base = chatbot.load_knowledge('knowledge_base.json')

    # Run program
    while True:
        
        # Opening
        menu.title()
        menu.show_menu()

        # First user input
        inputChoice: str = input('Enter command: ').lower()

# Ignores "Enter" keypress to execute else statement
        if not inputChoice.strip():
            continue
# Chatbot implementation
        if inputChoice == 'chat':
            print("\n" + Fore.YELLOW + "="*50 + "\n")
            print(Fore.GREEN + Style.BRIGHT + "💬 Entering Chat Mode...\n")
            print(Fore.WHITE + "Type " + Fore.CYAN + "'quit'" + Fore.WHITE + " to exit the chat feature.\n")

            while True:
                chat_input = input(Fore.CYAN + "You: " + Fore.RESET).strip().lower()

                if chat_input == 'quit':
                    print("\n" + Fore.GREEN + "Simplybot: Goodbye! Have a great day! 🌞\n")
                    break

                if not chat_input:
                    print(Fore.RED + "Simplybot: Please type something before pressing Enter.")
                    continue

                # Match question
                questions_list = [q["question"] for q in knowledge_base["questions"]]
                best_match = chatbot.find_best_match(chat_input, questions_list)

                if best_match:
                    answer = chatbot.get_answer_for_question(best_match, knowledge_base)
                    print(Fore.GREEN + f"\nSimplybot: {answer}\n")
                else:
                    print(Fore.YELLOW + "\nSimplybot: I don’t know the answer to that one yet!")
                    new_answer = input(Fore.WHITE + "You can teach me! Type the answer or 'skip' to skip: ").strip()

                    if new_answer.lower() != 'skip' and new_answer:
                        knowledge_base["questions"].append({
                            "question": chat_input,
                            "answer": new_answer
                        })
                        chatbot.save_knowledge('knowledge_base.json', knowledge_base)
                        chatbot.save_to_backup('backup.json', knowledge_base)
                        print(Fore.GREEN + "Simplybot: Thank you! I’ve learned something new! 🤖\n")
                    else:
                        print(Fore.CYAN + "Simplybot: No worries! Maybe next time.\n")

                print(Fore.YELLOW + "=" * 50 + "\n")

            
# Basic Math calculations
        elif inputChoice == 'math':

            try:
                operationChosen: str = input('Choose Operator (add, subtract, divide, multiply): ')
            
                if operationChosen in operations:
                    calculation.calculate(operationChosen)
                else:
                    print("\nSimplybot: Invalid operator chosen.")
                    
            except AttributeError:
                print("Module Error: Did not satisfy module logic")
            except Exception as e:
                print(f"Unexpected Error: {e}")
# Gives you a random fact
        elif inputChoice == 'randf':
            try:
                fetchFromApi = randf.fetch_random_fact()
                print("\n" + "="*40 + "\n")
                print(f'Your random fact for today: {fetchFromApi}')
                print("\n" + "="*40 + "\n")
            except Exception as e:
                print("\n" + "="*40 + "\n")
                print(f'Unexpected error: {e}')
                print("\n" + "="*40 + "\n")
# Input the location, fetch current weather
        elif inputChoice == 'showweather':
            try:
                while True:
                    inputCity: str = input('Enter Location: ')
                    fetchFromWeather = weather.fetch_weather_by_location(inputCity)

                    if "temperature" in fetchFromWeather:
                        print("\n" + "="*40)
                        print(f"   🌍  Weather Report for {inputCity.title()} ")
                        print("="*40)
                        print(f"🌡️  Temperature : {fetchFromWeather['temperature']}")
                        print(f"💨  Wind        : {fetchFromWeather['wind']}")
                        print(f"📝  Description : {fetchFromWeather['description']}")
                        print("="*40 + "\n")

                        break
                    else:
                        print("\n" + "="*40 + "\n")
                        print("\nSimplybot: Couldn't fetch weather. Try another location.\n")
                        print("\n" + "="*40 + "\n")


            except AttributeError:
                print("Module Error: Did not satisfy module logic")
            except Exception as e:
                print(f"Unexpected Error: {e}")
# Exits the program
        elif inputChoice == 'exit':
            print("\n" + "="*40)
            print("\nSimplybot: Goodbye! Have a great day 🚀")
            print("\n" + "="*40)
            break

        else:
            print("\n" + "="*40)
            print("\nSimplybot: I don't understand your message! Please try again")
            print("\n" + "="*40)

main()