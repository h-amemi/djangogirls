print('Hello, Django girls!')
if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print("a")

name = 'Sonja'
# Olaの場合
if name == 'Ola':
    print("Ola!!")
elif name == 'Sonja':
    print("sonjaa!")
else:
    print("anonymous!")

def hi(name):
    print("Hi " + name + "!")

girls = ["Rachel", "Monica", "Phoebe", "Ola", "Hayato"]
for name in girls:
    hi(name)
    print("Next girl")
