# Quantities collected per day (kg)
daily_intake = [120, 150, 90, 200, 170]
total = sum(daily_intake)
average = total / len(daily_intake)
maximum = max(daily_intake)
threshold = 140
# Compound condition: above threshold and max > 180
if average > threshold and maximum > 180:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")
print()

