class RecClass():
    def __init__(self, data):
        self.data = data
        if isinstance(self.data, list):
            self.data_array = self.data[:]

    def recursion(self):  # Метод для числа
        if self.data < 0 or not isinstance(self.data, int):
            raise (ValueError, 'Принимаются только положительные числа, целые числа')
        if self.data % 2 == 0:
            print(f' Четные числа: {self.data}')
        if self.data != 2:
            self.data -= 1
            return self.recursion()

    def recursion_array(self):  # Метод для списка
        if 0 in self.data_array:
            self.data_array.remove(0)
        for x in self.data:
            if x not in range(-256, 256):
                raise (ValueError, ' Принимается число от 256 до -256 ')

        if len(self.data_array) > 1:
            res = self.data_array[0] * self.data_array[1]
            self.data_array[1] = res
            self.data_array = self.data_array[1:]
            return self.recursion_array(), 'Произведение', res


x = RecClass(10)
print(x.recursion(), end='\tStop\n')
y = RecClass(15)
print(y.recursion(), end='\tStop\n')
z = RecClass([2, 0, 3, 4, 5, 6, 4, 0])
print(z.recursion_array())
'''w=RecClass(12.5)                 #Выдаст ошибку
print(z.recursion())'''
'''q=RecClass(-20)                  #Чтобы проверить сотрите кавычки
print(q.recursion())'''
'''e=RecClass([4,2,277])
print(e.recursion_array())'''
