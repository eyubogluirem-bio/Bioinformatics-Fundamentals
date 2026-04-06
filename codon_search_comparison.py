#LINEAR SEARCH

dna_sequence = "ATGCGTATGCGCATAGCTAGCTAGCTA"
target_codon = "CAT"

if target_codon in dna_sequence:
    print(f"YES! {target_codon} is present in the sequence.")
    print(f"First occurrence index: {dna_sequence.find(target_codon)}")
else:
    print("not found.")


#BINARY SEARCH

def binary_codon_search(sorted_codons, target_codon):
    low=0
    high=len(sorted_codons)-1
    steps=0


    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if sorted_codons[mid] < target_codon:
            low = mid + 1
        elif sorted_codons[mid] > target_codon:
            high = mid - 1
        else:
            return mid, steps

    return "not found", steps

# 1. DNA Sequence
dna_dizisi = "ATGCGTATGCGCATAGCTAGCTAGCTAATGCGTATGCGCATAGCTAGCTAGCTAATGCGTATGCGCATAGCTAGCTAGCTAATGCGTATGCGCATAGCTAGCTAGCTAATGCGTATGCGCATAGCTAGCTAGCTA"

# 2. Extracting codons using a 3-step jump
codons = [dna_sequence[i:i+3] for i in range(0, len(dna_sequence), 3)]

# 3. Sorting for Binary Search optimization
sorted_codons = sorted(codons)
print(f"Sorted Codon List: {sorted_codons}")

# 4. Search Execution
target_codon = "TAG"

result, steps = binary_codon_search(sorted_codons, target_codon)

if result == "not found":
    print(f"{target_codon} is NOT PRESENT in list.")
    print(f"Verified in {steps} search steps.")
else:
    print(f"{target_codon} is FOUND!")
    print(f"Found in {steps} steps.")

"""
Why did we use "Sorting"?
Binary Search is like finding a word in a dictionary. If the dictionary wasn't written in alphabetical order, we couldn't open a page in the middle and say "Is the word I'm looking for on the right or the left?". That's why we first sort the genetic data alphabetically with sorted().
"""
#Sorted Codon List: ['AGC', 'ATA', 'ATG', 'ATG', 'CGC', 'CGT', 'CTA', 'GCT', 'TAG']

list = ['AGC', 'ATA', 'ATG', 'ATG', 'CGC', 'CGT', 'CTA', 'GCT', 'TAG']

count = list.count('TAG')
print(f"There are {count} tane 'TAG' on the list.")



