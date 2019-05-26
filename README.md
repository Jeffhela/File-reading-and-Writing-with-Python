# File-reading-and-Writing-with-Python


create a file with the given format, inserts five employees into that file with the following information: (20 points)

Name	ID	Pay Type	Pay Rate	Hours Worked
Kelly	1	H	12	32
Jason	2	S	700	40
Alice	3	S	720	40
Debra	4	H	13	19
Gordon	5	H	12	23


Algorithm
(1)	Open file in write mode
(2)	Type in the header row that describes each entry in each row
(3)	For i in the range 0 to 10
(1)	Generate a name, user ID, pay type, pay rate, and hours worked
(2)	Concatenate (stick together, or add up) all the generated data, while inserting a tab delimiter between successive fields.
(4) Close the file
(5) Reopen the file
(6) For each line in the file
	(1) Read it, separate its fields, print them to the user

file_handle = open(“path_to_file”, “w”)
file_handle.write(“This is a line”)
file_handle.write(“This is another line”)
file_handle.close()


b)	For the same problem, convert the algorithm from your solution into Python code. Your code should output each employee’s name, ID, pay type, pay rate, hours worked, and the calculated gross pay.  (20 points)
Each employee’s information should be printed on the same line.
Information for each employee should be printed on a separate line. 
