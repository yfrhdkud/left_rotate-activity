def left_rotate(n):
    arr = [1,2,3,4,5]
    n = n % len(arr)
    return arr[n:] + arr[:n]

n = int(input("Rotate by how many?: "))
guess = input(f"What is the left rotate of {n}: ")
print(f"left rotate of {n} = {left_rotate(n)}, your guess: {guess}")