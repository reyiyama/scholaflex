class Course:  # This is the course class that has all the parameters to accommodate the Courses
    def __init__(self, id, name, credit):  # name and credits are the main parameters for course
        self.id = id  # The unique identifier for the course
        self.name = name  # The name of the course e.g. Java, etc.
        self.credit = credit  # The number of credits associated with the course
        self.students_finished = 0  # a counter for students who finished the course
        self.students_ongoing = 0  # a counter for students currently enrolled in the course
        self.total_score = 0  # This is the sum of all student scores in the course
    
    def add_student_score(self, score):
        if score != '--':
            self.total_score += score  # As long as the score is not '--' the score is incremented 
            self.students_finished += 1  # Incrementing the counter of students who have finished the course
        else:
            self.students_ongoing += 1  # Incrementing the counter of students currently enrolled in the course
    
    def average_score(self):  # This is the calculation for the average score based on how many students finished the course versus how many didn't
        # The average is calculated by dividing the total score by the number of students who finished the course.
        # If no students have finished the course yet, the average score is 0
        return self.total_score / self.students_finished if self.students_finished > 0 else 0


class CoreCourse(Course):  # This class is a placeholder for all of the Core Courses taken by a student, usually all
    def __init__(self, id, name, credit):
        super().__init__(id, name, credit)  # Call to the parent class's constructor to initialize common attributes
        self.semester = "All"  # Core courses are typically conducted in all semesters


class ElectiveCourse(Course):  # This class is designed for the Elective Courses, which may not be taken by all students and can vary by semeste
    def __init__(self, id, name, credit, semester):
        super().__init__(id, name, credit)  # Call to the parent class' constructor to initialize its common attributes
        self.semester = semester  # Elective courses are semester-specific, so this attribute stores the semester the course is held in

class Student:
    def __init__(self, id, name, student_type):
        self.id = id  # The unique identifier for the student a student id is unique
        self.name = name  # The name of the student
        self.student_type = student_type  # The type of student (e.g., UG, PG)
        self.courses = {}  # A dictionary to store the courses the student is enrolled in, keyed by course_id with scores as values like COSC or ISYS
        self.mode = None  

    def add_course(self, course_id, score):
        self.courses[course_id] = score  # this exists to add the course to the student's course dictionary with the corresponding score
    
    def calculate_gpa(self):
        # this function defines the GPA based on the scores of completed courses.
        # GPA is calculated on a 100-point scale and a 4-point scale.
        completed_courses = [score for score in self.courses.values() if score != '--']  # This filter helps remove out the completed courses
        if completed_courses:
            gpa_100 = sum(completed_courses) / len(completed_courses)  
            gpa_4 = gpa_100 / 25  # converts GPA to a 4-point scale
            return gpa_100, gpa_4
        else:
            return 0, 0

    def number_courses_finished(self):
        # this function calculates the number of courses that the student has finished
        return len([score for score in self.courses.values() if score != '--'])

    def number_courses_ongoing(self):
        # calculates the number of courses that the student is currently enrolled in
        return len([score for score in self.courses.values() if score == '--'])

    def satisfies_enrollment(self):
        # checks if the student is enrolled in at least the minimum number of courses
        return len(self.courses) >= self.min_courses

    def weighted_gpa_4(self, courses):
        # calculates the weighted GPA on a 4-point scale, taking into account the credit value of each course
        weighted_sum = 0
        total_credits = 0
        for course_id, score in self.courses.items():
            if score != '--':
                weighted_sum += score / 25 * courses[course_id].credit  # this calculates the weighted sum of scores
                total_credits += courses[course_id].credit  # this calculates the total credits
        return weighted_sum / total_credits if total_credits > 0 else 0  

    def average_score_100(self):
        # Calculate the average score on a 100-point scale
        completed_courses = [score for score in self.courses.values() if score != '--']  # filters out the completed courses
        if completed_courses:
            gpa_100 = sum(completed_courses) / len(completed_courses)  # calculates the average score, just like done before
            return gpa_100
        else:
            return 0

    def average_score_4(self):
        # calculates the average score on a 4-point scale
        completed_courses = [score for score in self.courses.values() if score != '--']  # filters out the completed courses
        if completed_courses:
            gpa_100 = sum(completed_courses) / len(completed_courses)  # calculates the average score
            gpa_4 = gpa_100 / 25  #convert the average score to a 4-point scale
            return gpa_4
        else:
            return 0

class UndergraduateStudent(Student):
    min_courses = 4  # this is the minimum number of courses an undergraduate student should be enrolled in.
    def __init__(self, id, name):
        super().__init__(id, name, 'UG')  # this inherits from the Student class and set the student type as 'UG' for undergraduate.


class PostgraduateStudent(Student):
    def __init__(self, id, name, mode):
        super().__init__(id, name, 'PG')  # This inherits from the Student class and set the student type as 'PG' for postgraduate.
        self.mode = mode  # mode of study for the postgraduate student can be 'PT' for part-time or 'FT' for full-time.
        # The minimum number of courses a postgraduate student should be enrolled in depends on their mode of study.
        self.min_courses = 2 if mode == 'PT' else 4 #if part time, the student can be enrolled in 2 courses, if not, it is 4

class Results:
    def __init__(self):
        self.students = {}  # Student object dictionary key is student ID.
        self.courses = {}  # Course object dictionary key is course ID.

    def read_courses(self, file_name):
        # This method reads the courses details from a file and populates the courses dictionary.
        with open(file_name, 'r') as file:
            for line in file:
                # this extracts course details from each line of the file.
                course_id, course_type, course_name, course_credit, *course_semester = line.strip().split(',')
                try:
                    # this converts course credit to integer. If it fails, it means the data is invalid.
                    course_credit = int(course_credit)
                except ValueError:
                    print(f"Invalid credit value for course {course_id}. Skipping this course.") #as suggested in HD or DI 
                    continue
                # If course type is 'C', create a CoreCourse object, else create an ElectiveCourse object.
                if course_type.strip() == 'C':
                    self.courses[course_id] = CoreCourse(course_id, course_name, course_credit)
                elif course_type.strip() == 'E':
                    self.courses[course_id] = ElectiveCourse(course_id, course_name, course_credit, course_semester[0] if course_semester else "All") #all semesters have core courses

    def read_students(self, file_name):
        # reads the student details from a file and populates the students dictionary.
        with open(file_name, 'r') as file:
            for line in file:
                # extracts student details from each line of the file.
                student_id, name, student_type, *mode = line.strip().split(',')
                # if student type is 'UG', create an UndergraduateStudent object, else create a PostgraduateStudent object.
                if student_type.strip() == 'UG':
                    self.students[student_id] = UndergraduateStudent(student_id, name)
                elif student_type.strip() == 'PG':
                    self.students[student_id] = PostgraduateStudent(student_id, name, mode[0].strip())

    def read_results(self, file_name):
        # Method to read course results from a file.
        with open(file_name, 'r') as file:
            # this is to check if the file is empty and notify the user.
            if file.read().strip() == '':
                print("Error: The result file is empty.")
                return
            file.seek(0)  # resetting the file pointer to the start
            for line in file:
                # splitting each line into different components.
                row = line.split(',')
                student_id, course_id, score = row[0], row[1].strip(), row[2].strip()
                # checking for valid student IDs to ensure they begin with S.
                if not student_id.startswith('S'):
                    print(f"Error: Invalid student ID {student_id}. Student ID must start with 'S'.")
                    return
                # checking for valid course ID as the course is either cosc, isys, orr math.
                if not (course_id.startswith('COSC') or course_id.startswith('ISYS') or course_id.startswith('MATH')):
                    print(f"Error: Invalid course ID {course_id}. Course ID must start with 'COSC', 'ISYS', or 'MATH'.")
                    return
                # checking if score is empty.
                if score == '':
                    score = '--'
                else:
                    try:
                        score = float(score)  #converting the score to a float so it can be evaluated.
                    except ValueError:
                        print(f"Error: Invalid score value for student {student_id} in course {course_id}. The score must be a valid number.")
                        return
                # adding the score to the student's courses and to the course.
                self.students[student_id].courses[course_id] = score
                self.courses[course_id].add_student_score(score)

    def display_course_info(self):
        # Method to print all the course information. utilizing string manipulating to arrange them in the best way possible
        print('---------------------------------------------------------------------------------------------------')
        print('CourseID'.ljust(10)
              + 'Course Name'.ljust(15)
              + 'Credit'.ljust(7)
              + 'Nfinish'.ljust(8)
              + 'Nongoing'.ljust(9)
              + 'Average'.ljust(8)) #adjusting the arrangement of the variables as they should appear on the table output
        print('---------------------------------------------------------------------------------------------------')        
        for course in self.courses.values():
            print(course.id.ljust(10)
                  + course.name.ljust(15)
                  + str(course.credit).ljust(7)
                  + str(course.students_finished).ljust(8)
                  + str(course.students_ongoing).ljust(9)
                  + '{:.2f}'.format(course.average_score()).ljust(8))

    def display_course_summary(self): #self-explanatory, this functions displays course summary and meets the Credit requirement
        #it also displays the hardest core and elective courses and the average scores in it
        print('\nCOURSE SUMMARY')
        core_courses = [course for course in self.courses.values() if isinstance(course, CoreCourse)]
        elective_courses = [course for course in self.courses.values() if isinstance(course, ElectiveCourse)]
        if core_courses:
            most_difficult_course = min(core_courses, key=lambda course: course.average_score())
            print(f"The most difficult core course is {most_difficult_course.id} with an average score of {most_difficult_course.average_score():.2f}.")
        if elective_courses:
            most_difficult_elective = min(elective_courses, key=lambda course: course.average_score())
            print(f"The most difficult elective course is {most_difficult_elective.id} with an average score of {most_difficult_elective.average_score():.2f}.")
    def display_results(self):
        #this displays the course information and the student information
        #ignore the function name, it was something I had made and was fairly intertwined with the whole functionality of the program that I
        #felt it would be complicated to change it
        print('COURSE INFORMATION')
        self.display_course_info()
        self.display_course_summary()
        print('\nSTUDENT INFORMATION')
        self.display_student_info()
        self.display_student_summary()
    def display_actual_results(self): #this displays the results and the summary
        #i have called quite a few methods to calculate the actual
        #scores
        course_ids = sorted(self.courses.keys())
        student_ids = sorted(self.students.keys())
        print('RESULTS')
        print('student_id'.ljust(15), ', '.join([id.ljust(10) for id in course_ids])) #string manipulation to ensure good formatting
        for student_id in student_ids:
            scores = [str(self.students[student_id].courses.get(course_id, '')).ljust(10) for course_id in course_ids]
            print(student_id.ljust(15), ', '.join(scores))
        print('\nRESULTS SUMMARY')
        print('There are', len(self.students), 'students and', len(self.courses), 'courses.') #this is the basic credit level requirements 
        total_scores = 0
        passed_scores = 0
        for student in self.students.values():
            for score in student.courses.values():
                if score != '--': #skips course if there is -- present
                    total_scores += 1
                    if score >= 49.5:
                        passed_scores += 1
        pass_rate = 100 * passed_scores / total_scores if total_scores > 0 else 0
        print('The average pass rate is {:.2f}%'.format(pass_rate)) #average pass rate printed out
    def display_student_info(self):
        #this prints out all the details of the student includeing WGPA meeting the HD level requirements
        #the strings are manipulated to ensure good formatting
        print('---------------------------------------------------------------------------------------------------')
        print('StudentID'.ljust(10)
              + 'Name'.ljust(15)
              + 'Type'.ljust(5)
              + 'Mode'.ljust(5)
              + 'GPA(100)'.ljust(9)
              + 'GPA(4)'.ljust(6)
              + 'WGPA(4)'.ljust(8)
              + 'Nfinish'.ljust(8)
              + 'Nongoing'.ljust(9))
        print('---------------------------------------------------------------------------------------------------')
        pg_students = [student for student in self.students.values() if isinstance(student, PostgraduateStudent)] #calling the postgraduate student and undergrad student classes
        ug_students = [student for student in self.students.values() if isinstance(student, UndergraduateStudent)]
        for student in pg_students:
            print(student.id.ljust(10)
                  + student.name.ljust(15)
                  + 'PG'.ljust(5)
                  + student.mode.ljust(5)
                  + '{:.2f}'.format(student.average_score_100()).ljust(9)
                  + '{:.2f}'.format(student.average_score_4()).ljust(6)
                  + '{:.2f}'.format(student.weighted_gpa_4(self.courses)).ljust(8)
                  + str(student.number_courses_finished()).ljust(8)
                  + str(student.number_courses_ongoing()).ljust(9))
        print('---------------------------------------------------------------------------------------------------')
        for student in ug_students:
            print(student.id.ljust(10)
                  + student.name.ljust(15)
                  + 'UG'.ljust(5)
                  + 'FT'.ljust(5)
                  + '{:.2f}'.format(student.average_score_100()).ljust(9)
                  + '{:.2f}'.format(student.average_score_4()).ljust(6)
                  + '{:.2f}'.format(student.weighted_gpa_4(self.courses)).ljust(8)
                  + str(student.number_courses_finished()).ljust(8)
                  + str(student.number_courses_ongoing()).ljust(9))
    def display_student_summary(self):
        print('\nSTUDENT SUMMARY') #this prints out the best ug and pg student scores
        #this is for prrinting out the best student with the best wgpa score
        pg_students = [student for student in self.students.values() if isinstance(student, PostgraduateStudent)]
        ug_students = [student for student in self.students.values() if isinstance(student, UndergraduateStudent)]        
        if pg_students:
            best_pg_student = max(pg_students, key=lambda student: student.weighted_gpa_4(self.courses))
            print(f"The best PG student is {best_pg_student.id} with a WGPA score of {best_pg_student.weighted_gpa_4(self.courses):.2f}.")        
        if ug_students:
            best_ug_student = max(ug_students, key=lambda student: student.weighted_gpa_4(self.courses))
            print(f"The best UG student is {best_ug_student.id} with a WGPA score of {best_ug_student.weighted_gpa_4(self.courses):.2f}.")
def custom_print(*args, **kwargs): #this was to write into the reports.txt file which is challenging and is still not working
    #apologies for the inconvenience in the code, it was initially working which is why I have kept the code block and moved to the next distinction level as I thought this was working
    kwargs.pop('file', None) 
    print(*args, file=report_file, **kwargs)
def main():
    print("Name: Amay Viswanathan Iyer")
    print("Student ID: s3970066")
    print("Highest Level Attempted: HD")
    print("Notes: the reports.txt does not correctly write the outputs.")
    print("Additional Notes: enter the valid courses, students, and results file names and all the necessary tables will be output.")
    print("")
    try: #all of the input validation and file reading occurs between this main method and the read file functions
        #the user is prompted persistently until a valid file name is entered
        global report_file
        report_file = open('reports.txt', 'w') #this code block does not correctly write the outputs
        results = Results()
        while True:
            try:
                course_file = input("Enter course file name (or 'q' to quit): ") #i added the press q to quit as a debugging measure but it was useful for when
                #i had saved the program in a folder without the correct files
                if course_file.lower() == 'q':
                    print("Quitting the application.")
                    return
                results.read_courses(course_file)
                break
            except FileNotFoundError:
                print(f"The file {course_file} was not found. Please check the course file name and try again.")
        while True:
            try:
                student_file = input("Enter student file name (or 'q' to quit): ")
                if student_file.lower() == 'q':
                    print("Quitting the application.")
                    return
                results.read_students(student_file)
                break
            except FileNotFoundError:
                print(f"The file {student_file} was not found. Please check the student file name and try again.")
        while True:
            try:
                results_file = input("Enter results file name (or 'q' to quit): ")
                if results_file.lower() == 'q':
                    print("Quitting the application.")
                    return
                results.read_results(results_file)
                break
            except FileNotFoundError:
                print(f"The file {results_file} was not found. Please check the results file name and try again.")
        results.display_results()
        results.display_actual_results()
        results.display_course_summary()
    except Exception as e:
        print(f"An unexpected error occurred: {e}") #this occurs when a correct file is entered but the file is unable to be read by the program
    finally:
        report_file.close()
if __name__ == '__main__':
    main()
