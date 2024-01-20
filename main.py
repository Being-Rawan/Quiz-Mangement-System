import os
import json
#from quizze import add_quize, delete_quize
def quize_info(line):
    return line.split(",")
def sherch_quize():
    b = 0
    que=input("enter quize title to shrch: ")
    with open("./database/quizzes.csv", "r") as file:
        all_lines = file.readlines()
    for line in all_lines:
        if (que in quize_info(line)[1] ):
            b = 1
            for ll in quize_info(line):
                if ("quize id" in ll or 'quize title' in ll or "qestion" in ll or "answers" in ll):
                    print(ll)
    if(b != 1):
        print("invalid")

def add_quize():
    ids_list=[]
    enter_id = input("Enter quize id: ")
    enter_tit = input("Enter quize title: ")
    with open('./database/quizzes.csv', "a") as f:  # what with do ?
        f.write(f"quize id : {enter_id},")
        f.write(f"quize title : {enter_tit},")
        print("quiz has been added succesfully\n")
    while 1:
        print("1.add question \n2.exite ")
        chh=int(input("enter your choice: "))
        if chh == 1 :
            question_id = input("enter question id: ")
            question = input("enter a question: ")
            question_ans = input("enter answers: ")
            ids_list.append(question_id)
            with open('./database/quizzes.csv', "a") as f:  # what with do ?
                f.write(f"qestion : {question}," )
                f.write(f"answers : {question_ans},")
                f.close()
        else :
            with open('./database/quizzes.csv', "a") as f:
                for ids in ids_list :
                    f.write(f"{ids},")
                f.write("\n")
                f.close()
            break
def delete_quize():
    que=input("enter quize title to delete: ")
    with open("./database/quizzes.csv", "r") as file:
        all_lines = file.readlines()
    with open("./database/quizzes.csv", "w") as file:
        s="quize title : "
        for line in all_lines:
            if quize_info(line)[1] != s+que:
                file.write(line)
                file.close()
                print("quiz has been deleted succesfully\n")
def show_quizes():
    with open("./database/quizzes.csv", "r") as file:
        all_lines = file.readlines()
    for line in all_lines:
        print(quize_info(line)[1])

login = False
admin = False
while True:
    print(
        "press 1 to register\npress 2 to login\npress 3 to log in as a professor \npress other key or num to exit: "
    )
    choice = int(input())
    if choice == 1:  # el registeration
        counter = 0
        id = int(input("enter your ID: "))
        name = str(input("enter your name: "))
        email = input("enter your email: ")
        password = input("enter password: ")
        age=input("enter your age: ")
        level = input("enter your level from 1 to 4: ")

        users = []
        if not os.path.exists("./database/users.json"):  # to open file for users if not exist
            f = open("./database/users.json", "w")
            json.dump(users, f)
            f.close()
        with open("./database/users.json", "r") as f:
            content = json.load(f)
            for user in content:
                if (
                    id == user[0]
                ):  # 34an a4of lw el user dh mawgood 2bl keda 34an lw mawgood my3ml4 register tany
                    print("\nthe user already exist")
                    counter = 1
                    break
            if counter == 0:
                users = content
                users.append(
                    [id, name, email, password,"age : "+age ,"level age is :" + level]
                )  # b3d ma et2akedt eno m4 mwgood hsagelo f el system
                with open("./database/users.json", "w") as f:
                    json.dump(users, f)
                    print("**you have been registered successfully**")

    elif choice == 2:  # el login
        counter = 0
        id = int(input("enter your ID: "))
        passw = str(input("enter your password: "))
        with open("./database/users.json", "r") as f:
            content = json.load(f)
            for user in content:  # bdwr 3leh f file el users
                if id == user[0]:
                    counter = 1

            if counter == 0:
                print("Invalid user\n\n")

            elif counter == 1:
                for user in content:
                    if passw == user[3]:
                        print("\n**login has been successfully**\n")
                        login = True
                if login == False:
                    print("wrong password")
                else:
                    break

    elif choice == 3:
        check = 0
        professors = []
        professor_name = input("enter your name: ")
        password = input("enter your password: ")
        if not os.path.exists("./database/professors.json"):
            f = open("./database/professors.json", "w")
            json.dump(professors, f)
            f.close()

        with open("./database/professors.json", "r") as f:
            professors = json.load(f)
            for professor in professors:
                if professor_name == professor[1]:
                    check = 1
                    break
            if check == 0:
                print("wrong name please try again\n")
            elif check == 1:
                for professor in professors:
                    if password == professor[3]:
                        check = 2
                        break

            if check == 1:
                print("wrong password\n")
            elif check == 2:
                print("\n**login has been successfully**\n")
                admin = True
                break

    else:
        break

while login:
    print(
        "1.To see the list of quizzes \n2.to serch for quiz \n3.to send answer for quiz  \n4.to see your grades  \n5.prees other key to exit"
    )
    choice = (input())
    if choice == '1':
        show_quizes()

    elif choice == '2':
        sherch_quize()


    elif choice == '3':
        file = []
        content = []
        id = input("enter quize id: ")
        student_name = input("enter your name: ")
        answers = input("enter your answers: ")

        if not os.path.exists("./database/answer of quizzes.json"):
            with open("./database/answer of quizzes.json", "w") as f:
                json.dump(file, f)
                f.close()
        with open("./database/answer of quizzes.json") as f:
            file = json.load(f)
            file.append([id, "student name: " + student_name, "answers: " + answers])
            with open("./database/answer of quizzes.json", "w") as s:
                json.dump(file, s)
        with open("./database/users.json", "r") as s:
            content = json.load(s)
            for user in content:
                if id == user[0]:
                    user.append("has solve the exam with id " + student_name)
        print("your answer has been submited succesfully\n")

    elif choice == '4':
        id = str(input("enter your id: "))
        check = True
        check2 = True
        if not os.path.exists("./database/grades.json"):
            print("The quizzes have not been corrected yet\n")
            check = False

        if check:
            with open("./database/grades.json", "r") as f:
                grades = json.load(f)
                for grade in grades:
                    if id == grade[0]:
                        print(grade, "\n")
                        check2 = False
                if check2:
                    print("Your score has not been set yet\n")
    else:
        break

while admin:
    print(
        "press 1 to add quizzes \npress 2 to remove quizzes \npress 3 to see List of registered students and if they send answers"
    )
    print(
        "press 4 to see answers of quizzes \npress 5 to give score to students  \npress 6 to see your information \npress other key to exit"
    )
    choice = input("")
    if choice == '1':
        add_quize()

    elif choice == '2':
        delete_quize()

    elif choice == '3':
        students = []
        if not os.path.exists("./database/users.json"):
            f = open("./database/users.json", "w")
            json.dump(students, f)
            f.close()

        with open("./database/users.json", "r") as f:
            students = json.load(f)
            for user in students:
                print(user)

    elif choice == '4':
        answers = []
        if not os.path.exists("./database/answer of quizzes.json"):
            with open("./database/answer of quizzes.json", "w") as f:
                json.dump(answers, f)
                f.close()
        with open("./database/answer of quizzes.json") as f:
            answers = json.load(f)
            for answer in answers:
                print(answer)

    elif choice == '5':
        added = True
        grades = []
        student_id = input("enter student id: ")
        quiz_name = input("enter quiz_title: ")
        score = input("enter score: ")
        if not os.path.exists("./database/grades.json"):
            with open("./database/grades.json", "w") as f:
                json.dump(grades, f)
                f.close()

        with open("./database/grades.json") as f:
            grades = json.load(f)
            for student in grades:
                if student_id == student[0]:
                    student.append(quiz_name + " : " + score)
                    added = False

        if added:
            grades.append([student_id, quiz_name + " : " + score])

        with open("./database/grades.json", "w") as f:
            json.dump(grades, f)

    elif choice == '6':
        professors=[]
        with open("./database/professors.json", "r") as f:
            professors = json.load(f)
            for professor in professors:
                if professor_name==professor[1]:
                    print(professor)


    else:
        break
