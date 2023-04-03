max_weight = 0
min_weight = 0
num_watermelons = int(input('Num watermelons--> '))

for i in range(num_watermelons):
    weight = int(input('Weight--> '))
    if weight > max_weight:
        max_weight = min_weight = weight
    if weight < min_weight:
        min_weight = weight
        
print(max_weight, min_weight) 