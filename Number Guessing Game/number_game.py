from random import randint
def rules():
    print("welcome to number game")
    print("In this game you have to find a random number.\n"+"In this game computer will take a random number.\n"+"You have to find this number.It can be any number in ranga 0 to 100")
    print("You are having some conditions to find the number")
    print("[1] You have only 3 lifes to find the number\n"+"[2] After every option entry you will get wether the given number is smaller or larger")
num=randint(0,100)
lifes=5
rules()
while lifes!=0:
    try:
        print("Lifes reamining "+str(lifes))
        inp_num=int(input("Enter number :"))
        if(num<inp_num):
            print("Selected number is smaller")
            lifes=lifes-1
        if(num>inp_num):
            print("Selected number is bigger")
            lifes=lifes-1
        if(num==inp_num):
            print("Yoah! guess is correct great job")
            break
            exit()
    except:
        print("Enter number correctly")
if(lifes==0):
    print("You are out of lifes\n"+"Game end")
