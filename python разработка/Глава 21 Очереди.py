
#Очередь структура данных
#Есть возможность добавлять элементы и удалять но в определенном порядке
#первым вошел первым вышел
#первый вошедший элемент является первым извлекаемым

class Queue:
    def __init__(self):
        self.items = []

        #проверяет на пустату очередь
    def is_empty(self):
        return self.items == []


        #метод добавляющий в очередь элмент
    def enqueue(self,item):
        self.items.insert(0,item)

        #удаляет элемент из очереди
    def dequeue(self):
        return self.items.pop()

        #возвращает колличество эллементов в очереди
    def size(self):
        return len(self.items)

a_queue = Queue()

print(a_queue.is_empty())

for i in range(6):
    a_queue.enqueue(i)
print(a_queue.size())

for i in range(6):
    print(a_queue.dequeue())

print()
print(a_queue.size())


class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
stack = Stack()
for i in "позавчера":
    stack.push(i)
r = ""
for i in range(len(stack.items)):
    r += stack.pop()

print(r)

s1 = Stack()
for i in range(5):
    s1.push(i)

for i in range(5):
    print(s1.pop())

    


















