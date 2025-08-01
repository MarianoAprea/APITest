
lista=[]
lista = [1, 2, -3, "hola", False]
lista.append(4)
i = 0
while i < len(lista):
    item = lista[i]
    if isinstance(item, int) and item > 0:
        print(f"{item} is an integer greater than 0")
    elif isinstance(item, str):
        print(f'"{item}" is a string')
    elif isinstance(item, bool):
        print(f"{item} is a boolean value")
    elif isinstance(item, int) and item < 0:
        print(f"{item} is an integer less than 0")
    else:
        print(f"{item} does not match any condition")
    i += 1
