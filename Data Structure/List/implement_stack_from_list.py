class Stack:

    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)
        print(self.items)

    def peek(self):
        return items.items[0]

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)


stack_obj=Stack()
stack_obj.push(1)
stack_obj.push(2)
stack_obj.pop()
print(stack_obj.peek())




