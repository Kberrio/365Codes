def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

def main():
    num = int(input("Enter a number to find its prime factors: "))
    if num < 2:
        print("Prime factors are not defined for numbers less than 2.")
    else:
        factors = prime_factors(num)
        print("Prime factors of", num, "are:", factors)

if __name__ == "__main__":
    main()
