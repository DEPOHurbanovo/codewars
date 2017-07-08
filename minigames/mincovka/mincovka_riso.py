values = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
values_count = {}

#number = int(100 * float(input("Zadaj hodnotu: ")))
number_str = input("Zadaj hodnotu: ")
if "." in number_str:
    if number_str[-2] == ".":
        number = number_str.replace(".", "")
        number = int(number + "0")
    elif number_str[-3] == ".":
        number = number_str.replace(".", "")
        number = int(number)
else:
    number = int(number_str) * 100
print(number)

# create dict
for value in values:
    values_count[value] = (number - (number % int(value * 100))) / int(value * 100)
    number = number % int(value * 100)

money = []
for values_count_each in values_count:
    if values_count[values_count_each] != 0:
        money.append([values_count_each, values_count[values_count_each]])

money.sort(reverse=True)

print(money)
