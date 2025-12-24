from mean_var_std import calculate

# List of test cases with 9 numbers each
test_cases = [
    [0,1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8,9],
    [9,8,7,6,5,4,3,2,1]
]

# Run all valid test cases
for i, case in enumerate(test_cases, 1):
    print(f"\nTest Case {i}: {case}")
    try:
        result = calculate(case)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

# Test ValueError for list with less than 9 elements
print("\nTesting ValueError for invalid input:")
try:
    calculate([1, 2, 3])
except ValueError as e:
    print("Passed ValueError Test:", e)
