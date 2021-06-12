import math

def conv_min_hr(a):
    global xm
    global zm
    global ym
    zm=0
    ym=0
    xm=a
    a=float(a)
    a=math.trunc(a)
    xm=a
    if a>0:
        xm=int(xm)
        ym=xm//60
        zm=xm-(ym*60)
def conv_hr_min(a):
    global yh
    global sh
    global xh
    xh=a
    xh=float(xh)
    yh=xh*60
    yth=math.trunc(yh)
    sh=(yh-yth)*60
    yh=int(yh)
    sh=int(sh)

a=input("enter number of minutes or hours to convert ")

conv_min_hr(a)
print(xm, "minutes is", ym, "hours, and", zm, "minutes")

conv_hr_min(a)
print(xh, "hours is", yh, "minutes and", sh, "seconds")