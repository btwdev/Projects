email = input("Enter The Email : ") #devshar9496@gmail.com

if email[-9:]=="gmail.com":
    if (email[-10] == "@") and (email.count("@")==1):
        if (email[0].isalpha()):
            print("Email is Valid")
        else:
            print("Wrong Email Syntax 3")
    else:
        print("Wrong Email Syntax 2")
else:
    print("Wrong Email Syntax 1")