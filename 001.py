def find_single_occurence_numbers(numbers: list) -> list:
    return [num for num in numbers if numbers.count(num) == 1]
    
print(find_single_occurence_numbers([4, 5, 6, 4, 7, 5, 8])) #Output [6, 7, 8]
print(find_single_occurence_numbers([1, 2, 2, 3 , 3, 4, 4])) #Output [1]
print(find_single_occurence_numbers([1, 2, 3, 4, 5, 6])) #Output [1, 2, 3, 4, 5, 6]
print(find_single_occurence_numbers([1, 1, 1, 1])) #Output []