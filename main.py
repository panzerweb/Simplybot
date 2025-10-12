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

# Variables needed
operations: List[str] = ["add", "subtract", "divide", "multiply"]
    
# Main function
def main():
    
    # Fetch the JSON file for all knowledge as a dictionary
    knowledge_base = chatbot.load_knowledge('knowledge_base.json')

    # Run program
    while True:
        
        # Opening
        menu.show_menu()

        # First user input
        inputChoice: str = input('Enter command: ').lower()

# Ignores "Enter" keypress to execute else statement
        if not inputChoice.strip():
            continue
# Chatbot implementation
        if inputChoice == 'chat':
            print("\n" + "="*40 + "\n")
            
            while True:
                chat_input: str = input("You: ")

                if chat_input.lower() == 'quit':
                    break

                # Find closely related question from the Dictionary to a List
                best_match = chatbot.find_best_match(chat_input, [question["question"] for question in knowledge_base["questions"]])

                if best_match:
                    answer: str = chatbot.get_answer_for_question(best_match, knowledge_base)
                    print(f'Simplybot: {answer}')
                else:
                    print(f'Simplybot: I do now know the answer for that one! You can train me by adding me a new knowledge.')
                    new_answer: str = input("Type the answer or 'skip' to skip: ")

                    if new_answer.lower() != 'skip':
                        knowledge_base["questions"].append({"question": chat_input, "answer": new_answer})
                        chatbot.save_knowledge('knowledge_base.json', knowledge_base)
                        print(f'Thank you for this knowledge!')
                    else:
                        break
            
            print("\n" + "="*40 + "\n")
            
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