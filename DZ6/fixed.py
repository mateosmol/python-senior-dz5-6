result = []
def divider(a, b):
    try:
        if a < b:
            return ValueError
        elif b > 100:
            return IndexError
        return a / b
    except TypeError:
        return "Format isn't dividible"
    except ZeroDivisionError:
        return "Can't divide by zero"

data = {10: 2, 2: 5, "123": 4, 18: 0, "": 15, 8: 4}
print(f"Neither a list, nor a set can't be inside a set. So i will replace it into a str. New: data = {data}")

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)