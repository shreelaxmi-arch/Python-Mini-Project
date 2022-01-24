m = 0
c = 0
e = 0
s = 0


class create:

    def reg(self, name, price):
        self.name = name
        self.price = price

    def dis(self):
        print("Details are:")
        print("Student Name:", name)
        print("Your Roll No:", price)


name = input("Enter Student Name:")
price = int(input("Enter Roll No:"))


class choice(create):
    def ch(self):
        print("Welcome to IA Test")
        print("Do you want to start enter:1")
        print("Don't want to attend the Test enter:0")
        ch = int(input("Enter your choice:"))
        if (ch == 1):
            f.start(m, c, e, s)
        else:
            f.fail()


class exam(choice):

    def start(self, m, c, e, s):

        print("Welcome to Maths Exam!")
        print("What is the value of 10*10?")
        ans = int(input("Enter your answer:"))
        if ans == 100:
            m = m + 25
        print("What is the value of (2*4)-4?")
        ans = int(input("Enter your answer:"))
        if ans == 4:
            m = m + 25
        print("What is the value of (9/3)?")
        ans = int(input("Enter your answer:"))
        if ans == 3:
            m = m + 25
        print("What is the value of 10*6*2?")
        ans = int(input("Enter your answer:"))
        if ans == 120:
            m = m + 25
        print("You have completed the Maths test.\n")
        print("Welcome to computer Exam!")
        print("What is the long form of CPU?")
        ans = input("Enter your answer:")
        if ans == "Central processing unit":
            c = c + 25
        print("What is the long form of GUI?")
        ans = input("Enter your answer:")
        if ans == "Graphical user interface":
            c = c + 25
        print("What is the long form of ALU?")
        ans = input("Enter your answer:")
        if ans == "Arithmetic logic unit":
            c = c + 25
        print("Who was the father of computer?")
        ans = input("Enter your answer:")
        if ans == "Charles Babbage":
            c = c + 25
        print("you have completed the Computer test.\n")
        print("Welcome to English Exam!")
        print("A prepositional pharse consists of a preposition and its  ---- ?")
        ans = input("Enter your answer:")
        if ans == "Object":
            e = e + 25
        print("phrases are grammatical units that consists of ---- ?")
        ans = input("Enter your answer:")
        if ans == "One or more words":
            e = e + 25
        print("The first letter of first word should be?")
        ans = input("Enter your answer:")
        if ans == "Capital":
            e = e + 25
        print("Every sentence must have a subject and?")
        ans = input("Enter your answer:")
        if ans == "A verb":
            e = e + 25
        print("You have completed English test.\n")
        print("Welcome to Science Exam!")
        print("How many bones are in the human body?")
        ans = int(input("Enter your answer:"))
        if ans == 206:
            s = s + 25
        print("How many vertebrae does the average human possess?")
        ans = int(input("Enter your answer:"))
        if ans == 33:
            s = s + 25
        print("At what temperature are Celiciaus and Farhenheit equals?")
        ans = int(input("Enter your answer:"))
        if ans == -40:
            s = s + 25
        print("How many teeth does an adult human have?")
        ans = int(input("Enter your answer:"))
        if ans == 32:
            s = s + 25
        print("You have completed the Science test")
        f.eligible(m, c, e, s)


class calculate(exam):
    def eligible(self, m, c, e, s):
        if (m >= 50):
            if (c >= 50):
                if (e >= 50):
                    if (s >= 50):
                        f.final(m, c, e, s)
                    else:
                        f.s(s)
                else:
                    f.e(e)
            else:
                f.c(c)
        else:
            f.m(m)


class finalexam(calculate):
    def final(self, m, c, e, s):
        Total = m + c + e + s
        per = Total / 4
        f.dis()
        print("Total maths score:", m)
        print("Total computer score", c)
        print("Total English score:", e)
        print("Total Science score", s)
        print("Total score:", Total)
        print("Percentage:", per)
        print("Congratulation!")

    def m(self, m):
        f.dis()
        print("Maths Score:", m)
        print("Your Maths score is too low.")
        print("You are not eligible for final exam.")

    def c(self, c):
        f.dis()
        print("Computer Score:", c)
        print("Your Computer score is too low.")
        print("You are not eligible for final exam.")

    def e(self, e):
        f.dis()
        print("English Score:", e)
        print("Your English score is too low.")
        print("You are not eligible not for final exam.")

    def s(self, s):
        f.dis()
        print("Science Score:", s)
        print("Your Science score is too low.")
        print("You are not eligible for final exam.")

    def fail(self):
        f.dis()
        print("You haven't attend the IA test.")
        print("You are not eligible for final exam.")


f = finalexam()
f.ch()

