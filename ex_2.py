"""

Я решил написать два класса, которые будут реализовывать циклический буфер FIFO для
очереди на прививку в поликлинике.

"""
class VaccineArray:
    def __init__(self, hall):
        self.hall = hall
        self.content = [None] * hall
        self.size = 0
        self.first = 0
        self.last = 0

    def enqueue(self, name, birth_year):
        if self.size == self.hall:
            print("Очередь переполнена")
            return
        self.content[self.last] = (name, birth_year)
        self.last = (self.last + 1) % self.hall
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Очередь пуста")
            return None, None
        name, birth_year = self.content[self.first]
        self.first = (self.first + 1) % self.hall
        self.size -= 1
        return name, birth_year

'''

VaccineArray

Плюсы: массив фиксированного размера позволяет эффективно использовать память.
Добавление и удаление элементов занимает постоянное количество времени вне
зависимости от того, сколько данных нужно обработать.

Минусы: если достигается предел размера буфера, то операция добавления элемента 
становится недоступной и память не освобождается.
В случае расширения числа значений необходимо скопировать все элементы,
что может замедлить работу программы. 

'''
class VaccineList:
    def __init__(self, hall):
        self.hall = hall
        self.content = []
        self.size = 0

    def enqueue(self, name, birth_year):
        if self.size == self.hall:
            print("Очередь переполнена")
            return
        self.content.append((name, birth_year))
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Очередь пуста")
            return
        name, birth_year = self.content.pop(0)
        self.size -= 1
        return name, birth_year

"""

VaccineList

Плюсы: список может динамически изменяться, поэтому появляется
гибкость в изменении числа значений.
Для удаления или изменения элементов не нужно дополнительно сохранять.

Минусы: удаление элемента из начала списка (pop(0)) неэффективно,
так как оно напрямую зависит от количества значений.
Производительность может снизиться из-за динамического изменения
размера списка в случае большого количества операций добавления и удаления.  

"""

# Создание объекта вместимостью 8 пациентов
vaccine_content = VaccineArray(8)
# vaccine_content = VaccineList(8)

# Добавление элементов
vaccine_content.enqueue("Jan Nepomnyashchy", 1990)
vaccine_content.enqueue("Hikaru Nakamura", 1987)
vaccine_content.enqueue("Alireza Firuja", 2003)
vaccine_content.enqueue("Gukesh Dommaraju", 2006)
vaccine_content.enqueue("Fabiano Caruana", 1992)
vaccine_content.enqueue("Rameshbabu Pragnanandha", 2005)
vaccine_content.enqueue("Nijat Abasov", 1995)
vaccine_content.enqueue("Vidit Gujrati", 1994)
# vaccine_content.enqueue("Magnus Carlsen", 1990)


# Извлечение элемента из буфера
name, birth_year = vaccine_content.dequeue()
print(name, birth_year)

"""

Реализация с использованием массива (VaccineArray) будет более эффективной и производительной
при большем объеме данных, чем реализация с использованием списка (VaccineList). Поэтому, если 
необходимо работать с большим объемом данных, то лучше подойдет массив. Однако, если требуется 
простая и легкая в понимании реализация, то можно использовать список.

"""
