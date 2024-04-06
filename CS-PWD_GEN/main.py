import random
import string

def generate_pwd(length):
    chr = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(chr) for _ in range(length))
    return pwd

def main():
    print("Welcome to Password Generator!")
    while True:
        try:
            length = int(input("Enter the length of the password you want: "))
            if length <= 0:
                print("Please enter a number greater than zero.")
            else:
                pwd = generate_pwd(length)
                print("Generated Password:", pwd)
                break
        except ValueError:
            print("Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
