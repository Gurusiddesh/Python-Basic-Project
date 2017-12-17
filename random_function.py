import random
random_number = random.randint(1,50)
print("Random Number Generated Between 1-50 ")
print("YOU HAVE THREE CHANCE TO GUESS")
count = 0
while(count<=2):
    user_input = int(input("Enter your guess number : "))
    print(user_input)
    if user_input<random_number:
        print("Failed")
        print("TRY WITH GREATER NUMBER \n")        
                
    elif user_input>random_number:
        print("Failed")
        print("TRY WITH SMALLER NUMBER\n")        
                
    elif user_input==random_number:
        print("Congrats Your Guess was Correct\n")
        print("The Random Number Generated was : ",random_number)
        break
    else:
        print("FAILED")
        print("Random Number Generated was ", random_number)
    count = count+1
input()



    
    
    
        
        
    
    
           
    
        
        
    
    
        
        

 
    


    
        


            
            

    
        
    
    

    











