# This will be my first python project
# A simple chatbot
# This will have very simple features
# But sooner, I intend to update with actual AI integration

# Custom modules
from modules import calculation
from modules import randf

# Predefined modules
from typing import List

# Variables needed
operations: List[str] = ["add", "subtract", "divide", "multiply"]


# Opening
print(f'Hello there! I am Simplybot, a simple chatbot developed by Panzerweb. How may I help you?\n')

print('There are several capabilities Simplybot can do, type:')
print('greet -> for Simplybot to greet you back')
print('math -> to allow for basic calculations')
print('randf -> to return a random fact')
print('exit -> to exit chatbot\n')
    
# Main function
def main():
    while True:
        inputChoice: str = input('What are you gonna do? ').lower()

        if inputChoice == 'greet':
            print("\nSimplybot: Hello there")

        elif inputChoice == 'math':

            try:
                operationChosen: str = input('Choose Operator: ')
            
                if operationChosen in operations:
                    calculation.calculate(operationChosen)
                else:
                    print("\nSimplybot: Invalid operator chosen.")
                    
            except AttributeError:
                print("Module Error: Did not satisfy module logic")
            except Exception as e:
                print(f"Unexpected Error: {e}")
        
        elif inputChoice == 'randf':
            fetchFromApi = randf.fetch_random_fact()
            print(f'Your random fact for today: {fetchFromApi}')

        elif inputChoice == 'exit':
            break

        else:
            print("\nSimplybot: I don't understand your message! Please try again")


main()