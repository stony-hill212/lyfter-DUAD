-- SQLite
DROP TABLE IF EXISTS Patients;

CREATE TABLE IF NOT EXISTS Patients (
    PatientID INTEGER PRIMARY KEY,
    PatientName TEXT,
    PatientPhone TEXT
);

DROP TABLE IF EXISTS Doctors;

CREATE TABLE IF NOT EXISTS Doctors (
    DoctorID INTEGER PRIMARY KEY,
    DoctorName TEXT,
    Specialty TEXT
);

DROP TABLE IF EXISTS Appointments;

CREATE TABLE IF NOT EXISTS Appointments (
    AppointmentID TEXT PRIMARY KEY,
    PatientID INTEGER,
    DoctorID INTEGER,
    Date TEXT,
    Time TEXT,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

INSERT INTO Patients VALUES (1, 'Diana Vargas', '8888-1111');
INSERT INTO Patients VALUES (2, 'Edwin Mora', '8999-2222');

INSERT INTO Doctors VALUES (1, 'Dr. Soto', 'Pediatrics');
INSERT INTO Doctors VALUES (2, 'Dr. Mora', 'Cardiology');

INSERT INTO Appointments VALUES ('A01', 1, 1, '2024-08-01', '10:00 AM');
INSERT INTO Appointments VALUES ('A02', 1, 1, '2024-08-10', '10:00 AM');
INSERT INTO Appointments VALUES ('A03', 2, 2, '2024-08-05', '01:00 PM');

SELECT * FROM Patients;
SELECT * FROM Doctors;
SELECT * FROM Appointments;
