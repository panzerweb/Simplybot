# This will be my first python project
# A simple chatbot
# This will have very simple features
# But sooner, I intend to update with actual AI integration

# Custom modules
from modules import calculation
from modules import randf
from modules import weather
import menu

# Predefined modules
from typing import List

# Variables needed
operations: List[str] = ["add", "subtract", "divide", "multiply"]
    
# Main function
def main():
    while True:
        
        # Opening
        menu.show_menu()

        inputChoice: str = input('Enter command: ').lower()
# Ignores "Enter" keypress to execute else statement
        if not inputChoice.strip():
            continue
# Simple greet
        if inputChoice == 'greet':
            print("\n" + "="*40 + "\n")
            print("\nSimplybot: Hello there! I am Simplybot, a simple chatbot developed to do simple things. How may I help you?")
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