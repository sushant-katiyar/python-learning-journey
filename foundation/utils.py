# utils.py
def get_grade(cgpa):
    if cgpa >= 9:
        return "Outstanding"
    elif cgpa >= 8:
        return "Excellent"
    else:
        return "Good"

def format_name(name):
    return name.strip().title()

def is_passing(cgpa):
    if cgpa >= 5:
        return True
    else:
        return False

def scholarship(cgpa):
    return cgpa >= 9