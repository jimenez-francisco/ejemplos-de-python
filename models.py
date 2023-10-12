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

