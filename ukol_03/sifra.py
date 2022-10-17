plain_text = input("Please, insert your message to encrypt: ")
shift = int(input("Please, insert shift: "))
result = ""

for character in plain_text:
    if character == " ": 
        result = result + " "
    else: 
        x = ord(character)
        result += chr(x + shift)

print(result)

lets_continue = input("Do you want to insert another message to encrypt? ")
