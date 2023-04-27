#выполнить переворот строки при помощи стрека

class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

steak = Stack()

for i in "Привет":
    steak.push(i)
r = ""
for i in range(len(steak.items)):
    r += steak.pop()
print(r)

r = "sdfgsdfg"
rv = r[::-1]
print(rv)

ser = []
for i in "пока":
    ser.append(i)

print(ser)
