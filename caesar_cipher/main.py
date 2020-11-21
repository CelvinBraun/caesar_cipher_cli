import caesar_cipher

end=text=direction=()
shift=0


while end!="y":

    #"menu"
    text=input("Which text?\n")
    shift=int(input("Which shift?\n"))
    direction=input("Which direction: 'encode' ord 'decode'?\n")
       
    #Call of cipher function
    caesar_cipher.cipher(text, shift, direction)

    end=input("Do you want to exit the programm?\n'y' for yes, otherwise anykey.\n\n")
    if end=="y":
        print("exit programm...")

    
    
    
    