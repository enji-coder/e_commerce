# Starting
import os
s="Quiz Appliation"
new_s=s.center(100)
list2=[]
list3=[]
list4=["a","b","c","d","A","B","C","D"]
print(new_s)
print("Dear Human, this quiz contains 10 Questions")

# Question 1
def ques1():
    print("""
Question 1: Three partners shared the profit in a business in the ratio 5 : 7 : 8. 
They had partnered for 14 months, 8 months and 7 months respectively. What was the ratio of their investments?
a) 5 : 7 : 8                                    c) 38 : 28 : 21
b) 20 : 49 : 64                                 d) None of these
    """)
    a1=input("Enter your answer option: ")
    if a1 in list4:
        a1=a1.lower()
        if a1=="b":
            list2.append("Answer1: Right(+50 points)")
            list3.append(50)
        else:
            list2.append("Answer1: Wrong(-20 points)")
            list3.append(-20)
    else:
        os.system("cls")
        print("Enter proper option")
        ques1()
    os.system("cls")

# Question 2
def ques2():
    print("""
Question 2: Look at this series: 53, 53, 40, 40, 27, 27, ... What number should come next?
a) 12                                           c) 14
b) 27                                           d) 53
    """)
    a2=input("Enter your answer option: ")
    if a2 in list4:
        a2=a2.lower()
        if a2=="c":
            list2.append("Answer2: Right(+50 points)")
            list3.append(50)
        else:
            list2.append("Answer2: Wrong(-20 points)")
            list3.append(-20)
    else:
        os.system("cls")
        print("Enter proper option")
        ques2()
    os.system("cls")

# Question 3
def ques3():
    print("""
Question 3: What is the maximum fine that can be imposed by the government for the misuse of National Emblem?
a) Rs.5 lakh                                    c) Rs.1 lakh
b) Rs.2 lakh                                    d) Rs.4 lakh
    """)
    a3=input("Enter your answer option: ")
    if a3 in list4:
        a3=a3.lower()
        if a3=="a":
            list2.append("Answer3: Right(+50 points)")
            list3.append(50)
        else:
            list2.append("Answer3: Wrong(-20 points)")
            list3.append(-20)
    else:
        os.system("cls")
        print("Enter proper option")
        ques3()
    os.system("cls")

# Question 4
def ques4():
    print("""
Question 4: In which country Blockchain-based carbon trading exchange has been launched?
a) Malaysia                                     c) Singapore
b) Japan                                        d) China
    """)
    a4=input("Enter your answer option: ")
    if a4 in list4:
        a4=a4.lower()    
        if a4=="c":
            list2.append("Answer4: Right(+50 points)")
            list3.append(50)
        else:
            list2.append("Answer4: Wrong(-20 points)")
            list3.append(-20)
    else:
        os.system("cls")
        print("Enter proper option")
        ques4()
    os.system("cls")

# Question 5
def ques5():
    print("""
Question 5: How much GST was collected in the country for the month of October-2019?
a) 95,380 Crore                                 c) 94,916 Crore
b) 105,610 Crore                                d) 92,442 Crore
    """)
    a5=input("Enter your answer option: ")
    if a5 in list4:
        a5=a5.lower()
        if a5=="a":
            list2.append("Answer5: Right(+50 points)")
            list3.append(50)
        else:
            list2.append("Answer5: Wrong(-20 points)")
            list3.append(-20)
    else:
        os.system("cls")
        print("Enter proper option")
        ques5()        
    os.system("cls")

# Question 6
def ques6():
    print("""
Question 6: India has been ranked at which position in the 2019 Ease of Doing Business rankings?
a) 56th                                         c) 68th
b) 63rd                                         d) 78th
    """)
    a6=input("Enter your answer option: ")
    if a6 in list4:
        a6=a6.lower()
        if a6=="b":
            list2.append("Answer6: Right(+50 points)")
            list3.append(50)
        else:
            list2.append("Answer6: Wrong(-20 points)")
            list3.append(-20)
    else:
        os.system("cls")
        print("Enter proper option")
        ques6()
    os.system("cls")

# Question 7
def ques7():
    print("""
Question 7: Which of the following launched India's First Service Audio Service 'Suno'?
a) Netflix                                      c) Facebook
b) Audible                                      d) Hotstar
    """)
    a7=input("Enter your answer option: ")
    if a7 in list4:
        a7=a7.lower()
        if a7=="b":
            list2.append("Answer7: Right(+50 points)")
            list3.append(50)
        else:
            list2.append("Answer7: Wrong(-20 points)")
            list3.append(-20)
    else:
        os.system("cls")
        print("Enter proper option")
        ques7()
    os.system("cls")

# Question 8
def ques8():
    print("""
Question 8: FSSAI to develop app to prevent food wastage in partnership with which company?
a) Google                                       c) Infosys
b) Nasscom Foundation                           d) TCS
    """)
    a8=input("Enter your answer option: ")
    if a8 in list4:
        a8=a8.lower()
        if a8=="b":
            list2.append("Answer8: Right(+50 points)")
            list3.append(50)
        else:
            list2.append("Answer8: Wrong(-20 points)")
            list3.append(-20)
    else:
        os.system("cls")
        print("Enter proper option")
        ques8()
    os.system("cls")

# Question 9
def ques9():
    print("""
Question 9: Scientists from which institute have developed the biggest-ever 
computer chip using carbon nanotubes (CNT)- RV16XNano?
a) Yale University                                     c) Harvard University
b) Massachusetts Institute of Technology (MIT)         d) Stanford University
    """)
    a9=input("Enter your answer option: ")
    if a9 in list4:
        a9=a9.lower()
        if a9=="b":
            list2.append("Answer9: Right(+50 points)")
            list3.append(50)
        else:
            list2.append("Answer9: Wrong(-20 points)")
            list3.append(-20)
    else:
        os.system("cls")
        print("Enter proper option")
        ques9()        
    os.system("cls")

# Question 10
def ques10():
    print("""
Question 10: First night trial of which nuclear capable surface-to-surface 
ballistic missile was carried out recently in India?
a) Prithvi                                     c) Brahmos
b) Agni-III                                    d) Nag
    """)
    a10=input("Enter your answer option: ")
    if a10 in list4:
        a10=a10.lower()
        if a10=="b":
            list2.append("Answer10: Right(+50 points)")
            list3.append(50)
        else:
            list2.append("Answer10: Wrong(-20 points)")
            list3.append(-20)
    else:
        os.system("cls")
        print("Enter proper option")
        ques10()
    os.system("cls")


list1=[ques1(),ques2(),ques3(),ques4(),ques5(),ques6(),ques7(),ques8(),ques9(),ques10()]
for i in list1:
    print(i)

os.system("cls")

print("""
Please find the result below:\n""")
for j in list2:
    print(j)
print()
# sum of list3
Total_points=sum(list3)
print("Total Point=",Total_points)
# 4-5=5 lakh| 3-4=50k | 2-3=20k | 1-2=10k | 0-1=1k  | <0=5 lakh

if Total_points>=400:
    print("Hurray!!! You won ₹5Lakh")
elif Total_points>=300:
    print("Excellent! You won ₹50k")
elif Total_points>=200:
    print("Very Good! You won ₹20k")
elif Total_points>=100:
    print("Good! You won ₹10k")
elif Total_points>=0:
    print("Nice! You won ₹1k")
else:
    print("Oh dear! You need to pay ₹5 Lakh still there is always a next try :)")

# Answers Functions
# Answer1
def ans1():
        print("""
Question 1: Three partners shared the profit in a business in the ratio 5 : 7 : 8. 
They had partnered for 14 months, 8 months and 7 months respectively. What was the ratio of their investments?

Answer: b) 20 : 49 : 64
Explanation:
Let their investments be Rs. x for 14 months, Rs. y for 8 months and Rs. z for 7 months respectively.
Then, 14x : 8y : 7z = 5 : 7 : 8.
Now,	(14x/8y)=(5/7)	       98x = 40y        y =	(49x/20)
And,	(14x/7z)=(5/8)	       112x = 35z       z= (112x/35) =	(16x/5)
 x : y : z = x : (49x/20) : (16x/5)= 20 : 49 : 64.
       """)

# Answer2
def ans2():
        print("""
Question 2: Look at this series: 53, 53, 40, 40, 27, 27, ... What number should come next?

Answer: c) 14 
Explanation:
In this series, each number is repeated, then 13 is subtracted to arrive at the next number.
        """)

# Answer3
def ans3():
        print("""
Question 3: What is the maximum fine that can be imposed by the government for the misuse of National Emblem?

Answer: a) Rs.5 lakh
Explanation:
The Government of India has proposed increasing the fine for illegal and improper use of 
national emblems for commercial gains from Rs.500 to Rs.1 lakh. It also suggested change 
also includes jail time and a fine of Rs.5 lakh for repeat offenders.
        """)

# Answer4
def ans4():
        print("""
Question 4: In which country Blockchain-based carbon trading exchange has been launched?

Answer: c) Singapore
Explanation:
New technology, blockchain-based carbon trading exchange has been launched in Singapore.
This will enable airlines and other corporate buyers to buy and sell tokens approved 
by the International Civil Aviation Organization and supported by carbon offset credits.
        """)

# Answer5
def ans5():
        print("""
Question 5: How much GST was collected in the country for the month of October-2019?

Answer: a) 95,380 Crore
Explanation:
GST collection rose to Rs 95,380 crore in October against Rs 91,916 crore in September,
but it was still 5.29 per cent less in comparison to Rs 1 lakh crore collected in the same month last year.
Tax Collection in October (Rs Crore) is as follows:
CGST: 17,582
SGST: 23,674
IGST: 46,517
Cess: 7,607
        """)

# Answer6
def ans6():
        print("""
Question 6: India has been ranked at which position in the 2019 Ease of Doing Business rankings?

Answer: b) 63rd
Explanation:
India was ranked at the 63rd position in the 2019 Ease of Doing Business rankings. 
The rankings were released by the World Bank.
        """)

# Answer7
def ans7():
        print("""
Question 7: Which of the following launched India's First Service Audio Service 'Suno'?

Answer: b) Audible
Explanation:
Audible, a part of e-commerce giant Amazon, on December 12 launched an India-first audio service 'Suno'. 
Audible Suno-which will be available via a separate Android app - provides free and advertising-free 
access to hundreds of hours of original audio entertainment in Hindi and English.
        """)

# Answer8
def ans8():
        print("""
Question 8: FSSAI to develop app to prevent food wastage in partnership with which company?

Answer: b) Nasscom Foundation
Explanation:
Food regulator FSSAI (Food Safety and Standards Authority of India) and Nasscom Foundation,
a trade association of Indian IT and Business Process Outsourcing industry, have signed 
a Memorandum of Understanding (MoU) to jointly build a technology platform to prevent 
food wastage and encouraging food donation by developing an app for the purpose.
        """)

# Answer9
def ans9():
        print("""
Question 9: Scientists from which institute have developed the biggest-ever 
computer chip using carbon nanotubes (CNT)- RV16XNano?

Answer: b) Massachusetts Institute of Technology (MIT)
Explanation:
Scientists at the Massachusetts Institute of Technology (MIT), Cambridge, USA,
have developed the biggest-ever computer chip using carbon nanotubes (CNT)- RV16XNano. 
This was published in the journal Nature.RV16X-Nano is a 16-bit processor that contains 
14,000 transistors - electronic switches. These switches are made up of CNT - tiny cylinders 
made of rolled-up, atom-thick sheets of graphene.
        """)

# Answer10
def ans10():
        print("""
Question 10: First night trial of which nuclear capable surface-to-surface 
ballistic missile was carried out recently in India?

Answer10: b) Agni-III
Explanation:
First night-trial of the nuclear capable Agni-III surface-to-surface ballistic missile
was carried out from a mobile launcher.The test was carried out at the Integrated Test Range 
at the APJ Abdul Kalam Island off Odisha coast.The missile has a strike range of over 3,500 km.
        """)

print("Please find Q & A of your wrong answers below")
if list3[0]==-20:
    ans1()
print()
if list3[1]==-20:
    ans2()
print()
if list3[2]==-20:
    ans3()
print()
if list3[3]==-20:
    ans4()
print()
if list3[4]==-20:
    ans5()
print()
if list3[5]==-20:
    ans6()
print()
if list3[6]==-20:
    ans7()
print()
if list3[7]==-20:
    ans8()
print()
if list3[8]==-20:
    ans9()
print()
if list3[9]==-20:
    ans10()