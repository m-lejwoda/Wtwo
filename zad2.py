from abc import ABC, abstractmethod
import time
class State(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def update(self):
        pass
     
class TaxOffice:
    def __init__(self,nr):
        self._state = None
        self._nr = nr
        self._context = self
    def transition_to(self,state):
        self._state = state
        
    def apply_application(self,application):
        print("apply application")
        self._application = application
        self.transition_to(Complex(self._context))
        self._state.update()
    def check_application(self,application,office):
        print("wywołanie")
        if self._nr == office:
            self.transition_to(Adopted(self._context))
        else:
            print(self._nr)
            self.transition_to(Redirect(self._context))
        

class Complex(State):
    def __init__(self,context):
        self._context = context
        self._context._state = self
        print("Wniosek zostaje złożony")
    def update(self):
        
        self._context.transition_to(Adopted(self._context))
        
class Adopted(State):
    def __init__(self,context):
        self._context = context
        self._context._state = self
        self._vovel = []
        self._consonant = []
        print("Mija 1 minuta")
        print("Wniosek został przyjęty")
        self.update()
    def vovel(self,ch):
        if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
            or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
            self._vovel.append(ch)
        else:
            self._consonant.append(ch)  
    def update(self):
        print("Odczekanie 3 minut")
        for element in self._context._application._lastname:
            print(element)
            self.vovel(element)
        if len(self._vovel) > 0 and len(self._consonant) == 0:
            self._context.transition_to(Rejected(self._context)) 
        elif len(self._consonant) > 0 and len(self._vovel) == 0:
            self._context.transition_to(Cancelled(self._context)) 
        else:
            self._context.transition_to(Accepted(self._context))

class Redirect(State):
    def __init__(self,context):
        self._context = context
        self.update()
    def update(self):
        print("Wniosek został przekierowany")

class Accepted(State):
    def __init__(self,context):
        self._context = context
        self.update()
    def update(self):
        print("Wniosek został zaakceptowany")
        print("Czekam 5 minut")
        self._context.transition_to(Closed(self._context))

class Rejected(State):
    def __init__(self,context):
        self._context = context
        self.update()
    def update(self):
        print("Wniosek został odrzucony")
        print("Czekam 6 minut")
        self._context.transition_to(Closed(self._context))

class Cancelled(State):
    def __init__(self,context):
        self._context = context
        self.update()
    def update(self):
        print("Wniosek został anulowany")
        print("Czekam 4 minut")
        self._context.transition_to(Closed(self._context))

class Closed(State):
    def __init__(self,context):
        self._context = context
        self.update()
    def update(self):
        print("Wniosek został zamkniety")

class Application:
    def __init__(self,lastname):
        print("init")
        self._lastname = lastname


if __name__ == "__main__":
    application = Application("Kowalski")
    taxoffice = TaxOffice(4353)
    taxoffice.apply_application(application)
    taxoffice.check_application(application,4353)
    