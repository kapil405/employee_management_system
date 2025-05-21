from employee import Employee
import  utils

def display_menu():
    print('\n-------Employee Management-------')
    print('1. View all employees')
    print('2. Add new employee')
    print('3. Update employee')
    print('4. Delete employee')
    print('5. Exit')

def view_employees():
    data = utils.load_employees()
    if not data:
        print('No employees found.')
        return 

    print('\n--- Employee List ---')
    for emp in data:
        print(f'ID: {emp['id']}, Name: {emp['name']}, Role: {emp['role']}')

def add_employee():
    name = input('Enter name: ')
    role = input('Enter role: ')
    emp = Employee(name,role)
    data = utils.load_employees()
    data.append(emp.to_dict())
    utils.save_employee(data)
    print("✅ Employee addedd!")

def Update_employee():
    emp_id = input('Enter employee ID to update: ')
    data = utils.load_employees()

    for emp in data:
        if emp['id'] == emp_id:
            new_name = input(f'Enter new name (current : {emp['name']}) : ')
            new_role = input(f'Enter new roile (curent: {emp['role']}) : ')
            emp['name'] = new_name
            emp['role'] = new_role
            utils.save_employee(data)
            print("✅ Employee updated!")
            return

        print("❌ Employee not found.")

def delete_employee():
    emp_id = input('Enter employee ID to delete: ')
    data = utils.load_employees()
    new_data = [emp for emp in data if emp['id'] != emp_id]

    if len(data) == len(new_data):
        print("❌ Employee not found.")
    else:
        utils.save_employee(new_data)
        print("🗑️ Employee deleted.")


def main():
    while True:
        display_menu()
        choiche = input('Choose an option (1-5): ')
        
        if choiche == '1':
            view_employees()
        elif choiche == '2':
            add_employee()
        elif choiche == '3':
            Update_employee()
        elif choiche == '4':
            delete_employee()
        elif choiche == '5':
           print("👋 Goodbye!")
           break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()