import re

example = '''
P1 is a product composed of P2 and P3
P2 is an elementary product
P5 is a product composed of P1 and P4
P4 is an elementary product
P9 is a product composed of P1, P6, and P4
P10 is a product composed of P3 and P5
P11 is a product composed of P5 and P3 '''

print(example)

print("\nElementary Products:")
search1 = re.findall(r"P\d is an elementary product", example)
print("\n".join(search1))

print("\nProducts composed of three products:")
search2 = re.findall(r"P\d+ is a product composed of P\d+, P\d+, and P\d+", example)
print("\n".join(search2))

print("\nProducts composed only of P3 and P5:")
search3 = re.findall(r"(P\d+ is a product composed of P3 and P5|P\d+ is a product composed of P5 and P3)", example)
print(*search3, sep="\n")

print("\nProducts composed that do not have P2 in their compositions:")
search4 = re.findall(r"P\d+ is a product composed of P[^2] and P[^2]|P\d+ is a product composed of P[^2], P[^2], and P[^2]", example)
print(*search4, sep="\n")

search5 = re.findall(r"P9 is a product composed of (.+)", example)
print("\nProducts that compose P9:"," ".join(search5))
