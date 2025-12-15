def victorial(x):
    '''recursive'''
    if x==0 or x==1:
        return 1
    else:
        return x*victorial(x-1)
print(victorial.__doc__)
print("victorial of five",victorial(5))