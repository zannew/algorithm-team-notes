from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

# permutations
result = list(permutations(data, 3))
print(result)

# combinations
result = list(combinations(data, 2))
print(result)

# product
result = list(product(data, repeat=2))
print(result)

# combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
print(result)