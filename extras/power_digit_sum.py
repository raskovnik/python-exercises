#project euler problem 16:What is the sum of the digits of the number 2**1000
a, power_sum = str(2**1000), 0
print("Calculating...")
for i in range(0, len(a)):
    power_sum += int(a[i])

print(f"Sum of powers is: {power_sum}")
