--------------------------------------------------------
-- SAM database core data
-- last update: 21/11/2021
--------------------------------------------------------

USE sam;

-- Create default groups
INSERT INTO sam.group (designation) VALUES ("Administrators");
INSERT INTO sam.group (designation) VALUES ("Users");

-- Create an administrator user with password 123
INSERT INTO user (email, firstname, psw, administrator) 
VALUES ('admin@sam.pt','Administrator', '6e68eff9ad873e8df6d25fce9282fb9bfbd3f8f6ff32a639a42963448787d88a:7e3627579e1e4304874ce442f2e50760', 1);

-- Create a test user with password 123.
INSERT INTO user (email, firstname, lastname, psw) 
VALUES ('forrest@sam.pt','Forrest','Gump', '6e68eff9ad873e8df6d25fce9282fb9bfbd3f8f6ff32a639a42963448787d88a:7e3627579e1e4304874ce442f2e50760');

-- Add default users to groups
INSERT INTO user_group (userid, groupid) VALUES (1, 1);
INSERT INTO user_group (userid, groupid) VALUES (1, 2);
INSERT INTO user_group (userid, groupid) VALUES (2, 2);

