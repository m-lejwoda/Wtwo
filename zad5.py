from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self,inst):
        pass
class NameChanger(Observer):
    typ = "NameChanger"
    def update(self,inst,*args):
        for el in inst.parents:
            print("<" + el.name +" " + el.lastname+ "> :" + "Obecnie " + args[0]+ " " +args[1] + " nazywa się " + args[2] +" " + args[3] )
        for el in inst.childrens:
            print("<" + el.name +" " + el.lastname+ "> :" + "Obecnie " + args[0]+ " " +args[1] + " nazywa się " + args[2] +" " + args[3] )

class DateChanger(Observer):
    typ = "DateChanger"
    def update(self,inst,*args):
        for el in inst.parents:
            print("<" + el.name +" " + el.lastname+ "> :" + " Moje dziecko urodziło się nie " + args[0] +" a " + args[1])

class ChildrenChanger(Observer):
    typ = "ChildrenChanger"
    def update(self,inst,*args):
        for el in args[0]:
            print("<" + el.name +" " + el.lastname+ "> :" + " Moje nowe rodzeństwo " + args[1].name +" " + args[1].lastname)

class Producer(ABC):
    @abstractmethod
    def subscribe(self,observer):
        pass
    @abstractmethod
    def unsubscribe(self,observer):
        pass
    @abstractmethod
    def notify(self,type,*args):
        pass
class Person(Producer):
    def subscribe(self,observer):
        self.observers.append(observer)
    def unsubscribe(self,observer):
        for element in self.observers:
            if element in self.observers:
                self.observers.remove(element)
    
    def notify(self,typ,*args):
        for el in self.observers:
            if typ == "name" and el.typ == "NameChanger":
                el.update(self,*args)
            if typ == "birthday" and el.typ == "DateChanger":
                el.update(self,*args)
            if typ == "children" and el.typ == "ChildrenChanger":
                el.update(self,*args)
                 
    def __init__(self,name,lastname,birthday_date):
        self.name = name
        self.lastname = lastname
        self.birthday_date = birthday_date
        self.childrens = []
        self.parents = []
        self.wife = []
        self.observers = []
    def set_children(self,child):
        self.childrens.append(child)
    def set_parent(self,parent):
        self.parents.append(parent)
    def set_wife(self,wife):
        self.wife.append(wife)
    def change_name(self,name,lastname):
        self.notify("name",self.name ,self.lastname,name,lastname)
        self.name = name
        self.lastname = lastname
    def change_birthday(self,birthday_date):
        self.notify("birthday",self.birthday_date,birthday_date)
        self.birthday_date = birthday_date     
    def new_children(self,child):
        self.notify("children",self.childrens,child)
        self.childrens.append(child)
        
    
if __name__ == '__main__':
    me = Person("Michał","Kowalski","12.20.1997")
    wife = Person("Klaudia","Kowalska","12.20.1998")
    parent1 = Person("Jan","Kowalski","12.20.1965")
    parent2 = Person("Barbara","Kowalska","12.20.1969")
    child1 = Person("Krzysztof","Kowalski","12.20.2020")
    child2 = Person("Julia","Kowalska","11.20.2020")
    namechanger = NameChanger()
    datechanger = DateChanger()
    childrenchanger = ChildrenChanger()
    me.set_wife(wife)
    me.set_parent(parent1)
    me.set_parent(parent2)
    me.set_children(child1)
    me.set_children(child2)
    me.subscribe(namechanger)
    me.subscribe(datechanger)
    me.subscribe(childrenchanger)
    wife.subscribe(namechanger)
    wife.subscribe(datechanger)
    wife.subscribe(childrenchanger)
    parent1.subscribe(namechanger)
    parent1.subscribe(datechanger)
    parent1.subscribe(childrenchanger)
    parent2.subscribe(namechanger)
    parent2.subscribe(datechanger)
    parent2.subscribe(childrenchanger)
    child1.subscribe(namechanger)
    child1.subscribe(datechanger)
    child1.subscribe(childrenchanger)
    child2.subscribe(namechanger)
    child2.subscribe(datechanger)
    child2.subscribe(childrenchanger)
    #Nowe dziecko testowe
    child3 = Person("Jaś","Kowalski","11.20.2020")
    me.change_name("Michał","Nowak")
    me.change_birthday("10.09.1997")
    me.new_children(child3)

    

