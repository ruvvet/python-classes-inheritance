class Something():

    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c=c

    def __str__(self):
        return f"{self.a}{self.b}{self.c}"

    def print_hi(self):
        print('hi')


x = Something('a','b','c')

print(x)
x.print_hi()