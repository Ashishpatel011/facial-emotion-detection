def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    # Take a series of numbers as input from the user
    input_numbers = input("Enter a series of numbers separated by spaces: ")
    
    # Split the input string into individual numbers and convert them to integers
    numbers = map(int, input_numbers.split())
    
    # Filter out the prime numbers
    prime_numbers = [num for num in numbers if is_prime(num)]
    
    # Display the prime numbers
    if prime_numbers:
        print("Prime numbers in the series are:", prime_numbers)
    else:
        print("There are no prime numbers in the series.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
