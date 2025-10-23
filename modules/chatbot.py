import json
from difflib import get_close_matches

# Loads the data from the JSON file
# Returns the data from the JSON file
def load_knowledge(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

# Save new knowledge to the JSON file
# Use for training the chatbot, saving the new knowledge you input
def save_knowledge(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Dumps knowledge into backup file
def save_to_backup(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Find best match
# Uses the get_close_matches() to find the best question in the questions dictionary
# that is assumed from the JSON file
# n=1 defines the best match only for 60% accuracy
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

# Get answer for question from the knowledge_base acquired from the file
# Assume that we have extracted the JSON file already with load_knowledge()
def get_answer_for_question(best_match: str, knowledge_base: dict) -> str | None:
    for item in knowledge_base["questions"]:
        if item["question"] == best_match:
            return item["answer"]