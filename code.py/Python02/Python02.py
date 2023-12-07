import csv
with open('Salary.csv','r', newline = '') as csvfile :
    reader = csv.DictReader(csvfile)
    for row in reader :
        salary = float(row['Salary'])
        print("\n{} : {}".format(row['Employee'] ,row['Salary'] ))
        sick_day = int(row['Sick Days'])
        print("Sick day : {} days".format(sick_day))
        total = salary - ((salary / 20) * sick_day) 
        print("Total salary in this month : {} Baht".format(total))
        
