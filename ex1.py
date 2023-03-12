
my_string = input("enter string:")
my_string_list = my_string.split()
vowels_list = ["а", "е", "ё", "и", "о", "у", "э", "ю", "я"]
res_list =[]
for item in my_string_list:
    count = 0
    for letter in item:
        if letter in vowels_list:
            count += 1

    res_list.append(count)

flag = True
control = res_list[0]
for i in range(len(res_list)):
    if res_list[i] != control:
        flag = False

print("Парам пам-пам" if flag else  "Пам парам")




