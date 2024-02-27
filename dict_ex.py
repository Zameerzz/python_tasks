empty_dict = {}
print(empty_dict)

person_dict = {
    "name": "zameer",
    "age": "28",
    "occupation": "student"
}

age = person_dict["age"]
print(age)

if "occupation" in person_dict:
    print("key 'occupation' is present in person dictionary")
    
person_dict["languages"] = " 'telugu', 'hindi', 'english'"
print(person_dict)

del person_dict["age"]
print(person_dict)

for key in person_dict:
    print(key)
    
for value in person_dict.values():
    print(value)
    
    
text = "zameeeerudddsdinnnnnnnnnnnnnnnnnnnnnnnnnn"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
    
print(char_count)
