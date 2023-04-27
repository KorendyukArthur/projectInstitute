# Стек структура данных - как список только в него
# можно добавлять и удалять из него только последний эллемент

#Удаление из стека метод pop()
#Добавление в стек метода push()

#вид структуры данных "последним вошел, первым вышел"

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)



stack = Stack()
stack.push(1)
stack.push(2)
print(stack.is_empty())
stack.pop()
stack.pop()
print(stack.is_empty())

stack1 = Stack()
for i in range(0,7):
    stack1.push(i)

print(stack1.peek())
print(stack1.size())











