#FasterFrequentWords
dna = "CGGAAGCGAGATTCGCGTGGCGTGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGGCGTGATTCGAGCGGCGGATTCGAGATTCCGGGCGTGCGGGCGTGAAGCGCGTGGAGGAGGCGTGGCGTGCGGGAGGAGAAGCGAGAAGCCGGATTCAAGCAAGCATTCCGGCGGGAGATTCGCGTGGAGGCGTGGAGGCGTGGAGGCGTGCGGCGGGAGATTCAAGCCGGATTCGCGTGGAGAAGCGAGAAGCGCGTGCGGAAGCGAGGAGGAGAAGCATTCGCGTGATTCCGGGAGATTCAAGCATTCGCGTGCGGCGGGAGATTCAAGCGAGGAGGCGTGAAGCAAGCAAGCAAGCGCGTGGCGTGCGGCGGGAGAAGCAAGCGCGTGATTCGAGCGGGCGTGCGGAAGCGAGCGG"
k = 12
if (k > len(dna)):
    print("Falsch, k > dna!")
print("Input: ", dna)
print("Länge kmer: ", k)

def PatToNum(pattern): #wie bei BA1L
    dec_index = 0
    for i in range(len(pattern)):
        if pattern[i] == "A":
            factor = 0
        elif pattern[i] == "C":
            factor = 1
        elif pattern[i] == "G":
            factor = 2
        elif pattern[i] == "T":
            factor = 3
        dec_index += 4 ** (len(pattern) - 1 - i) * (factor + 1)
    return dec_index

def NumToPat(number):
    quart_text = ""
    for i in range(len((number))):
        if number[i] == "0":
            factor = "A"
        elif number[i] == "1":
            factor = "C"
        elif number[i] == "2":
            factor = "G"
        elif number[i] == "3":
            factor = "T"
        quart_text += factor
    return quart_text

def DecToQuart(dec_number):
    quart_number = ""
    while dec_number > 0:
        remainder = dec_number % 4
        dec_number = int(dec_number / 4)
        quart_number = str(remainder) + quart_number
    return quart_number

kmer_frequencies = []
for i in range(4**k):
    kmer_frequencies.append(0)

for i in range(len(dna)-k+1):
    pattern = dna[i:i+k]
    if len(pattern) == k:
        list_index = PatToNum(pattern)
        for j in range(k):
            list_index -=  4**(k-j-1)
        kmer_frequencies[list_index] +=1

def indices(list, value):
    return [i for i,x in enumerate(list) if x==value]

print("häufigste (Listenindex): ", indices(kmer_frequencies, max(kmer_frequencies)))

for i in indices(kmer_frequencies, max(kmer_frequencies)):
    quart_number = int(DecToQuart(i))
    for i in range(k - len(str(quart_number))):
        quart_number = "0" + str(quart_number)
    print(NumToPat(str(quart_number)), end=" ")
print()
print("mit je", max(kmer_frequencies), "mal.")
