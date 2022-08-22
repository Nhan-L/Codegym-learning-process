from tokenize import ContStr


spending = int(input("Số tiền người dùng chi ($): "))
if spending >= 150: 
    print ("Total: ", spending-50)
elif spending >= 100: 
    print ("Total: ", spending-25)
elif spending >= 75: 
    print ("Total: ", spending-15)
else:
    print ("Total: ", spending)

