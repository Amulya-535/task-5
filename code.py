employee_name = input("Enter Employee Name: ")  # using string datatype           
employee_id = int(input("Enter Employee ID: ")) # using integer datatype            
company_name = input("Enter Company Name: ")    # using string datatype            
department = input("Enter Department: ")    # using string datatype                
designation = input("Enter Designation: ")   # using string datatype               
monthly_salary = float(input("Enter Monthly Salary: "))     # using float datatype
years_of_experience = float(input("Enter Years of Experience: "))   # using float datatype
work_location = input("Enter Work Location: ")  # using string datatype     
status_input = input("Is Employee Active? (True/False): ") # using string datatype     
employee_active_status = status_input == "True" # using string datatype     
yearly_salary = monthly_salary * 12 # converting string to boolean
# now displaying employee details card
print("\n")
print("=========== EMPLOYEE DETAILS CARD ==================")
print("\n")
print(f"Employee Name          : {employee_name}")
print(f"Employee ID            : {employee_id}")
print(f"Company Name           : {company_nameompany_Name}")
print(f"Department             : {department}")
print(f"Designation            : {designation}")
print(f"Monthly Salary         : ₹{monthly_salary}")
print(f"Yearly Salary          : ₹{yearly_salary}")
print(f"Years of Experience    : {years_of_experience}")
print(f"Work Location          : {work_location}")
print(f"Employee Active Status : {employee_active_status}")
# now displaying data types 
print("\n")
print("========== DATA TYPES ==========")
print("\n")
print("employee_name          :", type(employee_name))
print("employee_id            :", type(employee_id))
print("company_name           :", type(company_name))
print("department             :", type(department))
print("designation            :", type(designation))
print("monthly_salary         :", type(monthly_salary))
print("yearly_salary          :", type(yearly_salary))
print("years_of_experience    :", type(years_of_experience))
print("work_location          :", type(work_location))
print("employee_active_status :", type(employee_active_status))