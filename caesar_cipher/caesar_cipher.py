alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(text, shift, direction):
    display_text=[]
    display_letter=alphabet_position=0

    if direction=="decode":
        shift*=-1

    for letter in text:
        alphabet_position=alphabet.index(letter)
        display_letter=alphabet_position+shift
        
        if display_letter>25:
            display_letter-=26
        elif display_letter<0:
            display_letter+=26

        display_text.append(alphabet[display_letter])
    print(display_text)
