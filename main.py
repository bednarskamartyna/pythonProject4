x = 5
print(type(x))

x = 'HELLO'
print(type(x))

x = 3.14159
print(type(x))

x = 4
id(x)

x = 'hello'
print(id(x))

x = 3.14159
print(id(x))

x = 5
print(id(x))

x = 4
print(id(x))

lst = [1, 2, 3]
print(id(lst))
print(type(lst))
print(lst)

lst[0] = 2
print(id(lst))
print(lst)

t = (1,2,3)
t[0] = 2
#krotka jest niezmienna

s = "Python jest spoko"
print(id(s))
s[0] = "j"
print(id(s))

L = [1, 2, 3]
L.append(100)
print(L)

x = 4.5
print(x.real, "+", x.imag, 'i')

x = (-4.5)**0.5
print(x.real, "+", x.imag, 'i')

f = open("test.txt", "w")   # 'f' jest obiektem typu "plik"
print(type(f))

#atrybuty obiektów też są obiektami
numbers = [6, 9, 3, 1]
print(numbers)
print(id(numbers))
print(sorted(numbers))
print(numbers)
print(id(numbers))
numbers.sort()
print(numbers)
print(id(numbers))

x = 4.0
print(x)
print(type(x))
print(x.real)

print(x.is_integer())
print(type(x.is_integer()))

#klasy - najczęściej używane do nowego typu danych

class NazwaKlasy:
    pass

obiekt = NazwaKlasy()
instancja = NazwaKlasy()

print((type(obiekt)))

print(id(obiekt))
print(id(instancja))

print(obiekt)
print(instancja)

print(NazwaKlasy)
print(type(NazwaKlasy))
print(id(NazwaKlasy))

class NazwaKlasy:
    def nazwa_metody(self, argument1, argument2):
        print(argument1)
        print(argument2)

#self to będzie argument, na którym wywołujemy metodę
#self - musimy powiedzień, na którym obiekcie chcemy wowołać metodę

obiekt = NazwaKlasy()
obiekt.nazwa_metody("arg1", "arg2")

#docstring - literał ciągu, dokumentacja kodu -> wyświetlana za pomocą "help"
# __doc__

"""Dokumentacja modułu"""

class MyClass:
    """Dokumentacja klasy"""

    def my_method(self):
        """Dokumentacja metody"""

def my_function():
    """Dokumentacja funkcji"""

help(MyClass)
help(MyClass.my_method)

#składnia atrybutów
#wariant 1: atrybut klasy, wspólny dla całej klasy
class NazwaKlasy:
    atrybut_pierwszy = "Wartość"
    atrybut_drugi = 123.0

o = NazwaKlasy()
print(o.atrybut_pierwszy)
print(o.atrybut_drugi)

#wariant 2: atrybut nadawany przy tworzeniu obiektu klasy
#związany z konkretnymi instancjami

class NazwaKlasy:
    def __init__(self, trzeci):
        self.atrybut_pierwszy = "Wartość"
        self.atrybut_drugi = 123.0
        self.atrybut_trzeci = trzeci

instancja = NazwaKlasy("test")
print(instancja.atrybut_pierwszy)
print(instancja.atrybut_drugi)
print(instancja.atrybut_trzeci)

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

class Parrot:
    pass

