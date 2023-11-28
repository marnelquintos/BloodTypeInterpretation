# Blood Type Interpretation Application

import sys

# Welcome message
print("\n*** Welcome to the Blood Type Interpretation application! ***")
print("Based on your reactions, this application will give you an ABORh interpretation.")
print("Please input your reactions using a numerical value ranging from 0 to 4 (ex. 0, 1, 2, 3, 4)")
print("Type 'quit' to end the application at any time.\n")

# Assign variable for invalid result
invalid_result = "\nInvalid result.\nPlease try again using a numerical value ranging from 0 to 4 (ex. 0, 1, 2, 3, 4)" \
                 " or type 'quit' to end the application.\n"

quit_input = "\nYou have requested to quit the application. Feel free to run the application again at any time. " \
             "The application has now ended."

while True:

    # User input list
    user_input = []

    # User input reactions
    # Anti-A input
    while True:
        try:
            anti_a = input("Anti-A: ")
            if anti_a.lower() == "quit":
                print(quit_input)
                sys.exit()
            anti_a = int(anti_a)
            if anti_a < 0 or anti_a > 4:
                print(invalid_result)
                continue
            else:
                user_input.append(anti_a)
                break
        except ValueError:
            print(invalid_result)

    # Anti-B input
    while True:
        try:
            anti_b = input("Anti-B: ")
            if anti_b.lower() == 'quit':
                print(quit_input)
                sys.exit()
            anti_b = int(anti_b)
            if anti_b < 0 or anti_b > 4:
                print(invalid_result)
                continue
            else:
                user_input.append(anti_b)
                break
        except ValueError:
            print(invalid_result)

    # Anti-D input
    while True:
        try:
            anti_d = input("Anti-D: ")
            if anti_d.lower() == "quit":
                print(quit_input)
                sys.exit()
            anti_d = int(anti_d)
            if anti_d < 0 or anti_d > 4:
                print(invalid_result)
                continue
            else:
                user_input.append(anti_d)
                break
        except ValueError:
            print(invalid_result)

    # Anti-D Control input
    while True:
        try:
            anti_dc = input("Anti-D Control: ")
            if anti_dc.lower() == "quit":
                print(quit_input)
                sys.exit()
            anti_dc = int(anti_dc)
            if anti_dc < 0 or anti_dc > 4:
                print(invalid_result)
                continue
            else:
                user_input.append(anti_dc)
                break
        except ValueError:
            print(invalid_result)

    # A1 Cell input
    while True:
        try:
            a1_cell = input("A1 Cell: ")
            if a1_cell.lower() == "quit":
                print(quit_input)
                sys.exit()
            a1_cell = int(a1_cell)
            if a1_cell < 0 or a1_cell > 4:
                print(invalid_result)
                continue
            else:
                user_input.append(a1_cell)
                break
        except ValueError:
            print(invalid_result)

    # B Cell input
    while True:
        try:
            b_cell = input("B1 Cell: ")
            if b_cell.lower() == "quit":
                print(quit_input)
                sys.exit()
            b_cell = int(b_cell)
            if b_cell < 0 or b_cell > 4:
                print(invalid_result)
                continue
            else:
                user_input.append(b_cell)
                break
        except ValueError:
            print(invalid_result)

    # ABORh function that contains a dictionary
    def aborh(aborh_interp, user_input_reactions):
        aborh_to_reactions = {
            "AB Pos": [user_input_reactions[0] >= 1, user_input_reactions[1] >= 1, user_input_reactions[2] >= 1,
                       user_input_reactions[3] == 0, user_input_reactions[4] == 0, user_input_reactions[5] == 0],
            "AB Neg": [user_input_reactions[0] >= 1, user_input_reactions[1] >= 1, user_input_reactions[2] == 0,
                       user_input_reactions[3] == 0, user_input_reactions[4] == 0, user_input_reactions[5] == 0],
            "A Pos": [user_input_reactions[0] >= 1, user_input_reactions[1] == 0, user_input_reactions[2] >= 1,
                      user_input_reactions[3] == 0, user_input_reactions[4] == 0, user_input_reactions[5] >= 1],
            "A Neg": [user_input_reactions[0] >= 1, user_input_reactions[1] == 0, user_input_reactions[2] == 0,
                      user_input_reactions[3] == 0, user_input_reactions[4] == 0, user_input_reactions[5] >= 1],
            "B Pos": [user_input_reactions[0] == 0, user_input_reactions[1] >= 1, user_input_reactions[2] >= 1,
                      user_input_reactions[3] == 0, user_input_reactions[4] >= 1, user_input_reactions[5] == 0],
            "B Neg": [user_input_reactions[0] == 0, user_input_reactions[1] >= 1, user_input_reactions[2] == 0,
                      user_input_reactions[3] == 0, user_input_reactions[4] >= 1, user_input_reactions[5] == 0],
            "O Pos": [user_input_reactions[0] == 0, user_input_reactions[1] == 0, user_input_reactions[2] >= 1,
                      user_input_reactions[3] == 0, user_input_reactions[4] >= 1, user_input_reactions[5] >= 1],
            "O Neg": [user_input_reactions[0] == 0, user_input_reactions[1] == 0, user_input_reactions[2] == 0,
                      user_input_reactions[3] == 0, user_input_reactions[4] >= 1, user_input_reactions[5] >= 1]
        }
        # Loop through the dictionary to identify the key based on the values
        for interpretation in aborh_interp:
            if interpretation in aborh_to_reactions and all(aborh_to_reactions[interpretation]):
                return interpretation
        return "INVALID\nInterpretation could not be determined. Please check for ABO discrepancy and/or " \
               "validity of Anti-D control.\n"


    # List of ABORh types
    aborh_interpretations = ["AB Pos", "AB Neg", "A Pos", "A Neg", "B Pos", "B Neg", "O Pos", "O Neg"]

    # Print ABORh interpretation using the aborh function
    print("\nABORh interpretation: ", aborh(aborh_interpretations, user_input))
