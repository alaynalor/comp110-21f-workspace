"""An example of for in syntax."""

names: list[str] = ["Alayna", "Lanie", "Lu"]

print("while output")
i: int =0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print ("for... in output")
for name in names:
    print(names)