log_file = open("log.txt", "w")

name = ["Kelly","Jason","Alice","Debra","Gordon"]
user_ID = [1,2,3,4,5]
pay_Type = ["Hourly","Salary","Salary","Hourly","Hourly"]
pay_Rate = [12,700,720,13,12]
hours_Worked = [32,40,40,19,23]
gross_Pay=[]

log_file.write("name\tuser_ID\tpay_Type\tpay_Rate\thours_Worked\tgross_Pay\n")

print("name\tuser_ID\tpay_Type\tpay_Rate\thours_Worked\tgross_Pay\n")

for i in range(0,5):

        #set the file entry
        entry = str(name) + "\t" + str(user_ID) + "\t" + str(pay_Type) + "\t" + str(pay_Rate) + "\t" + str(hours_Worked) + "\t" + str(gross_Pay) + "\n"

        #write the file entry
        log_file.write(entry)

        print(entry,end='')

log_file.close()
