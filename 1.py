def perfect(number):

    def divisor(num):

        for i in range(1, num):

            if num % i == 0:
                yield i

    if sum(divisor(number)) == number:
        return f"{number} is a perfect number!"

    elif sum(divisor(number)) > number:
        return f"{number} is greater than the perfect number!"

    else:
        return f"{number} is less than the perfect number!"


while True:
    user_number = input("Enter a number: ")

    if user_number.isnumeric():
        print(perfect(int(user_number)))
        break
    else:
        print("INVALID INPUT! Please enter just a number.")
        continue
