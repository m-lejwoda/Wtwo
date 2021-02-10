from abc import ABC,abstractmethod
import random
class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, name):
        pass

class ExerciseHandler(Handler):
    _next_handler = None
    
    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self,name):
        if self._next_handler:
            return self._next_handler.handle(name)
        return None
    @abstractmethod
    def average(self):
        pass
class Exercise1Handler(ExerciseHandler):
    def __init__(self):
        self.deegrees = []
        for i in range(10):
            self.deegrees.append(random.randint(1,5))

    def average(self):
        add = 0
        for elements in self.deegrees:
            add = add + elements
        result = add / len(self.deegrees)
        print(result)
        print("Średnia ocen z zadania o numerze 1: " +  str(result))


    def handle(self,name):
        print(name)
        print("Sprawdzenie zadania nr 1")
        if name == "prowadzacy3":
            self.average()
        return super().handle(name)
class Exercise2Handler(ExerciseHandler):
    def __init__(self):
        self.deegrees = []
        for i in range(10):
            self.deegrees.append(random.randint(1,8))
    def average(self):
        add = 0
        for elements in self.deegrees:
            add = add + elements
        result = add / len(self.deegrees)
        print("Średnia ocen z zadania o numerze 2: " +  str(result))
    def handle(self,name):
        print("Sprawdzenie zadania nr 2")
        if name == "prowadzacy1":
            self.average()
        return super().handle(name)
class Exercise3Handler(ExerciseHandler):
    def __init__(self):
        self.deegrees = []
        for i in range(10):
            self.deegrees.append(random.randint(1,10))
    def average(self):
        add = 0
        for elements in self.deegrees:
            add = add + elements
        result = add / len(self.deegrees)
        print("Średnia ocen z zadania o numerze 3: " +  str(result))
    def handle(self,name):
        print("Sprawdzenie zadania nr 3")
        if name == "prowadzacy2":
            self.average()
        return super().handle(name)
class Exercise4Handler(ExerciseHandler):
    def __init__(self):
        self.deegrees = []
        for i in range(10):
            self.deegrees.append(random.randint(1,9))
    def average(self):
        add = 0
        for elements in self.deegrees:
            add = add + elements
        result = add / len(self.deegrees)
        print("Średnia ocen z zadania o numerze 4: " +  str(result))
    def handle(self,name):
        print("Sprawdzenie zadania nr 4")
        if name == "prowadzacy1":
            self.average()
        return super().handle(name)
class Exercise5Handler(ExerciseHandler):
    def __init__(self):
        self.deegrees = []
        for i in range(10):
            self.deegrees.append(random.randint(1,12))
    def average(self):
        add = 0
        for elements in self.deegrees:
            add = add + elements
        result = add / len(self.deegrees)
        print("Średnia ocen z zadania o numerze 5: " +  str(result))
    def handle(self,name):
        print("Sprawdzenie zadania nr 5")
        if name == "prowadzacy3":
            self.average()
        return super().handle(name)
class Leader():
    def __init__(self,name):
        self._name = name
    def check_exercise(self,handler):
        print("check_exercise")
        result = handler.handle(self._name)


if __name__ == "__main__":
    exercise1 = Exercise1Handler()
    exercise2 = Exercise2Handler()
    exercise3 = Exercise3Handler()
    exercise4 = Exercise4Handler()
    exercise5 = Exercise5Handler()
    leader1 = Leader("prowadzacy1")
    leader2 = Leader("prowadzacy2")
    leader3 = Leader("prowadzacy3")
    exercise1.set_next(exercise2).set_next(exercise3).set_next(exercise4).set_next(exercise5)
    leader1.check_exercise(exercise1)
    leader2.check_exercise(exercise1)
    leader3.check_exercise(exercise1)