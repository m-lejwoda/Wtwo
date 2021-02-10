from enum import Enum
from abc import ABC, abstractmethod
class Broker:
    def __init__(self):
        self.observers = []
        self.publishers = []
    def registerSubscriber(self):
        print("")
    def registerPublisher(self):
        print("")
    def fire(self):
        print("sdada")
class EventType(Enum):
    ChangeName=1
    ChangeDate=2
    NewChildren = 3
class Event(ABC):
    pass

class PersonEvent(Event):
    pass

class Publisher:
    def __init__(self):
        pass
