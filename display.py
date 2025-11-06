def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

start = int(input("Enter start of interval: "))
end = int(input("Enter end of interval: "))

print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
