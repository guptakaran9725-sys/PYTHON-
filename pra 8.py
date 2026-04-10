# PRACTICAL 8

# i. if-else: Check whether a string is Symmetrical or Palindrome
def check_string(s):
    # Palindrome check
    if s == s[::-1]:
        print(f"'{s}' is a Palindrome")
    else:
        print(f"'{s}' is not a Palindrome")

    # Symmetrical check
    mid = len(s) // 2
    if len(s) % 2 == 0:
        first_half = s[:mid]
        second_half = s[mid:]
    else:
        first_half = s[:mid]
        second_half = s[mid+1:]
    
    if first_half == second_half:
        print(f"'{s}' is Symmetrical")
    else:
        print(f"'{s}' is not Symmetrical")

# Example
check_string("madam")
check_string("abba")
check_string("abcabc")


# ii. for loop: Multiply two matrices using nested loops
def multiply_matrices_for(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Example matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("\nMatrix Multiplication using for loop:")
print(multiply_matrices_for(A, B))


# iii. while loop: Multiply two matrices using nested loops
def multiply_matrices_while(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    i = 0
    while i < len(A):
        j = 0
        while j < len(B[0]):
            k = 0
            while k < len(B):
                result[i][j] += A[i][k] * B[k][j]
                k += 1
            j += 1
        i += 1
    return result

print("\nMatrix Multiplication using while loop:")
print(multiply_matrices_while(A, B))