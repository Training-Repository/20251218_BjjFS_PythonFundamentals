a = 0.7
b = 0.6
c = a - b
print(c == 0.1)

print(c)

from decimal import Decimal

x = 0.7
p = Decimal(x)
q = Decimal(0.6)
print(p, q)
r = Decimal(p - q)
print(type(r), r)


p = Decimal('0.7')
q = Decimal('0.6')
print(p - q)

from fractions import Fraction

fr = Fraction('0.1')
print(fr)

PI = 22/7
print(PI)

# N = Decimal('22')
# D = Decimal('7')
# PI = N/D

print(PI)

radius = 7
circumference = 2 * PI * radius
print(circumference)
