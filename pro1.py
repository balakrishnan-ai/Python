roll1=["25spcs004","25spcs013"]

roll=input("Enter Roll No: ")
dob=input("Enter your D.O.B : ")



if(roll==roll1 and dob=="30-08-2004"):
    marks=[] #List to store marks
    for i in range(1,6):
        mark=int(input(f"Enter mark{i}: "))
        marks.append(mark)

    tot=sum(marks);
    print("Total : ",tot)

    avg=tot/len(marks)
    print("Percentage : ",avg," %")

    if(avg==100):
        print("You are a Gold Medalist")

    if(avg>=90 and avg<=100):
        print("You get a Distinction ")

    elif(avg>=70 and avg<90):
        print("You got a First Class")

    elif(avg>=60 and avg<70):
        print("You got a Second Class")

    elif(avg>=50 and avg<60):
        print("You got a Third Class")


    else:
        print("Better luck Next time and Study well")
    
    
