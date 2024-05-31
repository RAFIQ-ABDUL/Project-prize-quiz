player=input("Enter Your Name")
questions=[ ["What is the currency of Denmark?","krone","euro","dollar","dinar"],
    ["What is the capital of Finland?","Berlin","Helsinki","Tokyo","Nairobi"],
    ["What is the smallest planet in our solar system?","Mercury","Jupitar","Venus","Mars"],
    ["How many human players are there on each side in a polo match?","Eight","Six","Four","Eleven"],
    ["How many permanent teeth does a dog have?","40","45","44","42"],
    ["Which European city hosted the 1936 Summer Olympics?","Kentucky","Berlin","Helsinki","Denmark"],
    ["Which southern Italian city is usually credited as the birthplace of the pizza?","Nepals","Argentina","Berlin","Italy"],
    ["What is the capital city of Australia?","Sydeny","Malbourne","Cannbera","Frankfurt"]

]
amount=[1000,2000,3000,4000,5000,6000,7000,8000]
answer=[1,2,1,3]
total=0
for i in range(0,len(questions)//2):
    question=questions[i]
    print(f"\nAmount of {i+1}st question is {amount[i]}")
    print(f"\n{question[0]}\n")
    print(f"(1) {question[1]}\t   (2){question[2]}\t   (3){question[3]}\t   (4){question[4]}")
    answers=int(input("Write your answer 1-4")) 
    if answers==answer[i]:
      print("You won",amount[i])
      total+=amount[i]
    else:
       print("Your answer is wrong") 
    print("Your total at this stage is",total)
print("Congratulation You Won",total,"amount")
for x in range(0,1):
 print("Do You want to continue?")
 print("After this any wrong answer will deduct all your earning if you want to continue write 'y'")
 user=int(input("Enter your answer if yes enter '1'"))
 if user!=1:
   break
 
 for y in range(4,len(questions)):
    question1=questions[y]
    print(f"\nAmount of {y+1}th question is {amount[y]}")
    print(f"\n{question1[0]}\n")
    print(f"(1) {question1[1]}\t   (2){question1[2]}\t   (3){question1[3]}\t   (4){question1[4]}")
    answers1=int(input("Write your answer 1-4")) 
    if answers1==answer[i]:
      print("You won",amount[i])
      total+=amount[i]
    else:
       print("Your answer is wrong") 
       total=0
       print("Alas! You lose all your earning")
       break
    print("Your total at this stage is",total)
print("Congratulation You Won",total,"amount")
 

 




   
        


