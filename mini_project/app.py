import json

def calculate_bmi(weight, height):
    """Calculate BMI based on weight and height."""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def calculate_caloric_needs(weight, height, age, gender, activity_level):
    """Calculate daily caloric needs based on BMR and activity level."""
    # BMR calculation using the Mifflin-St Jeor Equation
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5
    else:  # female
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age - 161

    # Adjust BMR based on activity level
    activity_multipliers = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725
    }
    
    caloric_needs = bmr * activity_multipliers.get(activity_level.lower(), 1.2)
    return round(caloric_needs, 2)

def main(weight, height, age, gender, activity_level):
    """Calculate BMI and caloric needs and return as JSON-compatible output."""
    bmi = calculate_bmi(weight, height)
    caloric_needs = calculate_caloric_needs(weight, height, age, gender, activity_level)
    result = {
        'BMI': bmi,
        'Caloric Needs': caloric_needs
    }
    return json.dumps(result)  # Convert to JSON string for UiPath compatibility

# Example standalone test (remove in production)
if __name__ == "__main__":
    # Test with example parameters
    weight = 70  # in kg
    height = 1.75  # in meters
    age = 25
    gender = 'male'
    activity_level = 'moderately active'

    result = main(weight, height, age, gender, activity_level)
    print(result)  # Debug output
