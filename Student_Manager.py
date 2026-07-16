FILE_NAME= "student.txt"
def add_student(): #This function adds a new student record to the file
    name = input("Enter student name: ").capitalize() #This line takes the student's name as input and capitalizes it
    num_subjects = int(input("How many subjects? ")) #This line takes the number of subjects as input and converts it to an integer
    record = name #This line initializes the record variable with the student's name

    for i in range(num_subjects): #This loop iterates over the number of subjects and takes input for each subject's name, marks, and credits
        print(f"\nSubject {i+1}") #This line prints the subject number (i+1) to indicate which subject is being entered
        subject = input("Enter subject name: ").capitalize() #This line takes the subject name as input and capitalizes it
        marks = input("Enter marks: ") #This line takes the marks as input
        credits = input("Enter credits for this subject: ") #This line takes the credits as input
        record += "," + subject + ":" + marks + ":" + credits #This line appends the subject, marks, and credits to the record variable in the format "subject:marks:credits"

    with open(FILE_NAME, "a") as file: #This line opens the file in append mode, allowing new records to be added without overwriting existing data
        file.write(record + "\n")

    print("-" * 20) #This line prints a separator line of dashes for better readability in the console output
    print("Student record saved!") #This line prints a confirmation message indicating that the student record has been successfully saved to the file
    print("-" * 20) #This line prints another separator line of dashes for better readability in the console output 

def view_students(): #This function reads and displays all student records from the file and handles the case where the file does not exist
    try:
        with open(FILE_NAME, "r") as file: #This line opens the file in read mode, allowing the program to read the contents of the file
            records = file.readlines()

            if not records: #This line checks if the records list is empty, indicating that there are no student records in the file
                print("\nNo student records found.")
                return

            print("\n" + "=" * 15) #This line prints a separator line of equal signs for better readability in the console output 
            print("STUDENT RECORDS") #This line prints a header indicating that the following output will display student records
            print("=" * 15) #This line prints another separator line of equal signs for better readability in the console output

            for student_no, line in enumerate(records, start=1): #This loop iterates over each line in the records list, where student_no is the index of the student (starting from 1) and line is the actual line of text representing a student's record
                data = line.strip().split(",")
                name = data[0]

                print(f"\nStudent {student_no}")
                print("-" * 15)
                print(f"Name : {name}\n")
                for i, subject_data in enumerate(data[1:], start=1): #This loop iterates over the subject data for each student, where i is the index of the subject (starting from 1) and subject_data is the actual string containing the subject, marks, and credits
                    subject, marks, credits = subject_data.split(":")
                    print(f"{i}. Subject : {subject}")
                    print(f"   Marks   : {marks}")
                    print(f"   Credits : {credits}")

            print("\n" + "=" * 15)

    except FileNotFoundError:
        print("No records found.")

def calculate_average(): #This function calculates and displays the average marks for each student in the file. It handles the case where the file does not exist.
    try:
        with open(FILE_NAME, "r") as file:
            for line in file: #This loop iterates over each line in the file, where line represents a single student's record   
                data = line.strip().split(",")
                name = data[0]
                total = 0
                count = 0
                for subject_data in data[1:]: #This loop iterates over the subject data for each student, where subject_data is the actual string containing the subject, marks, and credits
                    subject, marks, credits = subject_data.split(":")
                    total += int(marks)
                    count += 1
                average = total / count
                print(f"{name}'s Average =", average)
    except FileNotFoundError:
        print("No records found.")

def clear_records(): #This function clears all student records from the file after confirming with the user. It handles the case where the file does not exist.
    confirm = input("Delete all records? (yes/no): ")
    if confirm.lower() == "yes": #This line checks if the user input is "yes" to confirm the deletion of all records
        with open(FILE_NAME, "w") as file:
            pass
        print("-" * 20)
        print("All records deleted.") #This line prints a confirmation message indicating that all student records have been successfully deleted from the file
        print("-" * 20)
    else: #This line handles the case where the user input is not "yes", indicating that the deletion of all records has been cancelled
        print("Operation cancelled.")

def calculate_sgpa(): #This function calculates and displays the SGPA (Semester Grade Point Average) for each student in the file. It handles the case where the file does not exist.
    try:
        with open(FILE_NAME, "r") as file:

            for line in file: #This loop iterates over each line in the file, where line represents a single student's record
                data = line.strip().split(",")

                name = data[0]

                total_points = 0
                total_credits = 0

                for subject_data in data[1:]: #This loop iterates over the subject data for each student, where subject_data is the actual string containing the subject, marks, and credits

                    subject, marks, credits = subject_data.split(":")

                    marks = int(marks)
                    credits = int(credits)

                    # Grade Point Calculation
                    if marks >= 90:
                        grade_point = 10
                    elif marks >= 80:
                        grade_point = 9
                    elif marks >= 70:
                        grade_point = 8
                    elif marks >= 60:
                        grade_point = 7
                    elif marks >= 50:
                        grade_point = 6
                    else:
                        grade_point = 0

                    total_points += grade_point * credits
                    total_credits += credits

                if total_credits > 0: #This line checks if the total number of credits is greater than zero to avoid division by zero when calculating SGPA
                    sgpa = total_points / total_credits
                    print(f"{name}'s SGPA = {sgpa:.2f}")
                else: #This line handles the case where a student has no subjects, resulting in zero total credits, and prints a message indicating that the student has no subjects to calculate SGPA.
                    print(f"{name} has no subjects.")

    except FileNotFoundError:
        print("No records found.")

def delete_student(): #This function deletes specific student record from the file based on the student's name provided by the user. It handles the case where the file does not exist.
    name_to_delete = input("Enter student name to delete: ") #This line takes the student's name to delete as input from the user

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file: #This line opens the file in write mode, allowing the program to overwrite the existing records with the updated records after deleting the specified student record
            for record in records:
                data = record.strip().split(",")

                if data[0].lower() != name_to_delete.lower():
                    file.write(record)
                else:
                    found = True

        if found: #This line checks if the specified student record was found and deleted. If found is True, it indicates that the student record was successfully deleted.
            print("-" * 20)
            print("Student record deleted successfully.")
            print("-" * 20)
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No records found.")

def total_students():#calculate total students
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
            total = len(records) #This line calculates the total number of student records by determining the length of the records list, which contains all the lines read from the file. Each line represents a student record, so the length of this list gives the total number of students.
            if total == 0: #This line checks if the total number of student records is zero, indicating that there are no student records in the file. If this condition is true, it prints a message stating that no student records were found.
                print("No Student records found.")
            else:
                print(f"Total Students: {total}")
    except FileNotFoundError:
        print("No records found.")  

def search_student(): #This function searches for a specific student record in the file based on the student's name provided by the user. It handles the case where the file does not exist.
    name = input("Enter student name to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for line in file:
                data = line.strip().split(",")

                if data[0].lower() == name.lower():
                    found = True
                    print("\nStudent Found")
                    print(" Name:", data[0])

                    for subject in data[1:]:
                        sub, marks, credits = subject.split(":")
                        print(f" Subject: {sub}\n Marks: {marks}\n Credits: {credits}")

            if not found: #This line checks if the specified student record was found in the file. If found is False, it indicates that the student record was not found, and it prints a message stating that the student was not found.
                print("Student not found.")

    except FileNotFoundError:
        print("No records found.")  

def update_student(): #This function updates a specific student record in the file based on the student's name provided by the user. It handles the case where the file does not exist.
    name_to_update = input("Enter student name to update: ").capitalize() #User input for the name of the student whose record needs to be updated. The input is capitalized to maintain consistency in the records.

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for record in records:
                data = record.strip().split(",")

                if data[0].lower() == name_to_update.lower(): #This line checks if the name of the student in the current record matches the name provided by the user for updating. It compares the lowercase versions of both names to ensure case-insebsitive matching. 
                    found = True

                    print("\nCurrent Record")
                    print("-" * 40)
                    print("Name:", data[0])

                    for i, subject_data in enumerate(data[1:], start=1): #This loop iterates over the subject data for the student whose record is being updated. It starts enumerating from 1 to display the subject number in the output. Each subject's details (subject name, marks, and credits) are extracted and printed in a formatted manner for the user to see the current record before making updates.
                        subject, marks, credits = subject_data.split(":")
                        print(f"{i}. {subject} | Marks: {marks} | Credits: {credits}")
                    print("=" * 40)
                    print("\nEnter New Details")
                    print("=" * 40)

                    new_name = input("Enter new student name: ").capitalize() #User input for the new name of the student. The input is capitalized to maintain consistency in the records.

                    while True:
                        try:
                            num_subjects = int(input("Enter number of subjects: ")) #User input for the number of subjects the student has. The input is converted to an integer. The loop continues until a valid positive integer is entered, ensuring that at least one subject is provided for the student.
                            if num_subjects > 0:
                                break
                            print("Enter at least one subject.")
                        except ValueError:
                            print("Enter a valid number.")

                    new_record = new_name #This line initializes the new_record variable with the new name of the student. It will be used to construct the updated record for the student, including the new name and the details of each subject (subject name, marks, and credits) that will be entered in the subsequent loop.

                    for i in range(num_subjects):
                        print(f"\nSubject {i+1}")

                        subject = input("Subject Name : ").capitalize() #User input for the name of subject. The input is capitalized to maintain consistency in the records.

                        while True:
                            try:
                                marks = int(input("Marks (0-100): ")) #User input for the marks obtained in the subject. The input is converted to an integer. The loop continues until a valid integer between 0 and 100 is entered, ensuring that the marks are within the acceptable range for grading.
                                if 0 <= marks <= 100:
                                    break
                                print("Marks must be between 0 and 100.")
                            except ValueError:
                                print("Enter valid marks.")

                        while True:
                            try:
                                credits = int(input("Credits : ")) #User input for the number of credits assigned to the subject. The input is converted to an integer. The loop continues until a valid positive integer is entered, ensuring that the credits are greater than zero for the subject.
                                if credits > 0:
                                    break
                                print("Credits must be greater than 0.")
                            except ValueError:
                                print("Enter valid credits.")

                        new_record += f",{subject}:{marks}:{credits}" #Updates the new_record by appending the new details.

                    file.write(new_record + "\n")

                else:
                    file.write(record)

        if found: #This line checks if the specified student record was found and updated. If found is True, it indicates that the student record was successfully updated, and it prints a confirmation message indicating that the student record has been updated successfully.
            print("\nStudent record updated successfully.")
        else:
            print("\nStudent not found.")

    except FileNotFoundError:
        print("No records found.")

def student_ranking(): #This function calculates and displays the ranking of students based on their average marks. It handles the case where the file does not exist.
    try:
        with open(FILE_NAME, "r") as file:
            rankings = []

            for line in file:
                data = line.strip().split(",")
                name = data[0]

                total_marks = 0
                total_subjects = 0

                for subject_data in data[1:]:
                    subject, marks, credits = subject_data.split(":")
                    total_marks += int(marks)
                    total_subjects += 1

                average = total_marks / total_subjects #Uses the total marks and total subjects to calculate the average marks for each student.
                rankings.append((name, average))

            rankings.sort(key=lambda x: x[1], reverse=True)

            print("\n" + "=" * 35)
            print("      STUDENT RANKING")
            print("=" * 35)
            print(f"{'Rank':<6}{'Name':<15}{'Average'}")
            print("-" * 35)

            for rank, (name, avg) in enumerate(rankings, start=1): #This loop iterates over the sorted rankings list, where rank is the index of the student in the ranking (starting from 1), name is the student's name, and avg is the average marks for that student. The enumerate function is used to generate the rank number automatically based on the position of the student in the sorted list. The loop prints each student's rank, name, and average marks in a formatted manner for better readability in the console output.
                print(f"{rank:<6}{name:<15}{avg:.2f}")

    except FileNotFoundError:
        print("No records found.")

def topper_details(): #This function calculates and displays the details of the student with the highest average marks and the student with the highest SGPA (Semester Grade Point Average). It handles the case where the file does not exist.
    try:
        with open(FILE_NAME, "r") as file:

            highest_avg = -1 #Initialaziation of the highest average to -1.
            highest_sgpa = -1 #Initialization of the highest SGPA to -1.

            avg_topper = "" #Initialization of avg_topper to an empty string.
            sgpa_topper = "" #Initialization of sgpa_topper to an empty string.

            for line in file:
                data = line.strip().split(",")
                name = data[0]

                total_marks = 0 #Initialization of total_marks to 0.
                total_subjects = 0 #Initialization of total_subjects to 0.

                total_points = 0 #Initialization of total_points to 0.
                total_credits = 0 #Initialization of total_credits to 0.

                for subject_data in data[1:]:
                    subject, marks, credits = subject_data.split(":")

                    marks = int(marks) #This line converts the marks obtained in the subject from a string to an integer, allowing for numerical calculations and comparisons in subsequent operations.
                    credits = int(credits) #This line converts the number of credits assigned to the subject from a string to an integer, allowing for numerical calculations and comparisons in subsequent operations.

                    total_marks += marks #Calculates the total marks obtained by the student.
                    total_subjects += 1 #Calculates the total number of subjects taken by the student.
                    # Grade Point Calculation
                    if marks >= 90:
                        grade_point = 10
                    elif marks >= 80:
                        grade_point = 9
                    elif marks >= 70:
                        grade_point = 8
                    elif marks >= 60:
                        grade_point = 7
                    elif marks >= 50:
                        grade_point = 6
                    else:
                        grade_point = 0

                    total_points += grade_point * credits #Calculates total grade points earned by a student.
                    total_credits += credits #Calculates total credits earned by a student.

                average = total_marks / total_subjects #Calculates the average marks obtained.
                sgpa = total_points / total_credits #Calculates the sgpa of the student.

                if average > highest_avg: #This line check if  the average marks of current student is greater than highest average.
                    highest_avg = average
                    avg_topper = name

                if sgpa > highest_sgpa: #This line check if  the sgpa of current student is greater than highest sgpa.
                    highest_sgpa = sgpa
                    sgpa_topper = name

            print("\n" + "=" * 40) #Prints the highest student average and sgpa in a formatted manner for better readability in the console output.
            print("           TOPPER DETAILS")
            print("=" * 40)
            print(f"Topper by Average : {avg_topper}")
            print(f"Average Marks     : {highest_avg:.2f}")
            print("-" * 40)
            print(f"Topper by SGPA    : {sgpa_topper}")
            print(f"SGPA              : {highest_sgpa:.2f}")
            print("=" * 40)

    except FileNotFoundError:
        print("No records found.")

def pass_fail_report():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            if not records:
                print("\nNo student records found.")
                return

            print("\n" + "=" * 45)
            print("           PASS / FAIL REPORT")
            print("=" * 45)

            for line in records:
                data = line.strip().split(",")
                name = data[0]

                failed_subjects = []

                for subject_data in data[1:]:
                    subject, marks, credits = subject_data.split(":")
                    marks = int(marks)

                    if marks < 50:
                        failed_subjects.append((subject, marks))

                print(f"\nStudent : {name}")

                if len(failed_subjects) == 0:
                    print("Status  : PASS")
                else:
                    print("Status  : FAIL")
                    print("Failed Subjects:")
                    for subject, marks in failed_subjects:
                        print(f"   • {subject} ({marks} Marks)")

            print("\n" + "=" * 45)

    except FileNotFoundError:
        print("No records found.")

def main(): #Main function that displays the menu and handles user input for various operations related to student records.
    print("=" *15 + "\nStudent Manager\n" +"=" *15)
    while True:
        print("_" *16 + "\n      MENU\n" +"*" *16)
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Average")
        print("4. Clear Records")
        print("5. Calculate SGPA")
        print("6. Delete Student Record")
        print("7. Total Students")
        print("8. Search Student")
        print("9. Update Student Record")
        print("10. Student Ranking")
        print("11. Topper Details")
        print("12. Pass/Fail Report")
        print("13. Exit")

        choice = input("Enter your choice(1-13): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            clear_records()
        elif choice == "5":
            calculate_sgpa()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            total_students()
        elif choice == "8":
            search_student()
        elif choice == "9":
            update_student()
        elif choice == "10":
            student_ranking()
        elif choice == "11":
            topper_details()
        elif choice == "12":
            pass_fail_report()
        elif choice == "13":
            print("Program Ended.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    try: #This line checks if the script is being run directly (not imported as a module) and executes the main function to start the program.
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
