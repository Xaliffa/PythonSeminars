# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def trans(marks_list):
    max_mark = min_mark = marks_list[0]
    for i in range (len(marks_list)):
        if marks_list[i] > max_mark:
            max_mark = marks_list[i]
        if marks_list[i] < min_mark:
            min_mark = marks_list[i]
            
    for i in range (len(marks_list)):
        if marks_list[i] == max_mark:
            marks_list[i] = min_mark
    return marks_list

num_of_marks = int(input("Enter the number of marks: "))

origin_list = []
for i in range(num_of_marks):
    origin_list.append(int(input(f"Enter the {i+1} mark: ")))
    
print(trans(origin_list))