import random

#List of usable characters for the password
pass_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

#Defining two variables String and Intiger
pass_len = int()
pass_str = str()

#Seting the value of int variable to user input
check = input("Type the wanted sizeo of your password:")
pass_len = int(check)


#Generating the password using random selection from the list
for i in range(pass_len):
     pass_str = pass_str + random.choice(pass_char)
        
print("Your password is:" + " " + pass_str + "\n")

#Asking the user if he would like to get the password in binary form
question_1 = str(input("Would you like to translate your password yo binary? \n Answer with \n YES NO \n"))

################ Functions ####################
def Binary_con(bin_con_str):
    
    # Converting String to binary 
    bin_str = ''.join(format(ord(i), 'b') for i in bin_con_str)
    return bin_str
  

#Asking the user if he would like to get his password in diffrent forms
if question_1 == "YES":
    x = Binary_con(pass_str)
    print("Translated to binary:" + "" + str(x))
    input("Press ENTER to Continue")

elif question_1 == "NO":
    print("Not converting")
else:
    print("Bad input!")
    
   
