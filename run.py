# 2. Practical (Rwanda) UR Example
print("=== UR Example ===")
ur_stack = ["Exercise1", "Exercise2", "Exercise3"]   # push
print("Stack after pushes:", ur_stack)

# Undo two (pop twice)
ur_stack.pop()
ur_stack.pop()
print("After undo two:", ur_stack)
print("Current top:", ur_stack[-1])
print()