import re
print("Our magical calculator")

ld_result = 0
lb_run = True 

def performMath():
    global ld_result
    global lb_run
    if ld_result == 0:
        ls_equation = input("Enter your equation or print q to exit :")
    else:
        ls_equation = input(str(ld_result))

    if ls_equation == "q":
        print("Thank You!!")
        lb_run = False
    else:
        ls_equation = re.sub('[a-zA-Z,.:" "]','',ls_equation)
        if ld_result == 0:
            ld_result = eval(ls_equation)
            #print("The result is ",ld_result)
        else:
            ld_result = eval(str(ld_result) + ls_equation)
while lb_run:
    performMath()