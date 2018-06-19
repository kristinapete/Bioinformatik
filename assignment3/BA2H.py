pattern = "AAA"
dna = "TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT"
dna = dna.split()

def FindHammingDistance(patternA, patternB):
    score = 0
    for base in range(len(patternA)):
        if patternA[base] != patternB[base]:
            score += 1
    return score

def DistanceBetweenPatternAndStrings(pattern, dna):
    k = len(pattern)
    distance = 0
    for Sequence in dna:
        HammingDistance = k+1
        for i in range(len(Sequence)-k+1):
            PatternB = Sequence[i:i+k]
            if HammingDistance > FindHammingDistance(pattern, PatternB):
                HammingDistance = FindHammingDistance(pattern, PatternB)
        distance += HammingDistance
    return distance

print(DistanceBetweenPatternAndStrings(pattern, dna))

