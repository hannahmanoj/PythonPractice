import sys
count = len(sys.argv)
total = 0
while count > 1:
     count -= 1
     total += float(sys.argv[count])
     avg = (total/float(sys.argv[count]))
if total==0:
    print("no arguments were provided")
else:
    print("Total is", total)
    print("The average is", avg)