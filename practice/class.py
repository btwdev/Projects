class student():
    def __init__(self , name , subject , roll_no ,grade):
        self.name = name
        self.subject = subject
        self.roll_no = roll_no
        self.grade = grade

    @staticmethod
    def greet():
        print("Good Morning")

dev = student("dev" , "PCM" , "21" , "A+")
ram = student("ram", "Bio" , "19" , "A")

student.greet()
print(dev.name , dev.subject , dev.roll_no , dev.grade)
print(ram.name , ram.subject , ram.roll_no , ram.grade)