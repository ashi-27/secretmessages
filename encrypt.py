alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
character = input("please enter a character:-")
position = alphabet.find(character)
print(position)

newposition = (position + key) % 26

print(newposition)

newchar = alphabet[newposition]

print("new character is=",newchar)


