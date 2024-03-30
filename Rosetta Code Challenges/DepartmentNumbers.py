# Department Numbers
def generate_department_combinations():
    combinations = []
    for police in range(2, 8, 2):
        for sanitation in range(1, 8):
            for fire in range(1, 8):
                if police != sanitation and police != fire and sanitation != fire and police + sanitation + fire == 12:
                    combinations.append([police, sanitation, fire])
    return combinations
valid_combinations = generate_department_combinations()
for combination in valid_combinations:
    print(combination)