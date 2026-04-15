"""
BIOINFORMATICS TOOL: DNA Sequence Thermal Stability Sorter
---------------------------------------------------------
Problem: Sorting DNA sequences based on their GC content to determine thermal stability.
Method: Implements the Merge Sort algorithm (O(n log n)) to arrange sequences 
        in descending order of their GC-richness.
Application: Primer design, melting temperature (Tm) estimation, and stability analysis.
"""

def gc_content(seq):
    g_count = seq.count("G")
    c_count = seq.count("C")
    gc_ratio = (g_count + c_count) / len(seq)

    return gc_ratio

def merge(left, right):
    sorted_seq = []
    i=j=0
    while i < len(left) and j < len(right):
        if gc_content(left[i]) > gc_content(right[j]):
            sorted_seq.append(left[i])
            i += 1
        else:
            sorted_seq.append(right[j])
            j += 1
    #for add the other elements
    sorted_seq.extend(left[i:])
    sorted_seq.extend(right[j:])
    return sorted_seq

def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    
    mid = len(seq)//2
    left_half = merge_sort(seq[:mid])
    right_half = merge_sort(seq[mid:])

    return merge(left_half, right_half)


seq = ["ATGCGA", "CCGGCG", "ATATAT", "GGCCTA", "GGGGCC", "ATTAAA"]

sorted_seq = merge_sort(seq)
print(f"Sequenced DNA Sequences (High GC to Low): {sorted_seq}")
for s in sorted_seq:
    print(f"{s} -> GC Oranı: {gc_content(s):.2f}")
