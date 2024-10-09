# ScholaFlex - A Dynamic Student Management System

Welcome to **ScholaFlex**, a powerful, object-oriented, Python-based application designed to efficiently manage student, course, and result information for a school or university system. The name **ScholaFlex** represents a flexible, dynamic solution for educational data management. This repository contains code that demonstrates the integration of various computer science concepts, algorithmic approaches, and problem-solving skills, all implemented with a focus on clean object-oriented design.

## Table of Contents
- [About the Project](#about-the-project)
- [Class Diagram Overview](#class-diagram-overview)
- [Features and Functionalities](#features-and-functionalities)
- [Key Computer Science Concepts](#key-computer-science-concepts)
- [Getting Started](#getting-started)
- [Usage Examples](#usage-examples)
- [Design Decisions](#design-decisions)
- [Real-World Problem Solving](#real-world-problem-solving)
- [Future Improvements](#future-improvements)
- [Contact](#contact)

## About the Project
**ScholaFlex** is a comprehensive student management application built to simplify the administrative tasks involved in managing courses, students, and results. By leveraging object-oriented principles, **ScholaFlex** provides a structured way to handle complex relationships between students, courses, and results. The primary objective of this project is to read data from multiple files and manage student records, course details, and result information, allowing easy access, modification, and display of these details.

This project aims to address the common challenges faced by educational institutions, such as managing course enrollments, keeping track of student performance, and generating insightful analytics for administrators. By automating these processes, **ScholaFlex** reduces administrative overhead and provides timely, accurate data for better decision-making.

The project consists of three main classes: **Course**, **Student**, and **Results**. These classes work together to achieve the goal of dynamically managing and processing course enrollments, student progress, and grade information in an efficient and modular manner.

## Class Diagram Overview
The class diagram forms the backbone of **ScholaFlex**, demonstrating the relationships between the key classes: **Course**, **Student**, and **Results**. Each of these classes plays a crucial role in managing different aspects of the educational system.

![class_diagram](https://github.com/user-attachments/assets/7e31e0aa-7725-4943-ab17-b3f852e1ed48)


### Classes and Their Relationships
1. **Course Class**: Represents individual courses.
   - **Attributes**:
     - `id` (unique identifier for the course)
     - `name` (name of the course)
     - `credit` (credit points for the course)
     - `students_finished` (number of students who have completed the course)
     - `students_ongoing` (number of students currently enrolled)
     - `total_score` (accumulated score for statistical calculations)
   - **Methods**:
     - `add_student_score(score: float)`: Adds a student's score to the course total.
     - `average_score() -> float`: Calculates and returns the average score of the course.
   - **Inheritance**: Extended by **CoreCourse** and **ElectiveCourse** to provide specialized behavior for different types of courses.

2. **Student Class**: Manages details related to students.
   - **Attributes**:
     - `id` (unique identifier for the student)
     - `name` (name of the student)
     - `student_type` (undergraduate or postgraduate)
     - `courses` (dictionary mapping course IDs to scores)
     - `mode` (optional; enrollment mode for postgraduate students)
   - **Methods**:
     - `add_course(course_id: str, score: float)`: Adds a course and score to the student's record.
     - `calculate_gpa() -> tuple[float, float]`: Calculates and returns the GPA on both a 100-point scale and a 4-point scale.
     - `number_courses_finished() -> int`: Returns the number of courses completed by the student.
     - `number_courses_ongoing() -> int`: Returns the number of courses the student is currently taking.
     - `satisfies_enrollment() -> bool`: Checks if the student satisfies the enrollment requirements.
     - `weighted_gpa_4(courses: dict[str, Course]) -> float`: Calculates the weighted GPA based on course credits.
     - `average_score_100() -> float`: Returns the average score on a 100-point scale.
     - `average_score_4() -> float`: Returns the average score on a 4-point scale.
   - **Inheritance**: Extended by **UndergraduateStudent** and **PostgraduateStudent** to handle specific enrollment requirements.

3. **Results Class**: Handles course and student data, processes scores, and displays information.
   - **Attributes**:
     - `students` (dictionary of student objects)
     - `courses` (dictionary of course objects)
   - **Methods**:
     - `read_courses(file_name: str)`: Reads course information from a file and initializes course objects.
     - `read_students(file_name: str)`: Reads student information from a file and initializes student objects.
     - `read_results(file_name: str)`: Reads results from a file and updates course and student objects accordingly.
     - `display_course_info()`: Displays detailed information about each course.
     - `display_course_summary()`: Displays a summary of courses including average scores.
     - `display_results()`: Displays the results of all students in a formatted table.
     - `display_actual_results()`: Displays detailed result information, including ongoing courses.
     - `display_student_info()`: Displays detailed information about each student.
     - `display_student_summary()`: Displays a summary of student achievements.

The class diagram visually maps the architecture of the solution, providing a clear understanding of how data flows between the components and how responsibilities are distributed.

## Features and Functionalities
1. **Course Management**: Handles details about core and elective courses, including course type, credit points, and statistics such as the average score, number of students completed, and students currently enrolled.
   - **Core Courses** are mandatory and offered in all semesters.
   - **Elective Courses** are optional and may be offered in specific semesters.

2. **Student Information System**: Manages undergraduate and postgraduate student details, checks enrollment requirements, calculates GPA, and keeps track of course completion.
   - **Undergraduate Students** must enroll in a minimum of 4 courses and are always full-time.
   - **Postgraduate Students** can enroll part-time or full-time, with specific enrollment requirements.

3. **Result Processing**: Reads and processes course and student result data, calculates pass rates, and generates summary reports.
   - Computes **weighted GPAs** to reflect the importance of credit-heavy courses.
   - Displays **pass rates** to provide insights into course difficulty and student performance.

4. **Data Input and Output**: Reads data from external files (`results.txt`, `courses.txt`, `students.txt`) and outputs summary tables for courses and students in a user-friendly format. The output is designed to be clear and informative for both administrators and academic staff.

5. **Error Handling**: Implements custom exceptions to handle file issues, data format errors, and missing information. This ensures that the program runs smoothly and provides informative error messages when issues arise.

## Key Computer Science Concepts
1. **Object-Oriented Programming (OOP)**: The project demonstrates the core principles of OOP—**encapsulation**, **inheritance**, and **polymorphism**. The use of specialized classes such as `CoreCourse`, `ElectiveCourse`, `UndergraduateStudent`, and `PostgraduateStudent` highlights how OOP can be used to model real-world entities and their interactions.

2. **Encapsulation and Abstraction**: Each class encapsulates attributes and methods relevant to a specific entity, like courses or students, making the code modular and easier to maintain. Complex operations like GPA calculation and enrollment checks are abstracted away from the user, ensuring ease of use and a clean interface.

3. **Polymorphism**: Through method overriding, specialized subclasses like `UndergraduateStudent` and `PostgraduateStudent` modify and extend the behavior defined in the `Student` class. This allows for flexible and reusable code that can easily adapt to changes in business logic.

4. **Algorithm Design**: The solution includes algorithms for calculating **GPA**, **pass rate**, and **weighted average scores**. These algorithms ensure efficient processing of student data, provide insightful metrics for academic progress, and identify areas where students might need additional support.

5. **Data Structures**: The project makes extensive use of Python dictionaries and lists to efficiently store and access students and courses based on their unique IDs. This choice of data structure ensures fast lookups and efficient management of the relationships between students and courses.

6. **File Handling**: Python's file handling is used to read and parse data from multiple input files. This makes it easy to work with different datasets, enabling flexibility in testing and updating data without modifying the underlying code.

7. **Error Handling**: Custom exceptions are employed to handle scenarios such as missing data, incorrect file formats, and invalid entries. This robustness is crucial in real-world applications where data quality can vary significantly.

## Getting Started
### Prerequisites
- Python 3.8 or higher

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/reyiyama/scholaflex.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ScholaFlex
   ```
3. Run the application with data files as arguments:
   ```bash
   python my_school.py results.txt courses.txt students.txt
   ```

## Usage Examples
To understand how to use **ScholaFlex**, refer to the sample data files provided in this repository: `courses.txt`, `results.txt`, and `students.txt`.

1. **Display Course Summary**: The course summary includes details about each course, such as the average score, the number of students who completed the course, and the number of ongoing enrollments. This information helps administrators understand course popularity and difficulty.

2. **Student Information**: Analyze individual students' progress by calculating their GPA, tracking completed courses, and generating performance reports. This feature helps academic advisors provide tailored support to students who may need help.

3. **Result Analysis**: Compute overall pass rates, display ongoing versus completed courses, and identify the most challenging subjects based on pass rates. This feature is particularly useful for curriculum planners and instructors to assess course effectiveness.

## Design Decisions
- **Class Hierarchies**: The use of inheritance in the `Student` and `Course` classes allows for specific behaviors for different types of students (undergraduate vs. postgraduate) and courses (core vs. elective). This approach simplifies the code by avoiding repetition and making it easier to extend functionality in the future.

- **File Input**: The decision to use text files (`courses.txt`, `students.txt`, `results.txt`) for data input provides flexibility during development and testing. Users can easily modify data without changing the source code, making it easy to experiment with different scenarios.

- **Method Choices**: Methods like `calculate_gpa()` and `weighted_gpa_4()` were implemented to showcase different ways of handling academic performance metrics—using both a simple 100-point scale and a GPA weighted by course credits. This dual approach provides a more comprehensive view of student performance.

- **Student Enrollment**: Enrollment checks were implemented to ensure students meet the criteria for either full-time or part-time status. This feature reflects real-world administrative policies and helps ensure data integrity.

## Real-World Problem Solving
**ScholaFlex** addresses a common problem faced by educational institutions: managing student records, course enrollments, and result processing in an efficient and scalable manner. In real-world educational environments, the need to handle a growing number of students and courses while ensuring data consistency is paramount. **ScholaFlex** solves these challenges through:

1. **Automated Data Processing**: By reading student, course, and result data from files, **ScholaFlex** automates what is traditionally a manual process. This saves significant time for administrators and reduces the risk of human error in data entry.

2. **Performance Tracking**: The system calculates GPAs, pass rates, and other metrics that help academic staff track the performance of students and courses. Identifying struggling students or particularly challenging courses early allows for proactive interventions to improve learning outcomes.

3. **Scalable Design**: The use of OOP principles ensures that the system can easily scale as the number of students and courses increases. For example, adding new student types or course formats can be done by extending existing classes, making the system adaptable to future requirements.

4. **Insightful Analytics**: With features like weighted GPA and pass rate calculations, **ScholaFlex** provides valuable insights into academic performance that can inform curriculum adjustments, teaching strategies, and resource allocation.

5. **User-Friendly Outputs**: The system provides detailed, formatted tables for courses and student results, which can be easily interpreted by users who may not be technically inclined. This makes the tool accessible to academic staff, students, and administrators alike.

6. **Data Consistency and Integrity**: By managing student and course records in a systematic way, **ScholaFlex** ensures that data consistency is maintained. This is crucial for preventing discrepancies that could affect a student's academic record or the institution's reporting accuracy.

7. **Flexible Course Management**: By distinguishing between core and elective courses, **ScholaFlex** offers flexible course management tailored to different academic programs. This allows educational institutions to define course structures that meet their specific needs, providing a modular approach to curriculum design.

8. **Real-Time Student Support**: The student performance tracking and enrollment validation features provide timely insights to academic advisors, allowing them to intervene early when a student is at risk of underperforming or not meeting enrollment requirements.

9. **Improved Administrative Efficiency**: Administrative staff benefit from automated result processing and course summary generation, reducing paperwork and ensuring that critical academic data is available when needed. This directly addresses the pain points associated with managing large volumes of student data.

10. **Academic Planning**: The analysis of pass rates and the identification of the most challenging subjects help educators understand which courses may need revision or additional support. This leads to more effective academic planning and an improved learning experience for students.

## Future Improvements
- **User Interface**: Develop a graphical user interface (GUI) to make the application more accessible for non-technical users, enabling them to interact with the system through buttons and visual elements rather than command-line instructions.

- **Database Integration**: Instead of relying on text files, integrating a database like SQLite or PostgreSQL would improve data persistence, scalability, and security, making the application suitable for larger educational institutions.

- **Unit Testing**: Implement unit tests to verify the correctness of the methods and ensure the reliability of the system. This will make future development easier by ensuring that changes do not introduce regressions.

- **Additional Analytics**: Add more in-depth analytics, such as tracking a student's performance over multiple semesters, identifying at-risk students, or generating statistical insights about course popularity and average grades over time.

- **Role-Based Access Control**: Implement a role-based access system where different users (e.g., students, teachers, administrators) have different levels of access to the data and functionalities, improving security and data privacy.

- **Cloud Integration**: Integrate cloud services to enable access from anywhere, making it easier for administrators, students, and teachers to use the system remotely. Cloud integration could also facilitate automatic backups and improve data availability.

- **API Development**: Develop an API that allows external systems (such as student portals, learning management systems, or mobile applications) to interact with **ScholaFlex**, making it more versatile and increasing its potential integrations.

## Contact
For more information or collaboration inquiries, contact **Amay** via GitHub: [reyiyama](https://github.com/reyiyama).

---
Thank you for checking out **ScholaFlex**! Feel free to contribute or reach out for any improvements, questions, or feedback.
