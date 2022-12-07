import random
points=0
def rolldice(x):
    global points
    R=random.randint(1,6)
    print("Rolling dice for you: ",R)
    if int(x)==R:
        points=points+1
        print("You won")
        print("You scored :",points,"points")
    else:
        print("Sorry wrong guess")
    t=input("if you wanna Play one more match,(yes/no): ")
    if t not in ["no","n","N","NO"]:
        print("BE READY")
        input_()
    else:
        print("Total points scored :",points)
        print("see you again")
def input_():
    global a
    a=input("Select a number between '1-6' : ")
    if len(a)==1:
        if a.isdigit():
            if int(a) in [1,2,3,4,5,6]:
                rolldice(a)
            else:
                print("Enter digits between '1-6' only")
                input_()
        else:
            print("Enter a valid number")
            input_()
    else:
        print("Enter only single digit number")
        input_()
input_()
