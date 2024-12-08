with open("lab.txt", "r") as file:
    data = file.readlines()

def process_student_data(data):
    # Extract and clean lines
    name_line = data[0].strip()
    age_line = data[1].strip()
    grade_line = data[2].strip()
    
    # Convert Age to Buddhist Era
    age = int(age_line.split(": ")[1])
    christYear = 2024 - age
    year_buddhist = christYear + 543
    
    # Convert Grade to Ranking Table
    grade = grade_line.split(": ")[1]
    if grade == "A":
        rank = "High Distinction"
    elif grade in ["B+", "B"]:
        rank = "Distinction"
    elif grade in ["C+", "C"]:
        rank = "Good"
    elif grade in ["D+", "D"]:
        rank = "Normal"
    elif grade == "F":
        rank = "Failed"
    else:
        rank = "Unknown"

    # Return processed information
    return {
        "name": name_line,
        "buddhist_era": year_buddhist,
        "rank": rank
    }
