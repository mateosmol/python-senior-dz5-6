import colorama
from colorama import Fore, Back, Style
import inspect

print(Fore.GREEN + Style.BRIGHT + "Ретроспекція бібліотеки colorama")
print(Fore.RESET + Style.RESET_ALL + "Тип елемента {type(colorama)}")
print("Методи елемента:")
for i in dir(colorama):
    print(i)
print(f"Розміщення модуля {inspect.getmodule(colorama)}")

print(Style.BRIGHT + "Якщо ви читали README, там в третьому пункті був код. Тут його демонстрація:")

colorama.init(autoreset=True)

print(Fore.RED + "Червоний текст")
print(Fore.GREEN + "Зелений текст")
print(Back.BLUE + "Текст на синьому фоні")
print(Style.BRIGHT + "Яскравий (взагалі він жирний) текст")
print(Style.DIM + "Тьмяний текст")
print()
print(Fore.RESET + Style.RESET_ALL + "а взагалі дякую за бібліотеку, прикольна, використовуватиму")
