Employee_Name = input("Enter Employee Name: ")  # using string datatype           
Employee_ID = int(input("Enter Employee ID: ")) # using integer datatype            
Company_Name = input("Enter Company Name: ")    # using string datatype            
Department = input("Enter Department: ")    # using string datatype                
Designation = input("Enter Designation: ")   # using string datatype               
Monthly_Salary = float(input("Enter Monthly Salary: "))     # using float datatype
Years_Of_Experience = float(input("Enter Years of Experience: "))   # using float datatype
Work_Location = input("Enter Work Location: ")  # using string datatype     
Status_Input = input("Is Employee Active? (True/False): ") # using string datatype     
Employee_Active_Status = Status_Input == "True" # using string datatype     
Yearly_Salary = Monthly_Salary * 12 # converting string to boolean
# now displaying employee details card
print("\n")
print("=========== EMPLOYEE DETAILS CARD ==================")
print("\n")
print(f"Employee Name          : {Employee_Name}")
print(f"Employee ID            : {Employee_ID}")
print(f"Company Name           : {Company_Name}")
print(f"Department             : {Department}")
print(f"Designation            : {Designation}")
print(f"Monthly Salary         : ₹{Monthly_Salary}")
print(f"Yearly Salary          : ₹{Yearly_Salary}")
print(f"Years of Experience    : {Years_Of_Experience}")
print(f"Work Location          : {Work_Location}")
print(f"Employee Active Status : {Employee_Active_Status}")
# now displaying data types 
print("\n")
print("========== DATA TYPES ==========")
print("\n")
print("employee_name          :", type(Employee_Name))
print("employee_id            :", type(Employee_ID))
print("company_name           :", type(Company_Name))
print("department             :", type(Department))
print("designation            :", type(Designation))
print("monthly_salary         :", type(Monthly_Salary))
print("yearly_salary          :", type(Yearly_Salary))
print("years_of_experience    :", type(Years_Of_Experience))
print("work_location          :", type(Work_Location))
print("employee_active_status :", type(Employee_Active_Status))