disease_symptoms = {
    "Malaria": ["Fever", "Chills", "Sweating", "Headache", "Muscle pain"],
    "Typhoid": ["Fever", "Headache", "Abdominal pain", "diarrhea", "Rash"],
    "Dengue": ["Fever", "Headache", "Joint pain", "Muscle pain", "Rash"],
    "Chickenpox": ["Rash", "Fever", "Fatigue", "Headache", "Loss of appetite"],
    "Measles": ["Fever", "Cough", "Runny nose", "Red, watery eyes", "Rash"],
}

def input_symptom():
    print("Give your symptoms according to the following list (separate by commas):")
    print("Fever, Chills, Sweating, Headache, Muscle pain, \nAbdominal pain, diarrhea, Rash, Joint pain, \nFatigue, Loss of appetite, Cough, Runny nose, Red, watery eyes")
    user_input = input("Enter your symptoms (comma-separated): ").lower()
    symp = [s.strip() for s in user_input.split(',')]
    return symp

def diagnose(user_symptoms):
    possible_diseases = {}
    for disease, symptoms in disease_symptoms.items():
        match_count = 0
        for symptom in user_symptoms:
            if symptom in [s.lower() for s in symptoms]:
                match_count += 1
        if match_count > 0:
            possible_diseases[disease] = match_count
            
  
    if not possible_diseases:
        print("No matching diseases found.")
        return

    sorted_diseases = sorted(possible_diseases.items(), key=lambda item: item[1], reverse=True)

    print("\n diagnoses is :")
    for disease, match_count in sorted_diseases:
        print("-", disease , "matched ",match_count,"symptoms")
        
    print("\n  Consult to the Doctor")
def main():
    user_symptoms = input_symptom()
    diagnose(user_symptoms)

if _name_ == "_main_":
    main()
