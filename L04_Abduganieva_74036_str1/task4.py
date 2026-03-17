#  Ominakavsar Abduganieva, ID: 74026
import re

student_records = [
    "Name: Alisher Navoiy, student ID: 71111, Email: alisher.n@university.uz",
    "Name: Nodira Begim, student ID: 79999, Email: nodira.b@university.uz",
    "Name: Temur Malik, student ID: 71245, Email: temur.m@university.uz",
    "Name: Bibixonim Azizova, student ID: 77890, Email: bibi.a@university.uz",
    "Name: Jaloliddin Manguberdi, student ID: 74321, Email: jalol.m@university.uz",
    "Name: Gulnara Islomova, student ID: 77777, Email: g.islomova@university.uz"
]

my_id_MA = "74026"
my_record_MA = f"Name: Ominakavsar Abduganieva, student ID: {my_id_MA}, Email: okavsar9@university.uz"
student_records.append(my_record_MA)

extracted_ids_MA = []

for record in student_records:
    match_obj = re.search(r"7\d{4}", record)
    if match_obj:
        extracted_ids_MA.append(match_obj.group())

print("--- Student Record List ---")
for record in student_records:
    print(record)

print("\n--- Extracted Student IDs ---")
print(extracted_ids_MA)