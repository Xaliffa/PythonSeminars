class1_amount = int(input('Enter the number of students of class 1: '))
class2_amount = int(input('Enter the number of students of class 2: '))
class3_amount = int(input('Enter the number of students of class 3: '))

# print(math.ceil(class1_amount/2) + math.ceil(class2_amount/2) + math.ceil(class3_amount/2))
print(f"It will be need {(class1_amount + class1_amount%2 + class2_amount + class2_amount%2 + class3_amount + class3_amount%2) // 2} tables")