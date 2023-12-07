#Write to an Existing File

f = open("/Users/balast/Desktop/demofile2.txt","a") #เพิ่มข้อมูลเรื่อยๆตามจำนวนการรัน
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending :
f = open("/Users/balast/Desktop/demofile2.txt","r")
print(f.read())

print("------------------------------------------") 

# f = open("/Users/balast/Desktop/demofile3.txt","w") #เขียนทับข้อมูลเดิมที่มีอยู่แล้ว
# f.write("Woops! I have deleted the content!")
# f.close()

#open and read the file after the overwriting :
# f = open("/Users/balast/Desktop/demofile3.txt","r")
# print(f.read())

print("------------------------------------------") 

#Create a New File

# f = open("/Users/balast/Desktop/myfile.txt","x")
# f = open("/Users/balast/Desktop/myfile.txt","w")

print("------------------------------------------") 