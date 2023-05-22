def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Daftar bilangan
numbers = [7, 10, 13, 6, 17, 22, 19]

# Cari bilangan prima
prime_numbers = find_prime_numbers(numbers)

# Tampilkan bilangan prima yang ditemukan
print("Bilangan prima dalam daftar:", prime_numbers)
