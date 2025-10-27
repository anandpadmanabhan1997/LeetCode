# 🧪 Mixed Example: List with Primitives and Nested List
# python
import copy
original = [1, "hello", [2, 3]]
shallow = copy.copy(original)
shallow[0] = 99          # primitive → safe
shallow[2][0] = 88       # nested list → shared reference
print(original)  # Output: [1, 'hello', [88, 3]]
print(shallow) # [99,’hello’,[88,3]]





import copy

# Original nested list
original = [[1, 2], [3, 4]]

# Deep copy
deep = copy.deepcopy(original)

# Modify the deep copy
deep[0][0] = 99

# Print both
print("Original:", original)
print("Deep Copy:", deep)



