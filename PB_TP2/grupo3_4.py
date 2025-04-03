class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Listaenca:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def bubble_sort(self):
        if not self.head:
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if temp.data > temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data
                    swapped = True
                temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    lista = Listaenca()
    for num in [32,64,34,25,53, 12, 22,11,90]:
        lista.append(num)

    print("Antes de organizar")
    lista.display()

    lista.bubble_sort()
    print("Depois de organizar:")
    lista.display()
