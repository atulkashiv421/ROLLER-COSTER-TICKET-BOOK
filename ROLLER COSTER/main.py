'''telling about the roller coster '''


print("Telling me.....")
c = 'y'
    
abc = input("Do you want to ride the roller coster(y/n):")
if abc.lower() == c.lower():
        print("ok then Please tell your age")
    
        
        height= int(input("Your age is: "))
        if height <= 12:
            print("Please pay 7$")
        elif height >= 12 and height<= 18:
            print("Please pay 10$") 
        elif height >18 :
             print("Please pay 15$")
        
        food= input("if you want anthing for eating then i will send you list(y/n): ")
        if food.lower()=='y':
            y = ['1.Burger','2.Puffcorn','3.Drink']
            print("Here is the menu:")
            for item in y:
                print(item)
            ak= int(input("Enter your food number: "))
            if ak == 1:
                print("You selected burger\npay 50$")
            elif ak== 2:
                print("You selected Puffcorn\npay 40$")
            elif ak == 3:
                print("You selected Drink\npay 30$")
            print("Thanks for paying goo and enjoy your ride")
            go=input("Are you ready(y/n)")
        if go.lower() == 'y':
             print("Please take your seat")
        else:
             print("Ok Take your time")
        
        
        
elif abc.lower()=='n':
    print('ok bye')
    
    

      


