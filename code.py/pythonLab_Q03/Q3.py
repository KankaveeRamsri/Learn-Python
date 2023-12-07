user = str(input("Enter your text : "))
count = 0
while True :
    if 'a' in user[count:] :
        new_user = user.index('a',count)
        print(new_user)
        count = new_user + 1
    else :
        break







    





    