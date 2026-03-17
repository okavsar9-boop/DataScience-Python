# Name: Ominakavsar Abduganieva, ID: 74026
import re

string_for_pattern = "This is the beginning of a string. This is the beginning of a second sentence. And this is a number 12346."
pattern1 = "This is"
pattern2 = "this is"

match1_MA = re.match(pattern1, string_for_pattern)
match2_MA = re.match(pattern2, string_for_pattern)

print(f"Match 1 (Starts with 'This is'): {match1_MA}")
print(f"Match 2 (Starts with lowercase 'this is'): {match2_MA}") 

all_occurrences_MA = re.findall(pattern1, string_for_pattern)
print(f"All occurrences of '{pattern1}': {all_occurrences_MA}")
