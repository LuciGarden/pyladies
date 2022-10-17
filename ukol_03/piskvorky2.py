def caesar_cipher(text, n):
result = ""
text = text.upper()
for i in range(len(text)):
    if text[i] == " ": result = result + " "
    else:
        c = ord(text[i]) + n
        if (c > ord("Z")): c = c - 26
        result = result + chr(c)
return result
