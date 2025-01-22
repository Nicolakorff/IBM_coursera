# Create a function that takes an array of any items, removes all duplicate items (items with the same name or number-case sensitive), and returns a new array in the same sequence as the old array without any duplicates.
def removeDuplicates(arrlst):
    result = []
    for item in arrlst:
        if item not in result:
            result.append(item)
    return result 
