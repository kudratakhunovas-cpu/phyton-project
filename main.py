import re

file_path = "/Users/saminakudratahunovasamina/Desktop/ALL lesson/mockdata.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()

names = []
surnames = []
file_types = []

for line in lines:
    parts = line.split("\t")
    
    if len(parts) >= 4:
        name = parts[0]
        surname = parts[1]
        file_name = parts[3]

        file_type_match = re.search(r'\.\w+$', file_name)
        file_type = file_type_match.group() if file_type_match else ""

        names.append(name)
        surnames.append(surname)
        file_types.append(file_type)

with open("/Users/saminakudratahunovasamina/Desktop/ALL lesson/name.txt", "w", encoding="utf-8") as f:
    for name in names:
        f.write(name + "\n")

with open("/Users/saminakudratahunovasamina/Desktop/ALL lesson/surname.txt", "w", encoding="utf-8") as f:
    for surname in surnames:
        f.write(surname + "\n")

with open("/Users/saminakudratahunovasamina/Desktop/ALL lesson/typeFile.txt", "w", encoding="utf-8") as f:
    for t in file_types:
        f.write(t + "\n")

print("Данные успешно записаны в файлы!")
