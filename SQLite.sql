create TABLE Notes
(ID INT PRIMARY key,
 Note TEXT UNIQUE NOT NULL,
 TimeOfCreation DATETIME NOT NULL,
 ProgressMade REAL DEFAULT 0 CHECK( ProgressMade>0 AND ProgressMade < 1),
 Status TEXT DEFAULT 'started' CHECK( Status = 'started' OR Status = 'accepted' or Status = 'canceled'))