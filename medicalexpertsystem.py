# Medical expert system

# Define the rules for diagnosing diseases
rules = {
    'common_cold': {
        'symptoms': ['sneezing', 'cough', 'runny_nose'],
        'diagnosis': 'You may have a common cold.'
    },
    'flu': {
        'symptoms': ['fever', 'headache', 'muscle_pain'],
        'diagnosis': 'You may have the flu.'
    },
    'allergies': {
        'symptoms': ['itchy_eyes', 'sneezing', 'rash'],
        'diagnosis': 'You may have allergies.'
    },
    'migraine': {
        'symptoms': ['headache', 'nausea', 'sensitivity_to_light'],
        'diagnosis': 'You may have a migraine.'
    },
    'food_poisoning': {
        'symptoms': ['nausea', 'vomiting', 'diarrhea'],
        'diagnosis': 'You may have food poisoning.'
    },
    'no_disease': {
        'symptoms': [],
        'diagnosis': 'No specific disease could be diagnosed based on the given symptoms.'
    }
}


def diagnose_disease(symptoms):
    # Iterate over the rules and check if the symptoms match
    for disease, rule in rules.items():
        if set(symptoms) == set(rule['symptoms']):
            return rule['diagnosis']
    
    # If no match is found, return the default diagnosis
    return rules['no_disease']['diagnosis']


# Example usage
user_symptoms = ['sneezing', 'cough', 'runny_nose']
diagnosis = diagnose_disease(user_symptoms)
print(diagnosis)


#Footer
print("Question no.5")
print("Name: Sarovar Bhandari ")
print("Roll no : 15 ")
print("Section:A")
