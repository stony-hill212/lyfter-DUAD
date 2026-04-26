-- SQLite
DROP TABLE IF EXISTS Students;

CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY,
    StudentName TEXT
);

DROP TABLE IF EXISTS Instructors;

CREATE TABLE IF NOT EXISTS Instructors (
    InstructorID INTEGER PRIMARY KEY,
    InstructorName TEXT,
    InstructorEmail TEXT
);

DROP TABLE IF EXISTS Courses;

CREATE TABLE IF NOT EXISTS Courses (
    CourseCode TEXT PRIMARY KEY,
    CourseName TEXT,
    InstructorID INTEGER,
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID)
);

DROP TABLE IF EXISTS Enrollments;

CREATE TABLE IF NOT EXISTS Enrollments (
    StudentID INTEGER,
    CourseCode TEXT,
    PRIMARY KEY (StudentID, CourseCode),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseCode) REFERENCES Courses(CourseCode)
);

INSERT INTO Students VALUES (301, 'Marco Gomez');
INSERT INTO Students VALUES (302, 'Carla Ruiz');

INSERT INTO Instructors VALUES (1, 'Juan Perez', 'juan@uni.edu');
INSERT INTO Instructors VALUES (2, 'Laura Rojas', 'laura@uni.edu');

INSERT INTO Courses VALUES ('CS101', 'Python I', 1);
INSERT INTO Courses VALUES ('CS102', 'Python II', 2);

INSERT INTO Enrollments VALUES (301, 'CS101');
INSERT INTO Enrollments VALUES (301, 'CS102');
INSERT INTO Enrollments VALUES (302, 'CS101');

SELECT * FROM Students;
SELECT * FROM Instructors;
SELECT * FROM Courses;
SELECT * FROM Enrollments;