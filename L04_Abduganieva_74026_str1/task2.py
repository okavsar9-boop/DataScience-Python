# Ominakavsar Abduganieva, ID: 74026
first_name = "Ominakavsar"
surname = "Abduganieva"
student_id = "74026"

first_name_MA = first_name.upper()
surname_MA = surname.upper()
sentence_MA = f"First name: {first_name_MA}, surname: {surname_MA}, student id: {student_id}."
print("Step 2 (Sentence):", sentence_MA)

segments_MA = [s.strip() for s in sentence_MA.split(',')]
print("Step 3 (Segments):", segments_MA)

seg1_MA = segments_MA[0].replace(" ", "-")

seg2_MA = segments_MA[1].replace(":", ">")

seg3_MA = segments_MA[2].replace("7", "seven")

final_sentence_MA = "+".join([seg1_MA, seg2_MA, seg3_MA])

print("Step 5 (Final Modified Sentence):", final_sentence_MA)