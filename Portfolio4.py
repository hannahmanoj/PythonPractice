#question1

#num=int(input("enter an integer: "))
#def integer(num):

 #   if num>=0 and num<=100:
  #      print("true")
   # else:
    #    print("false")

#integer(num)

#question2

#string=input("enter a string: ")

#def Uplow(string):
#    countupper=0
 #   countlower=0
  #  for i in string:
   #     if i.isupper():
    #        countupper+=1
     #   elif i.islower():
      #      countlower+=1

    #print("number of uppercase letters: ", countupper)
    #print("number of lowercase letters: ", countlower)
#Uplow(string)

#question3

#str=input("enter your name: ")
#def greetings(str):
 #   newstr=str.capitalize()
  #  print(newstr)

#greetings(str)

#question4

#str=input("enter a string: ")
#def remove(str):
 #   if len(str)<=1:
  #      print(str)
   # else:
    #    print(str[:-1])
#remove(str)


#question5

#centi = eval(input("enter temperature in centigrade: "))
#def convert(centi):
   # newtemp=(centi*9/5)+32
   # print("the temperature in farenheit is ", newtemp)
#convert(centi)

#faren= eval(input("enter temprature in farenheit: "))

#def convt(faren):
   # new=(faren-32)*5/9
   # print("the temperature in centigrade is: ",new)


#convt(faren)

#question6

#centi=input("enter the temperature in centigrade: ")
#def convert(centi):

    #x=float(centi[:-1])
    #newtemp = (x * 9 / 5) + 32
    #print("the temperature in farenheit is ", newtemp,"F")

#convert(centi)


#question7

temp=[]
i=0
for i in range(2):
    temperature=input("enter the temperature")
    temp.insert(i,temperature)
    i=i+1

print(temp)


def maxminmean(temp):

    for j in temp:
        tmplst=[]
        x=float(j[:-1])
        tmplst.insert(x)

    if x==max(tmplst):
        print("the max temp is: ", j)
    elif x==min(tmplst):
        print("the min temp is:",j)
    from statistics import mean
    avg=mean(tmplst)
    print("the average of all the temperatures is: ", avg)


maxminmean(temp)
















