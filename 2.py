# def prime_number(number: int):
#
#     for num in range(2, number):
#         flag = False
#
#         for i in range(2, num):
#
#             if num % i == 0:
#                 flag = True
#                 break
#
#         if not flag:
#             yield num


class Primes:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        self.x = 2
        return self

    @staticmethod
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def __next__(self):

        if self.x < self.end:

            if self.is_prime(self.x):
                print(self.x)
            self.x += 1

        else:
            raise StopIteration


while True:
    user_number = input("Enter a number: ")
    if user_number.isnumeric():
        user_number = int(user_number)
        break
    else:
        print("INVALID INPUT! Please enter a number.")
        continue

number = Primes(user_number)
x = iter(number)
for i in range(number.end):
    next(x)

