log_file = open("log.txt", "w")

name = ["Kelly","Jason","Alice","Debra","Gordon"]
user_ID = [1,2,3,4,5]
pay_Type = ["Hourly","Salary","Salary","Hourly","Hourly"]
pay_Rate1 = [(12),    (700),   (720),   (13),    (12)]
pay_Rate2 = [700, 720]
hours_Worked = (32,40,40,19,23)
gross_Pay= pay_Rate1 * hours_Worked

log_file.write("name\tuser_ID\tpay_Type\tpay_Rate1\tpay_Rate2\thours_Worked\tgross_Pay\n")

print("name\tuser_ID\tpay_Type\tpay_Rate1, pay_Rate2\thours_Worked\tgross_Pay\n")

for element in name, user_ID, pay_Type, pay_Rate1,pay_Rate2, hours_Worked, gross_Pay :
    print (element)
    
for element in gross_Pay :
    print (element is pay_Rate1 * hours_Worked:
    endif 

log_file.close()
