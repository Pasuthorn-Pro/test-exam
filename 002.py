def find_repeated_substrings(s: str) -> list:
    repeated_substrings = []
    string_length = len(s)

    # Iterate over all possible substring lengths
    for length in range(2, string_length + 1):
        seen = set() # Create new set to  
        for i in range(string_length - length + 1):
            substring = s[i:i + length]
            if substring in seen:
                # Add substring if it is repeated and not already in the result list
                if substring not in repeated_substrings:
                    repeated_substrings.append(substring)
            else:
                seen.add(substring)

    return repeated_substrings

print(find_repeated_substrings("banana"))  # Output: ['an', 'ana', 'na']
print(find_repeated_substrings("abcdefg"))  # Output: []
print(find_repeated_substrings("abcabcabc"))  # Output: ['ab', 'abc', 'abca', 'abcab', 'abcabc', 'bc', 'bca', 'bcab','bcabc', 'ca', 'cab', 'cabc']
print(find_repeated_substrings("aaaa"))  # Output: ['aa', 'aaa']