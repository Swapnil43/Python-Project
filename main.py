from tempfile import NamedTemporaryFile
import csv
import os
import shutil

course_file_path = "C:\\Users\\User\\PycharmProjects\\courseManagementSystem\\storage\\coureses.csv"

def add_course(code,name,prereq_list):
    course_entry_row = list()
    course_entry_row.append(code)
    course_entry_row.append(name)
    course_entry_row.append(prereq_list)
    with open(course_file_path, mode='a', newline='') as courses:
        course_writer = csv.writer(courses, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        course_writer.writerow(course_entry_row)

def update_course(code,name):
    fields = ['course_code','course_name','course_prereq_list']
    temp_file = NamedTemporaryFile('w', newline='', delete=False)
    with open(course_file_path, mode='r') as courses, temp_file:
        reader = csv.DictReader(courses, fieldnames=fields)
        writer = csv.DictWriter(temp_file, fieldnames=fields)
        for row in reader:
            if row['course_code'] == str(code):
                row['course_name'] = str(name)
            row = {'course_code': row['course_code'], 'course_name': row['course_name'], 'course_prereq_list': row['course_prereq_list']}
            writer.writerow(row)
    shutil.move(temp_file.name, course_file_path)

def delete_course(code):
    fields = ['course_code','course_name','course_prereq_list']
    temp_file = NamedTemporaryFile('w', newline='', delete=False)
    with open(course_file_path, mode='r') as courses, temp_file:
        reader = csv.DictReader(courses, fieldnames=fields)
        writer = csv.DictWriter(temp_file, fieldnames=fields)
        for row in reader:
            if row['course_code'] == str(code):
                continue
            row = {'course_code': row['course_code'], 'course_name': row['course_name'], 'course_prereq_list': row['course_prereq_list']}
            writer.writerow(row)
    shutil.move(temp_file.name, course_file_path)

def check_course(name):
    with open(course_file_path, mode='r') as courses:
        course_reader = csv.DictReader(courses)
        line = 0
        for row in course_reader:
            if row['course_name'] == str(name):
                return True
    return False

def check_course_by_code(code):
    with open(course_file_path, mode='r') as courses:
        course_reader = csv.DictReader(courses)
        line = 0
        for row in course_reader:
            if row['course_code'] == str(code):
                return True
    return False

def search_course(name):
    flag = False
    with open(course_file_path, mode='r') as courses:
        course_reader = csv.DictReader(courses)
        line = 0
        for row in course_reader:
            if row['course_name'] == str(name):
                flag = True
                print(f'Course Code: {row["course_code"]}, Course_name: {row["course_name"]}, Prerequisite list: {row["course_prereq_list"]}')
    if flag == False:
        print("Course not found")

def show_all_course():
    with open(course_file_path, mode='r') as courses:
        course_reader = csv.DictReader(courses)
        line = 0
        for row in course_reader:
            print(f'Course Code: {row["course_code"]}, Course_name: {row["course_name"]}, Prerequisite list: {row["course_prereq_list"]}')

#prerq = list()
#update_course('4', 'Chemistry', ['coding', 'function'])
#delete_course('3')
#print(check_course('Dummy Subject'))
#show_all_course()

looping = 'y'
while looping == 'y':
    os.system("cls")
    print()
    print()
    print("..............................................................Course management System.........................................................")
    print()
    print("..................................................................Choose an option.............................................................")
    print()
    print()
    print("1. Show all courses and their details ")
    print("2. Add course")
    print("3. Delete course")
    print("4. Update course")
    print("5. Search course")

    choice = input("Enter your choice: ")
    if str(choice) == '1':
        print("Details of all courses")
        show_all_course()
    elif str(choice) == '2':
        cCode = input("Enter your Course code: ")
        if check_course_by_code(cCode) == False:
            new_course_name = input("Enter new course name: ")
            prereq_list = list()
            prereq_choice = input("Do you want to add course as prerequisite?(y/n): ")
            while prereq_choice == 'y':
                prereq_name = input("Enter prerequisite course name: ")
                if check_course(prereq_name) == True:
                    prereq_list.append(prereq_name)
                else:
                    print("Course name not found")
                prereq_choice = input("Do you want to add another course as prerequisite?(y/n): ")
            add_course(cCode, new_course_name, prereq_list)
            print("Course added successfully!")
        else:
            print("Course code already exists. Try another one.")
    elif str(choice) == '3':
        cCode = input("Enter course code: ")
        if check_course_by_code(cCode) == True:
            delete_course(cCode)
            print("Deleted successfully")
        else:
            print("Sorry, Course not found. :(")
    elif str(choice) == '4':
        cCode = input("Enter course code: ")
        if check_course_by_code(cCode) == True:
            new_cname = input("Enter new name of the course: ")
            update_course(cCode, new_cname)
            print("Updated successfully")
        else:
            print("Sorry, Course not found. :(")
    elif str(choice) == '5':
        cName = input("Enter course name: ")
        search_course(cName)
    else:
        print("Invalid input.")
    looping = input("Do you want to continue?(y/n): ")
    os.system("cls")


