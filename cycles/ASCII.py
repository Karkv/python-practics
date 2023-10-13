# Display in tabular form characters 32 through 127 , inclusive.

for i in range(32,128):
    print(chr(i),end="")
    if(i-1)%10==0:
        print()

print()