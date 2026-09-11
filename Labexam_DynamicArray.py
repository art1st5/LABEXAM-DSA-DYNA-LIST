

class Student():
    def __init__(self, ID, name, course, YearLvl):

        self._stud_Id = ID
        self._stud_name = name
        self._Stud_course = course
        self._Stud_YearLvl = YearLvl

    def setId(self, ID):
        self._stud_Id = ID

    def setName(self, name):
        self._stud_name = name

    def setCourse(self, course):
        self._Stud_course = course

    def setYearLvl(self, YEARLvl):
        self._Stud_YearLvl = YEARLvl

    def getId(self):
        return self._stud_Id

    def getName(self):
        return self._stud_name.upper()

    def getCourse(self):
        return self._Stud_course.upper()

    def getYearLvl(self):
        return self._Stud_YearLvl  

    def display(self):
        print("Student ID:", self._stud_Id)
        print("Student Name:", self._stud_name.upper())
        print("Student Course:", self._Stud_course.upper())
        print("Student Year Level:", self._Stud_YearLvl)

    def displaystudent(self):
        print("ID NUMBER:", self._stud_Id)
        print("NAME:", self._stud_name.upper())
        print("COURSE:", self._Stud_course.upper())
        print("YEAR LEVEL:", self._Stud_YearLvl)

class DynamicArr():
    def __init__(self):
        self.index = 0
        self.capacity = 5
        self.arr = [None] * self.capacity

    def input_add_student(self):
    
        ID = input("Enter Student ID: ")    
        name = input("Enter Student Name: ")
        course = input("Enter Student Course: ")
        YearLvl = input("Enter Student Year Level: ")

        new_student = Student(ID, name, course, YearLvl)
        self.add_student(new_student)
        print("Student added successfully")

    def add_student(self, value):
        if self.index == self.capacity:
            self.resize(self.capacity * 2)
        self.arr[self.index] = value
        self.index += 1

    def resize(self, new_capacity):
        bigger = [None] * new_capacity
        for i in range(self.index):
            bigger[i] = self.arr[i]
        self.arr = bigger
        self.capacity = new_capacity

    def input_idSearch(self):
        stud_Id = input("Enter Student ID to search: ")
        self.id_search(stud_Id)

    def id_search(self, stud_Id ):
        for i in range(self.index):
            if self.arr[i].getId() == stud_Id:
                print("====Student found!====")
                self.arr[i].display()
                return
        print(f"No student found with ID '{stud_Id}'.")

    def update_stud_input(self):
        stud_Id = input("Enter Student ID to update information: ")
        for i in range(self.index):
            if self.arr[i].getId() == stud_Id:
                print("Student found")
                self.arr[i].display()
                new_name = input("Enter new name: ")
                new_course = input("Enter new course: ")
                new_yearlvl = input("Enter new year level: ")
                self.arr[i].setName(new_name)
                self.arr[i].setCourse(new_course)
                self.arr[i].setYearLvl(new_yearlvl)
                print("Student information updated")
                return
        print("Student not found.")
        
    def delete_stud_input(self):
        self.display_students()
        stud_Id = input("Enter Student ID to delete: ")
        for i in range(self.index):
            if self.arr[i].getId() == stud_Id:
                print("Student found")
                self.arr[i].display()

                while True:
                    confirm = input("Are you sure you want to delete this student:\nName: " 
                                    + self.arr[i].getName() 
                                    + "\nCourse: (" 
                                    + self.arr[i].getCourse() 
                                    + ")\nType 'YES' to confirm, 'NO' to cancel: ")
                    if confirm.upper() == 'YES':

                        for j in range(i, self.index - 1):
                            self.arr[j] = self.arr[j + 1]
                        self.arr[self.index - 1] = None
                        self.index -= 1
                        print("Student deleted successfully!")
                        return
                    elif confirm.upper() == 'NO':
                            print("Deletion cancelled.")
                            return
                    else:
                        print("====Invalid input. Type 'YES' to confirm deletion or 'NO' to cancel====")
        print("Student not found.")

    def display_students(self):
        if self.index == 0:
            print("No students to display.")
            return

        for i in range(self.index):
            print(f"{'STUDENT INFORMATIONS':^50}")
            print("-" * 50) 
            self.arr[i].displaystudent()
            print("-" * 50) 



    def display_array_info(self):
            print("=" * 50)
            print(f"{'Array Information':^50}")
            print("=" * 50)
            print(f"Number of Students:  {self.index}")
            print(f"Array Capacity: {self.capacity}" )
            
            arrays = [f"[{self.arr[i].getName()}] " for i in range(self.index)]
            print("".join(arrays))


def main_menu():
    dynamic_arr = DynamicArr()

    menu_text = ''' select the following:
1. Dynamic Array

'''
    array_text = ''' 
1.Add Student
2.Display Students
3.Search Student
4.Update Student
5.Remove Student
6.Display Array Information
7.Exit
'''     
    while True:
        print("=" * 50)
        print(f"{'Student Record Management:':^50}")
        print("=" * 50)
        menu = input(menu_text + "\nEnter choice: ")

        match menu:

            case '1':

                while True:
                    print("="*50)
                    print(f"{'Student Record Management:':^50}")
                    print("="*50)
                    menu_array = input(array_text + "\nEnter choice: ")
                    print("\033c", end="\033[A")

                    match menu_array:
                            
                        case '1':
                            dynamic_arr.input_add_student()
                            test = input("Press ENTER to continue")
                        case '2':
                            print("\033c", end="\033[A")
                            dynamic_arr.display_students()
                            test = input("Press ENTER to continue")
                        case '3':
                            dynamic_arr.input_idSearch()
                            test = input("Press Anything to continue")
                        case '4':
                            print("\033c", end="\033[A")
                            dynamic_arr.update_stud_input()
                            test = input("Press ENTER to continue")
                        case '5':
                            dynamic_arr.delete_stud_input()
                            test = input("Press ENTER to continue")
                        case '6':
                            dynamic_arr.display_array_info()
                            test = input("Press ENTER to continue")
                        case '7':
                            print ("\nExiting menu..")
                            break
                        case _:
                            print("Invalid input")
        
if __name__ == "__main__":
    main_menu()
