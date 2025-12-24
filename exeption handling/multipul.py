try:
    num1,num2=eval(input("enter two numbers:"))
    result=num1/num2
    print("resultis:", result)
except ZeroDivisionError:
    print("division by zero is error!!")
except SyntaxError:
    print("comma is missing , enter 1 or 2")
except:
    print("wrong imput")
else:
    print("no exeptions")
finally:
    print("this will exicute no matter what")