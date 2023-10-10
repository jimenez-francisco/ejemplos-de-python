class User:
    name = None
    email = None

    def send_email(self):
        if self.email is not None:
            print("Sending email to " + self.email)
        else:
            print("Error: No email address provided.")

    def _init_(self, name, email):
        self.name = name
        self.email = email

    def _str_(self):
        return "User: " + self.email

per1 = User("jimenez", "21181@vitual.utsc.edu.mx")
per1.send_email()

class Student(User):
    id = None

    def _init_(self, name=None, email=None, id=None, score=None):
        super()._init_(name, email)
        self.id = id
        self.score = score

    def _str_(self):
        return "Student: " + str(self.id) + "," + self.email

    def is_approved(self):
        return self.score >= 8

student1 = Student("jimenez", "21181@vitual.utsc.edu.mx")
student1.send_email()
student2 = Student(email="francisco2015@outlook.es")
student2.send_email()
print(student1.id, student2.id)

User("jimenez", "21181@vitual.utsc.edu.mx")
print(User)
student1 = Student(name="jimenez", email="21181@vitual.utsc.edu.mx")
print(student1)
User("jimenez", "21181@vitual.utsc.edu.mx")
print(User)
student1 = Student(name="jimenez", email="21181@vitual.utsc.edu.mx")
print(student1)

list1 = ['8901bec5-8e07-4c41-9a55-f5b44a22e536', 'ad62ef52-acdc-41f3-97b3-acc3ccef27fc', 'e07b3196-82f9-40ad-a6d4-99764235ef72']

dict1 = dict()
for i, uuid_str in enumerate(list1):
    dict1[uuid_str] = Student(
        name="student" + str(i),
        email="email" + str(i) + "@ust",
        id=uuid_str
    )
print(dict1)
print(dict1['8901bec5-8e07-4c41-9a55-f5b44a22e536'])

print(dict1)
print(dict1['8901bec5-8e07-4c41-9a55-f5b44a22e536'])

dict2={'8901bec5-8e07-4c41-9a55-f5b44a22e536': Student(name='student0',email='email0@ust', id='8901bec5-8e07-4c41-9a55-f5b44a22e536'), 'ad62ef52-acdc-41f3-97b3-acc3ccef27fc': Student(name='student1',email='email1@ust', id='ad62ef52-acdc-41f3-97b3-acc3ccef27fc'), 'e07b3196-82f9-40ad-a6d4-99764235ef72': Student(name='student2',email='email2@ust', id='e07b3196-82f9-40ad-a6d4-99764235ef72')}
