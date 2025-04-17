from Bonus13.convert13 import convert
from Bonus13.parse13 import parse

feet_inch = input('Enter feet and inch')

f,i = parse(feet_inch)
result = convert(f, i)

print(result)
