from dis import dis
from cash_register import CashRegister
from customer import Customer 
from item import Item



egg= Item(100,"Egg",0.80,"Piece")
rice=Item(101,"Rice",3.45,"kg")
banana=Item(102,"Banana",5.67,"kg")
cheese=Item(103,"Cheese",5,"kg")
honey=Item(104,"Honey",4,"Gr")
oats=Item(105,"Oats",3.2,"Kg")
pasta=Item(106,"Pasta",2.2,"Kg")
yogurt=Item(107,"Yogurt",4.8,"Gr")



customer1 = Customer("Clark ", "Kent")

cr1=CashRegister(customer1)

cr1.add_item(yogurt)
cr1.add_item(oats,3,0.50)
cr1.update_item(oats,6,1)
cr1.add_item(cheese,3,0.75)
cr1.add_item(honey,3,0.75)
cr1.remove_item(egg)

cr1.display_invoice()


customer2 = Customer("John", "Doe")

cr2 = CashRegister(customer2)

cr2.add_item(yogurt,qty=4, discount=10)
cr2.add_item(egg,qty=6)
cr2.update_item(egg,qty=24, discount=12)
cr2.add_item(banana, qty=4, discount=2)
cr2.add_item(honey, qty=1)

cr2.display_invoice()
