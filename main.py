
# zad1
import time


def imie():
    i = input("Podaj imie: ")
    n = input("Podaj nazwisko: ")
    wypisz(i, n)


def wypisz(i, n):
    return print("Twoje imie i nzawisko to ", i, n)


imie()


# zad2
def licz(x):
    time.sleep(1)
    if (x == 0):
        print(x)
    elif (x < 0):
        print(x)
        licz(x + 1)
    else:
        print(x)
        licz(x - 1)


x = int(input("Wprowadz liczbe"))
licz(x)


# zad3

def komunikacja():
    i = int(input("Podaj pierwsza liczbe: "))
    n = int(input("Podaj druga liczbe: "))
    x = int(input("Podaj liczbe odpowiadajaca operacji: 1=mnozenie,2=dzielenie,3=dodawanie,4-=odejmowanie"))
    operacje(i, n, x)


def operacje(i, n, x):
    if (x == 1):
        wyn = i * n;
        print(wyn)
    elif (x == 2):
        if (n == 0):
            print("NIE DZIEL PRZEZ 0!")
        else:
            wyn = i / n;
            print(wyn)
    elif (x == 3):
        wyn = i + n;
        print(wyn)
    elif (x == 4):
        wyn = i - n;
        print(wyn)
    else:
        print("Podales zle wartosci")


komunikacja()

#zad4

add = lambda i, n: i + n
print(add(2, 5))
subtract=lambda i, n: i - n
print(subtract (4,8))
divide=lambda i, n: i / n
print(divide(8,2))
multiply=lambda i, n: i * n
print(multiply(4,2))


#zad5
print('Wpisz liczbe :')
liczba = int(input())

for dzielniki in filter(lambda x: liczba % x == 0, range(1, liczba)):
    print(dzielniki)

#zadanie6
import time
def licz(fun1,y):
    t1 = int(round(time.time() * 1000))
    x = fun1(y)
    t2 = int(round(time.time() * 1000)) - t1
    print(t2,"ms")
    return x

def sil1(x):
    if x == 1:
        return x
    else:
        wynik = 1
        for i in range(1, x+1):
            wynik = wynik * i
        return wynik

def sil2(x):
    if x == 1:
        return x
    else:
        return x * sil2(x - 1)

x = int(input("Podaj liczbe calkowita: "))

print(licz(sil1,x))
print(licz(sil2,x))

#zadanie7
def uzytkownik():
    uzytkownik.tekst = input("Podaj tekst: ")

def b(y):
    def dekor():
        return '<b>' + y() + '</b>'
    return dekor

def i(y):
    def dekor():
        return '<i>' + y() + '</i>'
    return dekor

def u(y):
    def dekor():
        return '<u>' + y() + '</u>'
    return dekor

uzytkownik()

@b
@i
@u
def wypisz():
    x = uzytkownik.tekst
    return x

print(wypisz())



