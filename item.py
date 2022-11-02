class Item:
  def __init__(self, id:int, name:str,price:float, mesurement_unit:str) -> None:
    self.id=id
    self.name=name
    self.price=price
    self.mesurement_unit=mesurement_unit
  
  def __repr__(self) -> str:
    return"<class 'Item'>"

  def __str__(self)->str:
    return f"{self.name}:${self.price}/{self.mesurement_unit}" 

