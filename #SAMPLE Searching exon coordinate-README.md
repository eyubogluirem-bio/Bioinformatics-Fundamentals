#Searching exon coordinate

def jump_search(sorted_list, target_coordinate):
    #Search for a specific genomic coordinate within a sorted list of exon starts.

    jump_value = 4
    start_index = 0
    list_length = len(sorted_list)

    # Jumping phase: Finding the block where the target might exist
    # min() is used to prevent IndexOutOfBounds error

    while sorted_list[int(min(jump_value, len(sorted_list))-1)] < target_coordinate:
        start_index = jump_value
        jump_value += 4

        if start_index >= len(sorted_list):
            return "not found"
        
        # Linear phase: Searching within the identified block
        
        while sorted_list[int(start_index)] < target_coordinate:
            start_index += 1

            if start_index == min(jump_value, len(sorted_list)):
                return "not found"

        if sorted_list[int(start_index)] == target_coordinate:
            return int(start_index)

        return "not found"   

exon_starts = [10500, 12200, 15400, 19800, 22100, 25600, 31000, 35400, 42000, 48500]
target_pos = 25600

print(f"exon start position list: {exon_starts}")
print(f"searching for coordinate: {target_pos} bp")

result = jump_search(exon_starts, target_pos)

if result == "not found":
    print("Result: Target coordinate is not an exon start position.") 
else:
    print(f"Result: Coordinate found at index {result}. This corresponds to Exon #{result + 1}.")
