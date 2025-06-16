import sqlite3

# Connect to DB or create if it doesn't exist
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        emp_id TEXT UNIQUE NOT NULL,
        department TEXT,
        salary REAL
    )
''')
conn.commit()

# Add employee
def add_employee():
    name = input("Enter name: ")
    emp_id = input("Enter Employee ID: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))
    try:
        cursor.execute("INSERT INTO employees (name, emp_id, department, salary) VALUES (?, ?, ?, ?)",
                       (name, emp_id, department, salary))
        conn.commit()
        print("✅ Employee added!")
    except sqlite3.IntegrityError:
        print("❌ Employee ID must be unique.")

# View all employees
def view_employees():
    cursor.execute("SELECT * FROM employees")
    for emp in cursor.fetchall():
        print(emp)

# Search employee
def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    cursor.execute("SELECT * FROM employees WHERE emp_id=?", (emp_id,))
    emp = cursor.fetchone()
    if emp:
        print("👀 Found:", emp)
    else:
        print("❌ No such employee.")

# Update salary
def update_salary():
    emp_id = input("Enter Employee ID: ")
    new_salary = float(input("Enter new salary: "))
    cursor.execute("UPDATE employees SET salary=? WHERE emp_id=?", (new_salary, emp_id))
    conn.commit()
    print("💰 Salary updated.")

# Delete employee
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    cursor.execute("DELETE FROM employees WHERE emp_id=?", (emp_id,))
    conn.commit()
    print("🗑️ Employee deleted.")

# Main loop
while True:
    print("\n=== Employee Manager ===")
    print("1. Add Employee")
    print("2. View All")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")
    choice = input("Choose an option (1–6): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        update_salary()
    elif choice == '5':
        delete_employee()
    elif choice == '6':
        print("👋 Exiting...")
        break
    else:
        print("❗ Invalid choice.")
