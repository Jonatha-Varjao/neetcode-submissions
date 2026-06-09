class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity
        self.asize = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        
        if self.asize == self.capacity:
            self.resize()
        self.array[self.asize] = n
        self.asize += 1

    def popback(self) -> int:
        value = self.array[self.asize-1] 
        self.asize -= 1
        return value

    def resize(self) -> None:
        self.array = self.array + [None] * self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.asize
    
    def getCapacity(self) -> int:
        return self.capacity