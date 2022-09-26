num_list = [1, 2, 3]

even_list: str = []
i: int = 0

while i < len(num_list):
    if num_list[i] % 2 == 0:
        even_list.append(num_list[i])
    i += 1
    
print(even_list)