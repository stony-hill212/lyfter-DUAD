-- SQLite
DROP TABLE IF EXISTS VehicleModels;

CREATE TABLE IF NOT EXISTS VehicleModels (
    ModelID INTEGER PRIMARY KEY,
    Make TEXT,
    Model TEXT
);

DROP TABLE IF EXISTS Vehicles;

CREATE TABLE IF NOT EXISTS Vehicles (
    VIN TEXT PRIMARY KEY,
    ModelID INTEGER,
    Year INTEGER,
    Color TEXT,
    FOREIGN KEY (ModelID) REFERENCES VehicleModels(ModelID)
);

DROP TABLE IF EXISTS Owners;

CREATE TABLE IF NOT EXISTS Owners (
    OwnerID INTEGER PRIMARY KEY,
    OwnerName TEXT,
    OwnerPhone TEXT
);

DROP TABLE IF EXISTS VehicleOwners;

CREATE TABLE IF NOT EXISTS VehicleOwners (
    VIN TEXT,
    OwnerID INTEGER,
    PRIMARY KEY (VIN, OwnerID),
    FOREIGN KEY (VIN) REFERENCES Vehicles(VIN),
    FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID)
);

DROP TABLE IF EXISTS InsuranceCompanies;

CREATE TABLE IF NOT EXISTS InsuranceCompanies (
    CompanyID INTEGER PRIMARY KEY,
    CompanyName TEXT
);

DROP TABLE IF EXISTS InsurancePolicies;

CREATE TABLE IF NOT EXISTS InsurancePolicies (
    PolicyID TEXT PRIMARY KEY,
    CompanyID INTEGER,
    FOREIGN KEY (CompanyID) REFERENCES InsuranceCompanies(CompanyID)
);

DROP TABLE IF EXISTS VehiclePolicies;

CREATE TABLE IF NOT EXISTS VehiclePolicies (
    VIN TEXT,
    PolicyID TEXT,
    PRIMARY KEY (VIN, PolicyID),
    FOREIGN KEY (VIN) REFERENCES Vehicles(VIN),
    FOREIGN KEY (PolicyID) REFERENCES InsurancePolicies(PolicyID)
);

INSERT INTO VehicleModels VALUES (1, 'Honda', 'Accord');
INSERT INTO VehicleModels VALUES (2, 'Honda', 'CR-V');
INSERT INTO VehicleModels VALUES (3, 'Chevrolet', 'Volt');

INSERT INTO Vehicles VALUES ('1HGCM82633A', 1, 2003, 'Silver');
INSERT INTO Vehicles VALUES ('5J6RM4H79EL', 2, 2014, 'Blue');
INSERT INTO Vehicles VALUES ('1G1RA6EH1FU', 3, 2015, 'Red');

INSERT INTO Owners VALUES (101, 'Alice', '123-456-7890');
INSERT INTO Owners VALUES (102, 'Bobby', '987-654-3210');
INSERT INTO Owners VALUES (103, 'Claire', '555-123-3333');
INSERT INTO Owners VALUES (104, 'Pete', '111-222-3333');

INSERT INTO VehicleOwners VALUES ('1HGCM82633A', 101);
INSERT INTO VehicleOwners VALUES ('1HGCM82633A', 102);
INSERT INTO VehicleOwners VALUES ('5J6RM4H79EL', 103);
INSERT INTO VehicleOwners VALUES ('1G1RA6EH1FU', 104);

INSERT INTO InsuranceCompanies VALUES (1, 'ABC Insurance');
INSERT INTO InsuranceCompanies VALUES (2, 'XYZ Insurance');
INSERT INTO InsuranceCompanies VALUES (3, 'DEF Insurance');
INSERT INTO InsuranceCompanies VALUES (4, 'GHI Insurance');

INSERT INTO InsurancePolicies VALUES ('POL12345', 1);
INSERT INTO InsurancePolicies VALUES ('POL54321', 2);
INSERT INTO InsurancePolicies VALUES ('POL67890', 3);
INSERT INTO InsurancePolicies VALUES ('POL98765', 4);

INSERT INTO VehiclePolicies VALUES ('1HGCM82633A', 'POL12345');
INSERT INTO VehiclePolicies VALUES ('1HGCM82633A', 'POL54321');
INSERT INTO VehiclePolicies VALUES ('5J6RM4H79EL', 'POL67890');
INSERT INTO VehiclePolicies VALUES ('1G1RA6EH1FU', 'POL98765');

SELECT * FROM VehicleModels;
SELECT * FROM Vehicles;
SELECT * FROM Owners;
SELECT * FROM VehicleOwners;
SELECT * FROM InsuranceCompanies;
SELECT * FROM InsurancePolicies;
SELECT * FROM VehiclePolicies;

SELECT * FROM VehicleOwners;

SELECT * FROM InsurancePolicies;
