import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)







print(Fore.RED + 'текст краний')
print(Back.GREEN + 'текст із зеленим фоном')
print(Style.BRIGHT + ' яскравий текст')
print(Fore.BLUE + Back.YELLOW + Style.BRIGHT + 'Комбінований стиль')

print(dir(colorama))

colorama.deinit()