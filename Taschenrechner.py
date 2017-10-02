print("was darfs sein")
print("1-addition")
print("2-subtraktion")
print("3-multiplikation")
print("4-division")
print("5-exponentialrechnung")
print("6-Wurzelrechnung")

n=int(input())

if n==1:
    print("gib eine Zahl ein")
    num1=int(input())
    print("gib eine zweite Zahl ein")
    num2=int(input())
    answer=num1+num2
    print(answer)

elif n==2:
    print("gib eine Zahl ein")
    num1=int(input())
    print("gib eine zweite Zahl ein")
    num2=int(input())
    answer=num1-num2
    print(answer)

elif n==3:
    print("gib eine Zahl ein")
    num1=int(input())
    print("gib eine zweite Zahl ein")
    num2=int(input())
    answer=num1*num2
    print(answer)

elif n==4:
    print("gib eine Zahl ein")
    num1=int(input())
    print("gib eine zweite Zahl ein")
    num2=int(input())
    answer=num1/num2
    print(answer)

elif n==5:
        print("gib die Basis ein")
        num1=int(input())
        print("gib den Exponenten ein")
        num2=int(input())
        answer=num1**num2
        print(answer)

elif n==6:
        print("gib den Radikanten ein")
        num1=int(input())
        print("gib die Wurzel ein")
        num2=int(input())
        num3=1/num2
        answer=num1**num3
        print("Das Ergebnis ist",answer)

else:
    print("*ERROR*")
    print("Bitte gib eine Zahl zwischen 1 und 6 ein")


    end=input()
