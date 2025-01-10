from tabulate import tabulate
import re


class student():
    def __init__(self):
        self.stulist = [{"stuNO":"01010101","name":"Denizer", "surname": "YILDIRIM", "grade":"15"},
            {"stuNO":"01010102","name":"Deniz Mete", "surname": "YILDIRIM", "grade":"90"},
            {"stuNO":"01010103","name":"Güneş", "surname": "YILDIRIM", "grade":"100"}]
        
        self.ogrno_oruntu = r"^\d{8}$"
        self.metin_oruntu = r"^[A-Za-zÇçĞğİıÖöŞşÜü]+$"
        self.not_oruntu = r"^(100|[1-9]?\d)$"
        self.mistakless_data=[]
        self.mistake_data=[]
        
    def save_student(self):  
        with open("ogrenci.txt","w") as stfile:
            self.headers=['stuNO', 'name', 'surname', 'grade']
            self.headers = ','.join(self.headers) 
            stfile.write(self.headers + '\n')
            for student in self.stulist:
                fileValue = f"{student['stuNO']},{student['name']},{student['surname']},{student['grade']}\n"
                stfile.write(fileValue)

                
    def student_add(self):
        
        a= input("enter the student identfy who you want to add")
        b=a.split()
        if len(b) == 4 and (re.match(self.ogrno_oruntu,b[0] ) and 
        re.match(self.metin_oruntu,b[1] ) and 
        re.match(self.metin_oruntu,b[2] ) and 
        re.match(self.not_oruntu,b[3] )) :
            new_student = {"stuNO": b[0], "name": b[1], "surname": b[2], "grade": b[3]}
            self.mistakless_data.append(new_student)
            self.stulist.append(new_student)
            self.save_student()
        else:
            self.mistake_data.append(new_student)
            print("data is wrong and append in mistake's as like as you ")
            
    def student_delete(self):
        student_id = input("Enter the ID of the student to remove: ")
        for student1 in self.stulist:
            if student1['stuNO'] == student_id:
                self.stulist.remove(student1)
                self.save_student()
                print(f"Student with ID {student_id} removed successfully!")
               
            
    def viewstudent(self):
        print("Valid students:")
        
        if self.stulist:
            print(tabulate(self.stulist, headers="keys", tablefmt="fancy_grid"))
        else:
            print("\nInvalid data (mistakes):")
        if self.mistake_data:

            print(tabulate(self.mistake_data, headers="keys", tablefmt="fancy_grid"))
        else:
            print("No mistake data available.")

        
    def searchstudent(self):
        search_value= input('which one you want search  stuno , name, surname, grade ').lower()
        if search_value == 'stuno':
            stuno= input(" enter the student's ıd ")
            filtered_students = [
                    student for student in self.stulist 
                    if  student.get("stuNO", 0) == stuno
                ]
            if not filtered_students:
                print(f"not valid {stuno}")
        elif search_value =="name":
            name= input("enter the name you want search ")
            filtered_students = [
                    student for student in self.stulist 
                    if student.get("name", 0) == name
            ]
            if filtered_students:
                print(tabulate(filtered_students, headers="keys", tablefmt="fancy_grid"))
            if not filtered_students:
                print(f"not valid {name}")
        elif search_value == "surname":
            surname= input(" enter the surname you want search ")
            filtered_students = [
                    student for student in self.stulist 
                    if student.get("surname", 0) == surname 
                ]
            if filtered_students:
                print(tabulate(filtered_students, headers="keys", tablefmt="fancy_grid"))
            if not filtered_students:
                print(f"not valid {surname}")
        elif search_value == "grade":
            grade = int(input("please enter a size of grade "))
            grade2= int(input("please enter a size of grade2 "))
            
            if (grade <100 and grade2 <= 100 and grade<grade2  ) :
                   
                filtered_students = [
                    student for student in self.stulist 
                    if grade <= int(student.get("grade", 0))<= grade2
                ]
                if filtered_students:
                    print(tabulate(filtered_students, headers="keys", tablefmt="fancy_grid"))
                else:
                    print(f"not valid {grade} {grade2}")
                        
                
                
    def choice(self):
        while True:
            secim=int(input("1- student add 2- student delete 3- student viewb 4- search student 5- exit"))     
            if secim ==1:
                self.student_add()
            elif secim ==2:
                self.student_delete()
            elif secim== 3:
                self.viewstudent()
            elif secim ==4:
                self.searchstudent()
            elif secim ==5:
                break
        
if __name__ == "__main__":
    run=student()
    run.choice()