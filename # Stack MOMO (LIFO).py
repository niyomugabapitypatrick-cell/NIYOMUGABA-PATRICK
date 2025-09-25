stack = []

print("=== MoMo Example ===")
momo_stack = ["PIN", "Amount", "Confirm"]   # push
print("Stack after pushes:", momo_stack)

momo_stack.pop()
print("After undo one:", momo_stack)
print("Remaining top:", momo_stack[-1])   # last item
print()
