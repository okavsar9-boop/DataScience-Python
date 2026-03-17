#Ominakavsar Abduganieva (ID: 74026)

practice_string = "This is a string, with, more, comas! This will help, when,practicing, splitting! Hopefully!"
list_of_words_XX = practice_string.split(",")
result_a_XX = " ".join(list_of_words_XX)

result_b_XX = practice_string.replace(",", " ")

print("Result using Method A:")
print(result_a_XX)

print("\nResult using Method B:")
print(result_b_XX)

print("\nAre they identical?", result_a_XX == result_b_XX)