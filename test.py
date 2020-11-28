
class Raging():

    def __init__(self, name):
        self.name = name.capitalize()

    def check_add(self, num, num2, ans):
        if num + num2 == ans:
            return f"{self.name}, {num} + {num2} = {ans}... nice big brain"
        return f"{self.name}, {num} + {num2} != {ans}... you dumbo go to school"


name = input("Enter your name\n")
add1 = int(input("Pick 1 number\n"))
add2 = int(input("Pick another number\n"))
ans = input(f"""{add1} + {add2} = ?\n""")
c = Raging(name)
print(c.check_add(add1,add2,ans))