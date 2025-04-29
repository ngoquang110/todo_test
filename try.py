from functools import reduce
from itertools import chain
numbers  = [1,2,3,4,5,6]
new_list = list(filter(lambda x : x > 3,numbers))
print(new_list)

produce = reduce(lambda x,y : x+y,numbers)
print(produce)

nested_list = [[1, 2], [3, 4], [5, 6]]

# Sử dụng map và chain để flatten
flat_map_result = list(chain.from_iterable(map(lambda x: x, nested_list)))
print(flat_map_result)  # Kết quả: [1, 2, 3, 4, 5, 6]

#flat
flat_result = [item for sublist in nested_list for item in sublist]
print(flat_result)  # Kết quả: [1, 2, 3, 4, 5, 6]
