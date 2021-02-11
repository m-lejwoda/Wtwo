class Student:
    def __init__(self,mediator,id1):
        self._mediator = mediator
        self._id = id1
    def create_message(self,message,id1):
        self._mediator.create_student_message(message,id1,self._id)
    def create_announcements(self,announcement):
        self._mediator.create_leader_announcements(announcement)
    def get_announcements(self,announcement):
        print("Student o id "+ str(self._id) + " Otrzymałem ogłoszenie " + str(announcement._description))
    def get_message(self,message,leader):
        print("Student o id "+ str(self._id) + " Otrzymałem wiadomość o treści " + str(message._description) + " od " + str(leader))
    def get_materials(self,material):
        print("Student o id "+ str(self._id) + " Otrzymałem materiał " + str(material._description))
class Leader:
    def __init__(self,mediator,id1):
        self._mediator = mediator
        self._id = id1
    def get_message(self,message,student):
        print("Prowadzacy o id "+ str(self._id) + " Otrzymałem wiadomość o treści " + str(message._description) + " od " + str(student))
    def create_announcements(self,announcement):
        self._mediator.create_leader_announcements(announcement)
    def create_materials(self,material):
        self._mediator.create_leader_materials(material)
    def create_message(self,message,id1):
        self._mediator.create_leader_message(message,id1,self._id)
        


class Mediator:
    def __init__(self):
        self._store_students = []
        self._store_leaders = []
        self._messages = []
        self._announcements = []
        self._materials = []
    def set_student(self,student):
        self._store_students.append(student)
    def set_leader(self,leader):
        self._store_leaders.append(leader)
    def create_student_message(self,message,id1,leaderid):
        for person in self._store_students:
            if person._id == id1:
                person.get_message(message,leaderid)
        for person in self._store_leaders:
            if person._id == id1:
                person.get_message(message,leaderid)
    def create_leader_message(self,message,id1,leaderid):
        for person in self._store_students:
            if person._id == id1:
                person.get_message(message,leaderid)
    def create_student_announcements(self,announcement):
        for person in self._store_students:
            person.get_announcements(announcement)
    def create_leader_announcements(self,announcement):
        for person in self._store_students:
            person.get_announcements(announcement)
    def create_leader_materials(self,material):
        for person in self._store_students:
            person.get_materials(material)

class Announcement:
    def __init__(self,description):
        self._description = description

class Material:
    def __init__(self,description):
        self._description = description

class Message:
    def __init__(self,description):
        self._description = description

if __name__ == '__main__':
    mediator = Mediator()
    student1 = Student(mediator,"s278444")
    student2 = Student(mediator,"s278445")
    student3 = Student(mediator,"s278446")
    leader1 = Leader(mediator,"p342131")
    leader2 = Leader(mediator,"p342132")
    mediator.set_student(student1)
    mediator.set_student(student2)
    mediator.set_student(student3)
    mediator.set_leader(leader1)
    mediator.set_leader(leader2)
    announcement = Announcement("Ogłoszenie testowe prowadzacego")
    material = Material("Materiał testowy prowadzacego")
    message = Message("Wiadomość testowa prowadzacego")
    announcement1 = Announcement("Ogłoszenie testowe studenta")
    message1 = Message("Wiadomość testowa studenta")
    leader1.create_announcements(announcement)
    leader1.create_materials(material)
    leader1.create_message(message,"s278446")
    student1.create_message(message1,"p342131")
    student1.create_announcements((announcement1))
    
