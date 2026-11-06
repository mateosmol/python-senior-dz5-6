import colorama
import inspect

print("Ретроспекція бібліотеки colorama")
print(f"Тип елемента {type(colorama)}")
print("Методи елемента:")
for i in dir(colorama):
    print(i)
print(f"Розміщення модуля {inspect.getmodule(colorama)}")
