log_file = open("log.txt", "w")

name = ["Kelly","Jason","Alice","Debra","Gordon"]
user_ID = [1,2,3,4,5]
pay_Type = ["Hourly","Salary","Salary","Hourly","Hourly"]
pay_Rate = [12,700,720,13,12]
hours_Worked = [32,40,40,19,23]
gross_Pay=[]

print ("writing File...")
log_file.write ("user_ID\tpay_Type\tpay_Rate\thours_Worked\tgross_Pay\n")
print ("name\tuser_ID\tpay_Type\tpay_Rate\thours_Worked\tgross_Pay\n")
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
	gross_pay[] = pay_rate * hours_Worked
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
