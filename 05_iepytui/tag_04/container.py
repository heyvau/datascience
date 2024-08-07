class Container:
    def __init__(self):
        self.content = {}


    def __len__(self):
        return len(self.content)


    def __getitem__(self, index: int):
        try:
            return self.content[index]
        except KeyError:
            print(f"Gibt es keinen Element unter dem Index <{repr(index)}>")


    def __setitem__(self, index: int, value):
        if not isinstance(index, int) or index < 0 or index > len(self):
            print(f"Index <{repr(index)}> ist ungültig.")
            return
        self.content[index] = value


    def __delitem__(self, index: int):
        try:
            del self.content[index]
        except KeyError:
            print(f"Gibt es keinen Element unter dem Index <{repr(index)}>")
        else:
            for k in range(index, len(self.content)):
                self.content[k] = self.content.pop(k+1)


c = Container()

c[0] = "Hallo"
c[1] = "Python"
c[2] = 123
c[3] = 10
c[4] = 1


print("Content:", c.content)

del c[3]
del c[10]

print("Content:", c.content)

print("Length:", len(c))