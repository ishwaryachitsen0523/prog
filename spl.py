 string = input("Please Enter your Own String : ")
 special = 0
 for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    else:
        special = special + 1
        print("Total Number of Special Characters in this String :  ", special)
