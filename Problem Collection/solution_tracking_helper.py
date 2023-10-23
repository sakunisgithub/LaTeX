import pandas as pd

def print_all_topics() :
    print("1. Logarithm")
    print("2. Geometry")
    print("3. Miscellaneous")
    print("4. Factorization")
    print("5. Construction")
    print("6. Indices")
    print("7. Trigonometry")
    print("8. Functional Equations")
    print("9. System of Equations")
    print("10. Coordinate Geometry")
    print("11. Mensuration")
    print("12. Inequality")
    print("13. Number Theory")

def add_inputs() :
    problem_no = int(input("Enter problem no = "))
    copy_no = int(input("Enter copy no = "))
    page_no = int(input("Enter page no = "))
    temp = (problem_no, copy_no, page_no)
    return(temp)

def operate_csv(c1, topic, inputs) :
    if topic == 1 :
        logarithm = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\logarithm.csv") 
        if c1 == 1 :
            logarithm.loc[len(logarithm)] = [inputs[0], inputs[1], inputs[2]]
            logarithm.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\logarithm.csv", index=False) 
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(logarithm.iloc[inputs-1])
    elif topic == 2 :
        geometry = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\geometry.csv")
        if c1 == 1 :
            geometry.loc[len(geometry)] = [inputs[0], inputs[1], inputs[2]]
            geometry.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\geometry.csv", index=False)
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(geometry.iloc[inputs-1])
    elif topic == 3 :
        miscellaneous = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\miscellaneous.csv")
        if c1 == 1 :
            miscellaneous.loc[len(miscellaneous)] = [inputs[0], inputs[1], inputs[2]]
            miscellaneous.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\miscellaneous.csv", index=False)
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(miscellaneous.iloc[inputs-1])
    elif topic == 4 :
        factorization = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\factorization.csv")
        if c1 == 1 :
            factorization.loc[len(factorization)] = [inputs[0], inputs[1], inputs[2]]
            factorization.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\factorization.csv", index=False)
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(factorization.iloc[inputs-1])
    elif topic == 5 :
        construction = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\construction.csv")
        if c1 == 1 :
            construction.loc[len(construction)] = [inputs[0], inputs[1], inputs[2]]
            construction.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\construction.csv", index=False)
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(construction.iloc[inputs-1])
    elif topic == 6 :
        indices = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\indices.csv")
        if c1 == 1 :
            indices.loc[len(indices)] = [inputs[0], inputs[1], inputs[2]]
            indices.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\indices.csv", index=False)
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(indices.iloc[inputs-1])
    elif topic == 7 :
        trigonometry = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\trigonometry.csv")
        if c1 == 1 :
            trigonometry.loc[len(trigonometry)] = [inputs[0], inputs[1], inputs[2]]
            trigonometry.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\trigonometry.csv", index=False)
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(trigonometry.iloc[inputs-1])
    elif topic == 8 :
        functional_equations = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\functional_equations.csv")
        if c1 == 1 :
            functional_equations.loc[len(functional_equations)] = [inputs[0], inputs[1], inputs[2]]
            functional_equations.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\functional_equations.csv", index=False)
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(functional_equations.iloc[inputs-1])
    elif topic == 9 :
        system_of_equations = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\system_of_equations.csv")
        if c1 == 1 :
            system_of_equations.loc[len(system_of_equations)] = [inputs[0], inputs[1], inputs[2]]
            system_of_equations.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\system_of_equations.csv", index=False)
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(system_of_equations.iloc[inputs-1])
    elif topic == 10 :
        coordinate_geometry = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\coordinate_geometry.csv")
        if c1 == 1 :
            coordinate_geometry.loc[len(coordinate_geometry)] = [inputs[0], inputs[1], inputs[2]]
            coordinate_geometry.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\coordinate_geometry.csv", index=False)
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(coordinate_geometry.iloc[inputs-1])
    elif topic == 11 :
        mensuration = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\mensuration.csv")
        if c1 == 1 :
            mensuration.loc[len(mensuration)] = [inputs[0], inputs[1], inputs[2]]
            mensuration.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\mensuration.csv", index=False)
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(mensuration.iloc[inputs-1])
    elif topic == 12 :
        inequality = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\inequality.csv") 
        if c1 == 1 :
            inequality.loc[len(inequality)] = [inputs[0], inputs[1], inputs[2]]
            inequality.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\inequality.csv", index=False) 
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(inequality.iloc[inputs-1])
    elif topic == 13 :
        number_theory = pd.read_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\number_theory.csv") 
        if c1 == 1 :
            number_theory.loc[len(number_theory)] = [inputs[0], inputs[1], inputs[2]]
            number_theory.to_csv("C:\\Users\\Ananda\\OneDrive\\Documents\\solution_tracker_for_problem_collection\\number_theory.csv", index=False) 
            print("\n\nDeatils added successfully !\n\n")
        elif c1 == 2 :
            print(number_theory.iloc[inputs-1])
    

print("\n\n-----MENU-----\n\n")
print("1. Add details of a problem")
print("2. Fetch details of a problem")

choice_1 = int(input("Enter your choice = "))

if choice_1 == 1 :
    print("\n\n-----TOPICS-----\n\n")
    print_all_topics()

    choice_2 = int(input("Enter the topic of the problem = "))

    my_inputs = add_inputs()

    operate_csv(choice_1, choice_2, my_inputs)
elif choice_1 == 2 :
    print("\n\n-----TOPICS-----\n\n")
    print_all_topics()

    choice_2 = int(input("Enter the topic of the problem = "))

    my_inputs = int(input("Enter the problem no = "))

    operate_csv(choice_1, choice_2, my_inputs)