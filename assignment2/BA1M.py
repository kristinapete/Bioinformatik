#BA1M
dec_number = int(45)
length = int(4)

quart_number = ""
while dec_number > 0:
    remainder = dec_number % 4
    dec_number = int(dec_number / 4)
    quart_number = str(remainder) + quart_number

for i in range(length-len(quart_number)):
    quart_number = "0" + quart_number

print("Quart_Number: ", quart_number)

def NumToPat(pattern):
    quart_text = ""
    for i in range(len(pattern)):
        if pattern[i] == "0":
            factor = "A"
        elif pattern[i] == "1":
            factor = "C"
        elif pattern[i] == "2":
            factor = "G"
        elif pattern[i] == "3":
            factor = "T"
        quart_text += factor
    return quart_text

print("Quart_Text: ", NumToPat(quart_number))
