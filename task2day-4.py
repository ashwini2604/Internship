class Person:
    def __init__(self, name, **kwargs):
        # Using **kwargs to pass extra arguments up the chain
        super().__init__(**kwargs)
        self.name = name

    def display_person(self):
        print(f"Name: {self.name}")


class Student(Person):
    def __init__(self, student_id, **kwargs):
        super().__init__(**kwargs)
        self.student_id = student_id

    def display_student(self):
        print(f"Student ID: {self.student_id}")


class SportsPlayer(Person):
    def __init__(self, sport_name, **kwargs):
        super().__init__(**kwargs)
        self.sport_name = sport_name

    def display_sports_player(self):
        print(f"Sport: {self.sport_name}")


class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        # Initialize the hierarchy with all required arguments
        super().__init__(
            name=name, 
            student_id=student_id, 
            sport_name=sport_name
        )
        self.college_name = college_name

    def display_college_student(self):
        print(f"--- College Student Details ---")
        self.display_person()         # From Person
        self.display_student()        # From Student
        self.display_sports_player()  # From SportsPlayer
        print(f"College: {self.college_name}")


# --- Testing the System ---

# Creating one object of CollegeStudent
student_athlete = CollegeStudent(
    name="Jordan Miller", 
    student_id="S10245", 
    sport_name="Basketball", 
    college_name="Greenwood University"
)

# Displaying all details
student_athlete.display_college_student()