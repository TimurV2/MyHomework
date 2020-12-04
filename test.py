class Node:
    
    def __init__(self, data):
        self.data = data
        self.ref = None

class MyQueue:
    
    mas = []
    
    def __init__(self):
        self.head = None
        mas = []

    def adding(self, data):
        new_node = Node(data)
        MyQueue.mas.append(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
    def print(self):
        if self.head is None:
            print("MuQueue is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref
            print("None")

    def delete(self):
        if self.head is None:
            print ("There is nothing to delete from MyQueue.")
        elif self.head.ref is None:
            self.head = None
            MyQueue.mas.pop()
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
            MyQueue.mas.pop()

    def clear(self):
        if self.head is None:
            print("MyQueue is already empty.")
        while self.head is not None:
            self.head = self.head.ref
        MyQueue.mas.clear()

class Country:
    
    def __init__(self, population, capital):
        self.population = str(population)
        self.capital = str(capital)
        
    def __str__(self):
        return 'Столица и население: {}, {}'.format(self.capital, self.population)

asd = MyQueue()
asd.adding(10) 
asd.adding(100)
asd.adding(200)

asd.print()
print(asd.mas)
print("-------------------------------------------------------")

asd.delete()
asd.print()
print(asd.mas)
print("-------------------------------------------------------")

asd.clear()
asd.print()
print(asd.mas)
print("-------------------------------------------------------")

asd.clear()
print("-------------------------------------------------------")

asd.adding(80085)
asd.print()
print("-------------------------------------------------------")

asd.delete()
print(asd.mas)
print("-------------------------------------------------------")

asd.adding(111) 
asd.adding(222)
asd.adding(333)
qwe1 = Country(1003000, "Катманду")
qwe2 = Country(1338000, "Дублин")

asd.adding(qwe1)
asd.adding(qwe2)

for i in range(len(asd.mas)):
    print(asd.mas[i])