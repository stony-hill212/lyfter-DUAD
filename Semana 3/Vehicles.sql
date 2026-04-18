-- SQLite
DROP TABLE IF EXISTS Owners;

CREATE TABLE IF NOT EXISTS Owners (
    OwnerID INTEGER PRIMARY KEY,
    OwnerName TEXT,
    OwnerPhone TEXT
);

DROP TABLE IF EXISTS Vehicles;

CREATE TABLE IF NOT EXISTS Vehicles (
    VIN TEXT PRIMARY KEY,
    Make TEXT,
    Model TEXT,
    Year INTEGER,
    Color TEXT
);

DROP TABLE IF EXISTS InsurancePolicies;

CREATE TABLE IF NOT EXISTS InsurancePolicies (
    PolicyID TEXT PRIMARY KEY,
    CompanyName TEXT,
    VIN TEXT,
    FOREIGN KEY (VIN) REFERENCES Vehicles(VIN)
);

DROP TABLE IF EXISTS VehicleOwners;

CREATE TABLE IF NOT EXISTS VehicleOwners (
    VIN TEXT,
    OwnerID INTEGER,
    PRIMARY KEY (VIN, OwnerID)
    FOREIGN KEY (VIN) REFERENCES Vehicles(VIN),
    FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID)
);

INSERT INTO Owners VALUES (101, 'Alice', '123-456-7890');
INSERT INTO Owners VALUES (102, 'Bobby', '987-654-3210');
INSERT INTO Owners VALUES (103, 'Claire', '555-123-3333');
INSERT INTO Owners VALUES (104, 'Pete', '111-222-3333');

INSERT INTO Vehicles VALUES ('1HGCM82633A', 'Honda', 'Accord', 2003, 'Silver');
INSERT INTO Vehicles VALUES ('5J6RM4H79EL', 'Honda', 'CR-V', 2014, 'Blue');
INSERT INTO Vehicles VALUES ('1G1RA6EH1FU', 'Chevrolet', 'Volt', 2015, 'Red');

INSERT INTO VehicleOwners VALUES ('1HGCM82633A', 101);
INSERT INTO VehicleOwners VALUES ('1HGCM82633A', 102);
INSERT INTO VehicleOwners VALUES ('5J6RM4H79EL', 103);
INSERT INTO VehicleOwners VALUES ('1G1RA6EH1FU', 104);

INSERT INTO InsurancePolicies VALUES ('POL12345', 'ABC Insurance', '1HGCM82633A');
INSERT INTO InsurancePolicies VALUES ('POL54321', 'XYZ Insurance', '1HGCM82633A');
INSERT INTO InsurancePolicies VALUES ('POL67890', 'DEF Insurance', '5J6RM4H79EL');
INSERT INTO InsurancePolicies VALUES ('POL98675', 'GHI Insurance', '1G1RA6EH1FU');

SELECT * FROM Owners;

SELECT * FROM Vehicles;

SELECT * FROM VehicleOwners;

SELECT * FROM InsurancePolicies;
