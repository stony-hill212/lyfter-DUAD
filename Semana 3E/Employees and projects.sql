-- SQLite
DROP TABLE IF EXISTS Departments;

CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT,
    DepartmentPhone TEXT
);

DROP TABLE IF EXISTS Employees;

CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY,
    EmployeeName TEXT,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

DROP TABLE IF EXISTS Projects;

CREATE TABLE IF NOT EXISTS Projects (
    ProJectID TEXT PRIMARY KEY,
    ProjectName TEXT,
    projectBudget REAL 
);

DROP TABLE IF EXISTS EmployeeProjects;

CREATE TABLE IF NOT EXISTS EmployeeProjects (
    EmployeeID INTEGER,
    ProjectID TEXT,
    PRIMARY KEY (EmployeeID, ProjectID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

INSERT INTO Departments VALUES (1, 'IT', '2222-2222');
INSERT INTO Departments VALUES (2, 'Marketing', '1111-1111');

INSERT INTO Employees VALUES (201, 'Ana Rivera', 1);
INSERT INTO Employees VALUES (202, 'Luis Mendez', 2);

INSERT INTO Projects VALUES ('P001', 'Web App', 5000);
INSERT INTO Projects VALUES ('P002', 'API REST', 25000);
INSERT INTO Projects VALUES ('P003', 'Campaña TV', 30000);

INSERT INTO EmployeeProjects VALUES (201, 'P001');
INSERT INTO EmployeeProjects VALUES (201, 'P002');
INSERT INTO EmployeeProjects VALUES (202, 'P003');

SELECT * FROM Departments;
SELECT * FROM Employees;
SELECT * FROM Projects;
SELECT * FROM EmployeeProjects;