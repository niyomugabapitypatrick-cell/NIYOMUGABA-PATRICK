# 3. Challenge: Reverse "STACKRWANDA" using stack
print("\n=== Reverse String Example ===")
word = "STACKRWANDA"
stack = []

# push each character
for ch in word:
    stack.append(ch)

# pop to reverse
reversed_word = ""
while stack:
    reversed_word += stack.pop()

print("Original:", word)
print("Reversed:", reversed_word)
print()
