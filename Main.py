# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# DAlexandrov,12.08.2019,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
    import DataClasses, ProcessingClasses, IOClasses # Will error if the modules are not found
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #

file_name = "EmployeeData.txt" # file_name to import from/export to

# Load data from file into a list of employee objects when script starts
try:
    lstEmpObj = ProcessingClasses.FileProcessor.read_data_from_file(file_name)
except FileNotFoundError as E:
    print("Cannot find the file!")

while(True):
    # Show user a menu of options
    IOClasses.EmployeeIO.print_menu_items()

    # Get user's menu option choice
    userChoice = IOClasses.EmployeeIO.input_menu_options()

    # Show user current data in the list of employee objects
    if(userChoice == "1"):
        list_of_emp = []
        for line in lstEmpObj:
            list_of_emp.append(DataClasses.Employee(line[0], line[1], line[2].strip()))
        IOClasses.EmployeeIO.print_current_list_items(list_of_emp)
        continue
    # Let user add data to the list of employee objects
    elif(userChoice == "2"):
        newEmp = IOClasses.EmployeeIO.input_employee_data()
        list_of_emp.append(newEmp)
        IOClasses.EmployeeIO.print_current_list_items(list_of_emp)
        continue
    # let user save current data to file
    elif(userChoice == "3"):
        ProcessingClasses.FileProcessor.save_data_to_file(file_name, list_of_emp)
        print("Data saved!")
        continue
    # Let user exit program
    elif(userChoice == "4"):
        print("Good-bye...")
        break
    else:
        raise Exception("Input was outside of menu options... please try again!")
# Main Body of Script  ---------------------------------------------------- #
