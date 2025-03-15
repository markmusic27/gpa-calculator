import json
import time
import os
import calculator

# Dictionary mapping command IDs to their descriptions for user selection
commands = {
        "calc_tot": {
            "name": "Calculate total GPA",
            "fn": calculator.calculate_gpa
            },
        "calc_qtr": {
            "name": "Calculate GPA for a specific quarter",
            "fn": calculator.calculate_quarter_gpa
            },
        "calc_yr": {
            "name": "Calculate GPA for a specific year",
            "fn": calculator.calculate_year_gpa
            },
        "exit": "Exit"
    }

# Gives user context to what they can do with the program
def welcome():
    # Clear the screen (works for both Windows and Unix-based systems)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\033[1mSelect a command:\033[0m")
    
    count = 0
    # Dictionary mapping command IDs to their descriptions for user selection
    for id in commands:
        count += 1
        # Check if the command value is a dictionary (has a name field) or just a string
        description = commands[id]["name"] if isinstance(commands[id], dict) else commands[id]
        print(f"\033[1m{count}\033[0m: {description}")


# Gets and validates user command input, returning the corresponding command ID
def get_command():
    user_input = input("\n\033[1mEnter a command: \033[0m")
    
    # Validate input is a number between 1 and count
    try:
        command_num = int(user_input)
        if 1 <= command_num <= len(commands.keys()):
            # Convert number to corresponding command ID
            return list(commands.keys())[command_num - 1]
        return try_again()
    except ValueError:
        return try_again()
    
def try_again():
    print("Invalid command. Please try again.")
    return get_command()
    


def main():
    grade_map_file = open('grade_map.json')
    map = json.load(grade_map_file)
    
    welcome()
    command = get_command()
    
    if command == "err":
        print("Invalid command. Please try again.")
        return
    
    if command == "exit":
        return
    
    # Call the function corresponding to the selected command
    commands[command]["fn"](map)
    
    
if __name__ == "__main__":
  main()