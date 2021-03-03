# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# #Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text,shift_amount):
#     #Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     #e.g.
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#     for letter in text:
#         if letter == 'z':
#             letter = 'a'
#         else:
#             index = alphabet.index(letter)
#             letter = alphabet[index + shift]
#     print(f'The encrypted message is {text}')
#
#
#
# encrypt(text,shift)
import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(art.logo)



def dank_function(plain_text,shift_amount,direction_value):
    if direction == 'encode':
        cipher = ''
        for letter in plain_text:
            if letter not in (alphabet):
                cipher += letter
            else:
                index = alphabet.index(letter)
                cipher += alphabet[index + shift_amount]

        print(f"The encoded text is {cipher}")
    elif direction == 'decode':
        decipher = ''
        for letter in plain_text:
            if letter not in (alphabet):
                decipher += letter
            else:
                index = alphabet.index(letter)
                decipher = alphabet[index - shift]
        print(f'The encrypted message is {decipher}')

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    dank_function(text,shift,direction)
    go = input('Do you want to play again (y/n)?').lower()
    if go == 'y':
        continue
    else:
        break
