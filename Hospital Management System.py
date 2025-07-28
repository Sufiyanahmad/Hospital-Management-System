# Hospital Management System
# Author: ChatGPT | Single Python File CLI Version

import datetime

# Data Storage
patients = []
medicines = []
doctors = []
staffs = []

# Utility Functions
def generate_id(entity_list, prefix):
    return f"{prefix}{len(entity_list)+1:03d}"

def input_date(prompt="Enter date (YYYY-MM-DD): "):
    while True:
        try:
            date_str = input(prompt)
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Try again.")

# Patient Management
def add_patient():
    print("\n--- Add New Patient ---")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    disease = input("Disease: ")
    admit_date = input_date("Admit Date (YYYY-MM-DD): ")
    pid = generate_id(patients, "PAT")
    patients.append({
        "id": pid,
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease,
        "admit_date": admit_date
    })
    print(f"Patient {name} added with ID {pid}.")

def view_patients():
    print("\n--- All Patients ---")
    for p in patients:
        print(f"ID: {p['id']}, Name: {p['name']}, Age: {p['age']}, Disease: {p['disease']}, Admit: {p['admit_date']}")

def search_patient():
    pid = input("Enter Patient ID: ").upper()
    found = next((p for p in patients if p['id'] == pid), None)
    if found:
        print(f"\nPatient Details:\n{found}")
    else:
        print("Patient not found.")

# Doctor Management
def add_doctor():
    print("\n--- Add New Doctor ---")
    name = input("Name: ")
    specialization = input("Specialization: ")
    phone = input("Phone: ")
    did = generate_id(doctors, "DOC")
    doctors.append({
        "id": did,
        "name": name,
        "specialization": specialization,
        "phone": phone
    })
    print(f"Doctor {name} added with ID {did}.")

def view_doctors():
    print("\n--- All Doctors ---")
    for d in doctors:
        print(f"ID: {d['id']}, Name: {d['name']}, Specialization: {d['specialization']}, Phone: {d['phone']}")

def search_doctor():
    did = input("Enter Doctor ID: ").upper()
    found = next((d for d in doctors if d['id'] == did), None)
    if found:
        print(f"\nDoctor Details:\n{found}")
    else:
        print("Doctor not found.")

# Staff Management
def add_staff():
    print("\n--- Add New Staff ---")
    name = input("Name: ")
    role = input("Role: ")
    phone = input("Phone: ")
    sid = generate_id(staffs, "STF")
    staffs.append({
        "id": sid,
        "name": name,
        "role": role,
        "phone": phone
    })
    print(f"Staff {name} added with ID {sid}.")

def view_staffs():
    print("\n--- All Staff ---")
    for s in staffs:
        print(f"ID: {s['id']}, Name: {s['name']}, Role: {s['role']}, Phone: {s['phone']}")

# Medicine Management
def add_medicine():
    print("\n--- Add New Medicine ---")
    name = input("Medicine Name: ")
    company = input("Company: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    mid = generate_id(medicines, "MED")
    medicines.append({
        "id": mid,
        "name": name,
        "company": company,
        "price": price,
        "quantity": quantity
    })
    print(f"Medicine {name} added with ID {mid}.")

def view_medicines():
    print("\n--- All Medicines ---")
    for m in medicines:
        print(f"ID: {m['id']}, Name: {m['name']}, Company: {m['company']}, Price: ₹{m['price']}, Qty: {m['quantity']}")

# Main Menu
def main_menu():
    while True:
        print("\n=== Hospital Management System ===")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Staff Management")
        print("4. Medicine Management")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            patient_menu()
        elif choice == '2':
            doctor_menu()
        elif choice == '3':
            staff_menu()
        elif choice == '4':
            medicine_menu()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Sub-menus
def patient_menu():
    while True:
        print("\n--- Patient Menu ---")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient by ID")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def doctor_menu():
    while True:
        print("\n--- Doctor Menu ---")
        print("1. Add Doctor")
        print("2. View All Doctors")
        print("3. Search Doctor by ID")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            add_doctor()
        elif choice == '2':
            view_doctors()
        elif choice == '3':
            search_doctor()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def staff_menu():
    while True:
        print("\n--- Staff Menu ---")
        print("1. Add Staff")
        print("2. View All Staff")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            add_staff()
        elif choice == '2':
            view_staffs()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

def medicine_menu():
    while True:
        print("\n--- Medicine Menu ---")
        print("1. Add Medicine")
        print("2. View All Medicines")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            add_medicine()
        elif choice == '2':
            view_medicines()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

# Run the app
if __name__ == "__main__":
    main_menu()
