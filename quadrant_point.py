print("The coordinates of a point:")
x=float(input("x= "))
y= float(input("y= "))

if x>0 and y>0:
    print("THe I Quadrant")
elif x<0 and y>0:
    print("THe II Quadrant")
elif x<0 and y<0:
    print("THe III Quadrant")
elif x>0 and y<0:
    print("The IV Quadrant")

elif x==0 and y==0:
    print("The point is at the origin"
          "of the  CoOrdinate System")
    
elif x==0:
    print("THe point is on the x- axis")
elif y==0:
    print("The point is on the y-axis")
    