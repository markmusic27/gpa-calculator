# Helper functions
import os
import json


# Returns list of .json files in grades directory
def get_grade_files():
    import os
    
    grades_dir = "grades"
    try:
        files = os.listdir(grades_dir)
        grade_files = [f for f in files if f.endswith('.json')]  # Assuming files are .txt
        return grade_files
    except FileNotFoundError:
        return []
    
# Reads and returns the contents of a grade file
def read_grade_file(file):
    file_path = os.path.join("grades", file)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file} not found.")
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"Error reading {file}: Invalid JSON format", "", 0)
    except Exception as e:
        raise Exception(f"Error processing {file}: {str(e)}")
    
# Calculates GPA for a specific academic year
def calc_gpa_per_year(grade_map, year):
    total_gpa = 0
    total_units = 0
    
    for quarter in year:
        result = calc_gpa_per_quarter(grade_map, year[quarter])
        total_gpa += result["numerator"]
        total_units += result["denominator"]
        
    return {"numerator": total_gpa, "denominator": total_units, "gpa": total_gpa / total_units if total_units > 0 else 0}
        
# Calculates GPA for a specific academic quarter
def calc_gpa_per_quarter(grade_map, quarter):
    sum = 0
    sum_units = 0
    for course in quarter:
        grade = grade_map[quarter[course]["grade"]]
        units = quarter[course]["units"]
        
        # Validate grade and units are present and of correct type
        if not isinstance(grade, (int, float)):
            raise TypeError(f"Invalid grade value for {course}: {grade}")
        if not isinstance(units, (int, float)):
            raise TypeError(f"Invalid units value for {course}: {units}")
        
        sum_units += units
        sum += grade * units
        
    return {"denominator": sum_units, "numerator": sum, "gpa": sum / sum_units if sum_units > 0 else 0}

def get_letter_grade(gpa, grade_map):
    # Sort the grade_map by GPA values in descending order
    sorted_grades = sorted(grade_map.items(), key=lambda x: x[1], reverse=True)
    
    for letter, grade_value in sorted_grades:
        if gpa >= grade_value:
            return letter
    return "F"  # Default to "F" if no other grade matches

def calculate_gpa(grade_map):
    files = get_grade_files()
    
    if len(files) == 0:
        print("No grade files found.")
        return 0
    
    total_gpa = 0
    total_units = 0
    
    for file in files:
        year_data = read_grade_file(file)
        
        # Calculate GPA for each year and accumulate
        result = calc_gpa_per_year(grade_map, year_data)
        total_gpa += result["numerator"]
        total_units += result["denominator"]
        
    gpa = total_gpa / total_units if total_units > 0 else 0
    
    letter_grade = get_letter_grade(gpa, grade_map)
    
    print()
    print(f"Your GPA is \033[1m{gpa:.2f}\033[0m which is an average \033[1m{letter_grade}\033[0m")
    

# Calculates GPA for a specific academic quarter
def select_quarter(year_data):
    quarters = list(year_data.keys())
    for i, quarter in enumerate(quarters, 1):
        # Capitalize the quarter name
        print(f"\033[1m{i}\033[0m: {quarter.capitalize()}")
    
    while True:
        try:
            choice = int(input("\n\033[1mEnter the number of the quarter: \033[0m"))
            if 1 <= choice <= len(quarters):
                return quarters[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def select_year(years):
    # Sort the years alphabetically
    sorted_years = sorted(years)
    
    for i, year in enumerate(sorted_years, 1):
        # Remove the file extension and capitalize the first letter
        display_year = year.replace('.json', '').capitalize()
        print(f"\033[1m{i}\033[0m: {display_year}")
    
    while True:
        try:
            choice = int(input("\n\033[1mEnter year: \033[0m"))
            if 1 <= choice <= len(sorted_years):
                return sorted_years[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_quarter_gpa(grade_map):
    print()
    print("In which year did you take the quarter?")
    files = get_grade_files()
    
    if len(files) == 0:
        print("No grade files found.")
        return 0
    
    year = select_year(files);
    year_data = read_grade_file(year)
    
    quarter = select_quarter(year_data)
    
    gpa = calc_gpa_per_quarter(grade_map, year_data[quarter])["gpa"]
    letter_grade = get_letter_grade(gpa, grade_map)
    
    print()
    print(f"Your GPA for your {year.replace('.json', '')} {quarter} is \033[1m{gpa:.2f}\033[0m which is an average \033[1m{letter_grade}\033[0m")
    

# Calculates GPA for a specific academic year
def calculate_year_gpa(grade_map):
    print()
    files = get_grade_files()
    
    if len(files) == 0:
        print("No grade files found.")
        return 0
    
    year = select_year(files);
    year_data = read_grade_file(year)
    
    gpa = calc_gpa_per_year(grade_map, year_data)["gpa"]
    
    letter_grade = get_letter_grade(gpa, grade_map)
    
    print()
    print(f"Your GPA for your {year.replace('.json', '')} year is \033[1m{gpa:.2f}\033[0m which is an average \033[1m{letter_grade}\033[0m")



