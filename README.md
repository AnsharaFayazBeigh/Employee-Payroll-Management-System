# Employee Payroll Management System
## Overview
The Employee Payroll Management System is a Python-based desktop application designed to manage employee payroll efficiently. It allows organizations to track employee details, calculate salaries, and generate payslips.

## Features
Login System: Secure user authentication before accessing the system.
Add Employee Details: Input employee designation, name, date of joining (D.O.J), and salary information.
Salary Calculator: Calculate final salaries after deductions (e.g., GP fund, taxes).
Employee Search: Quickly retrieve employee records by ID.
Scrollable Employee Records: Navigate through extensive employee data with a vertical scrollbar.
Payslip Generation: Automatically generate payslips for employees.
Print Salary Slip: Print payslips directly from the application.
## Technologies Used
Python 3.x
Tkinter for GUI
pymysql for database connectivity
SQLite3/MySQL (optional for database management)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/employee-payroll-management.git
Install required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application: Start with the login module:

bash
Copy code
python login.py
After successful login, open the main application:

bash
Copy code
python main.py
Usage
Login: Access the system using your credentials.
Manage Employee Information: Add, update, or delete employee details.
Calculate Salary: Use the built-in calculator to compute final salaries.
Search for Employees: Enter employee ID to retrieve details.
Generate Payslips: Automatically create and print payslips for employees.
Sample Payslip Format
yaml
Copy code
------------------------------------------------
Employee ID           :  [ID]
Salary Of             :  MON-YYYY
Generated on          :  DD-MM-YYYY
-------------------------------------------------
Total Days            :  DD
Total Present         :  DD
Total Absent          :  DD
Basic Salary          :  Rs. ----
Medical               :  Rs. ----
PF                    :  Rs. ----
Conveyance            :  Rs. ----
Net Salary            :  Rs. -----
-------------------------------------------------

## Contribution
Contributions are welcome! You can enhance the system by adding new features or improving existing functionalities. Please fork the repository and submit a pull request.

