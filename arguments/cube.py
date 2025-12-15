def cube(number):
    return number*number*number
def three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(three(9))
print(three(4))