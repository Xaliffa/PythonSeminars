num_days = int(input('Num days--> '))
days_list = []
for i in range(num_days):
    day = int(input('Day--> '))
    days_list.append(day)
    
print(days_list)

max_len = 0
temp_count = 0
for temp in days_list:
    if temp > 0:
        temp_count +=1
    else:
        temp_count = 0
        
    if temp_count > max_len:
        max_len = temp_count
        
print(max_len) 
