# ------------------------------------------------- #
# Title: Test Harness
# Description: A module of data classes
# ChangeLog: (Who, When, What)
# DAlexandrov,12.8.2019,Created copy for Assignment09
# ------------------------------------------------- #
'''
# Person Class Test

if __name__ == "__main__":
    import DataClasses as DP  # data classes
    import ProcessingClasses as PC  # processing classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = DP.Person("Bob", "Smith")
objP2 = DP.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
PC.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
lstFileData = PC.FileProcessor.read_data_from_file("PersonData.txt")
for row in lstFileData:
    p = DP.Person(row[0], row[1])
    print(p.to_string().strip(), type(p))
'''

'''
# Employee/File Processor Test 

if __name__ == "__main__":
    from DataClasses import Employee as Emp  # Employee class only!
    import ProcessingClasses as PC  # processing classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
PC.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = PC.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))
    
'''

#'''
# IO Test 

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())

#'''



