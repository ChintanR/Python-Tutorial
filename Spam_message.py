a = input("Enter any text: ")

if(("Make a lot of money" in a) or ("buy now" in a) or ("subscribe this" in a) or ("click this" in a)):
    print("This message is spam comment")
else:
    print("This message is not a spam comment")