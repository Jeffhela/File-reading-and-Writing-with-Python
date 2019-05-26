import random

# write to file

log_file = open ("log.txt", "w")
names = ["Kelly", "Jason", "Alice", "Debra", "Gordon"]
payType = ["Hourly", "Salary"]
payRate = [12,13]
Salary = [700, 720]
print ("writing File...")
log_file.write ("user_ID\tpayType\tpayRate\thours-Worked\n")
print ("user_ID\tpayType\tpayRate\thours_worked")
for i in range (0,6) :
        #convert i into a string
        user_ID = str (i)

        #generate names
        name = names [ int (random.random()*5)]

        #generate pay types
        payType = ("Hourly", )
        payType = ("Salary", )
        print ("Please enter payType:",)

        #Gross pay
if  employee is "Hourly" :
	gross Pay = pay_rate * hours_Worked
else:
        if employee pay_type is "salary" based
	gross pay = pay_rate

        
            

        #set the file entry
        entry = uid, + "\t" + payType, + "\t" + payRate, + "\t" + hours_Worked, + "\n"

        #write the file entry
        log_file.write(entry)

        print(entry,end='')

log_file.close()
print("File Write Completed.")
print("Please open the file on disk.")
print("-----------------------------")
