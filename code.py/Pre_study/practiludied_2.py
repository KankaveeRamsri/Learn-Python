import csv
def read_text():
    with open("rio2016.csv") as f :
        data = f.read()
        print(type(data))
        print(data)

def read_csv() :
    with open("rio2016.csv" , newline="") as f :
        data = csv.reader(f)
        print(type(data))
        print(data)
        for row in data :
            # print(row)
            print("{:25}: {:2} {:2} {:2} {:3}".format(row[0],row[1],row[2],row[3],int(row[1]) + int(row[2]) + int(row[3])))


# read_text()
read_csv()

def read_csv_tab():
    with open("rio2016tab.txt" , newline="") as f :
        data = csv.reader(f,delimiter="\t")
        print(type(data))
        print(data)
        for row in data :
            # print(row)
            print("{:25}: {:2} {:2} {:2} {:3}".format(row[0],row[1],row[2],row[3],int(row[1]) + int(row[2]) + int(row[3])))

# read_csv_tab()

def read_csv_header() :
    with open("rio2016_header_column.csv" , newline="") as csvfile :
        data = csv.DictReader(csvfile)
        print(type(data))
        print(data.fieldnames) #column_header
        for row in data :
            print(row["country"],row["gold"],row["silver"],row['bronze'])
        
read_csv_header()

print('---------------------------------------')

#เขียนไฟล์ csv

def demo1() :
    with open("some.csv" , "a" , newline="" , encoding="utf8") as csvfile : #encoding สำคัญ ถ้าเขียนไทย ปน Eng
        fw = csv.writer(csvfile)
        # fw.writerow(['one','two','three'])
        # fw.writerow(("lily" , "carnation" , "rose"))
        # fw.writerow(["th","Thailand","ประเทศไทย"])
        fw.writerow(["a","b","c"])



def demo2() :
    menus = [
        ["mocha" , 30 , 40 , 50],
        ["latte" , 40 , 50 , 65],
        ["espresso" , 50 , 55 , 70]
    ]
    with open("some2.csv" , "w" , newline="" , encoding="utf8") as csvfile :
        fw = csv.writer(csvfile,delimiter="|",quoting=csv.QUOTE_NONNUMERIC) #quoting = เปลี่ยนที่ไม่ใช่ตัวเลขให้มี ""
        fw.writerow(["menu" , "S" , "M" , "L"])
        fw.writerows(menus)

# demo1()
# demo2()