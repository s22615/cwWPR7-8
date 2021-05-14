import sys

terminator = "\n"
reverse = False
separator= " "

for i, each in enumerate(sys.argv[1:]):
    if each == "-n":
        terminator = ""
    elif each == "-r":
        reverse = True
    elif each == "-l":
        separator = "\n"
    else:
        break

args = sys.argv[i+1:]
if reverse:
    args = reversed(args)

print(separator.join(args), end=terminator)

# lista = ["x","y","z"]
# print(lista)
# print(list(enumerate(lista)))