import csv
def read_text() :
    with open("rio2016.csv" , "r" ,newline="" ) as file :
        data = file.read()
        print(type(data))
        print(data)

# read_text()

def read_csv() :
    with open("rio2016.csv" , "r" , newline="") as csvfile :
        file_reader = csv.reader(csvfile)
        for row in file_reader : 
            print("{:25}{:3}{:3}{:3}{:3}".format(row[0],row[1],row[2],row[3],int(row[1]) + int(row[2]) + int(row[3])))
          
# read_csv()

def read_csv_header() :
    with open("rio2016_header_column.csv" , "r" , newline="") as csvfile :
        file_reader = csv.DictReader(csvfile)
        print(type(file_reader))
        print(file_reader.fieldnames) #column header
        for row in file_reader :
            print(row['country'],row['gold'],row['silver'],row['bronze'])

# read_csv_header()

def read_csv_tab() :
    with open("rio2016tab.txt" , "r" , newline="") as file :
        file_reader = csv.reader(file,delimiter="\t")
        for row in file_reader:
            print(row)

# read_csv_tab() 

def write_csv() :
    with open("some.csv" , "w" , newline="", encoding="utf8") as csvfile :
        file_writer = csv.writer(csvfile)
        file_writer.writerow(['one' , 'two','three'])
        file_writer.writerow(('Ronnakrit' , 'Kankavee' , 'Puntawat'))
        file_writer.writerow(['Rattamanee' , 'Ramsri' , 'Samakkee'])
        print(file_writer)

write_csv()

def write_csv_2() :
    data = [
        ['Latte' , 30 , 40 , 50],
        ['Espresso' , 35 , 45 , 60],
        ['Americano' , 30 , 45 , 55],
        ['Mocha' , 30 , 40 , 50]
    ]
    with open("some2.csv" , "w" , newline="" , encoding="utf8") as csvfile :
        file_writer = csv.writer(csvfile)
        file_writer.writerow(['Beverage' , 'S' , 'M' , 'L'])
        file_writer.writerows(data)
        print(file_writer)

# write_csv_2()


