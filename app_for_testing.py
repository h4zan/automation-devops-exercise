def main():
    print("Enter a number between 1-10")

    while True:
        first_num = int(input("Enter first number: "))
        if first_num < 1 or first_num > 10:
            print("Try again, enter a number between 1-10")
            continue  
        second_num = int(input("Enter second number: "))

        if second_num < 1 or second_num > 10:
            print("Try again, enter a number between 1-10")
            continue
        total = first_num + second_num
        print(f"The sum of {first_num} + {second_num} is {total}")

        break  

def add_numbers():
    return 1 + 1

if __name__ == "__main__":
    main()

