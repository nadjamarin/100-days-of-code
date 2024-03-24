# def add(*args):
#     final_sum = 0
#     for n in args:
#         final_sum += n
#     return final_sum
#
#
# print(add(3, 5, 6))


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        # self.model = kw["model"]
        self.model = kw.get("model")
        self.color = kw.get("color")


# my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan")
print(my_car.model)
