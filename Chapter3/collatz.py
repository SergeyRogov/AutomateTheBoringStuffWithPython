def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def main():
    print("Enter integer: ", end='')
    try:
        num = int(input())

        while num != 1:
            print(num)
            num = collatz(num)

        print(num)
    except ValueError as e:
        print("Entered not integer! Try again.")
        main()