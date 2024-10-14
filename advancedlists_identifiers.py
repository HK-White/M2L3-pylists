#2. Advanced List Methods and Identity Operators

#Task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

check_alice = "Alice" in attended and "Alice" in submitted
print(check_alice)
## or ##
if "Alice" in attended and "Alice" in submitted:
    print("Alice is in both lists!")


#Task 2
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:14]
print("These are the temps for week two: " + str(second_week))

