class Item:
    def calculate(self, x,  y):
        return x*y

itemOne=Item()
itemOne.name="phone"
itemOne.price=100
itemOne.quantity=5
print(itemOne.calculate(10,2))
print(itemOne.calculate(itemOne.price,itemOne.quantity))


print(type(itemOne))
print(type(itemOne.name))
print(type(itemOne.price))
print(type(itemOne.quantity))
