IL = input("Enter Latex->> ")
lenght = len(IL)
for i in range(lenght):
    if(IL[i].isalpha() and IL[i+1].isalpha() and IL[i-1] == '/'):
        Code = "/"
        while(IL[i].isalpha() and i < lenght):
            Code = Code+IL[i]
            i += 1
        print(Code)
    else:
        print(IL[i])
