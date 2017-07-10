from decimal import Decimal

value = Decimal(float(input("Zadaj sumu: ")) * 100).quantize(2)

money = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
usages = []

for m in money:
    m_cents = m * 100
    usages.append(int(value / m_cents))
    value = int(value % m_cents)

print("\nNajefektivnejsie rozmenenie sumy:")
for value, usage in zip(money, usages):
    print("{}: {}".format(value, usage))
