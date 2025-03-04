# المشكلة:  قائمة من الأسماء مرتبة أبجديًا، ونريد إدراج اسم جديد في المكان الصحيح بحيث تبقى القائمة مرتبة.


def insert_name_sorted(names, new_name):
    index = 0
    while index < len(names) and names[index] < new_name:
        index += 1
    names.insert(index, new_name)  # إدراج الاسم في الموضع الصحيح
    return names

# تجربة الكود
names_list = ["Ahmed", "Khaled", "Mohamed", "Omar"]
new_name = "Islam"

print("قبل الإدراج:", names_list)
names_list = insert_name_sorted(names_list, new_name)
print("بعد الإدراج:", names_list)
