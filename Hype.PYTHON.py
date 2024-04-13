#first_name = 'bro'
#last_name = 'code'
#full_name = first_name +' '+ last_name

#print('meu nome é '+full_name)


#age = 32
#age += 1 
#print("your age is : "+str(age))


#height = 250,5
#print('your height is : '+str(height))
#print(type(height))


#human = True
#print("Are you a human: "+str(human))
#print(type(human))

#nome = 'Bro'
#age = 21
#attractive = True

#nome, age, attractive = 


#spongebob = 30
#Patrick = 30
#Sandy = 30
#squidward = 30
 
#spongebob = Patrick = Sandy = squidward = 30
 
#print(spongebob)
#print(Patrick)
#print(Sandy)
#print(squidward)


#name = 'system'

#print(len(name))
#print(name.find('t'))
#print(name.capitalize())
#print(name.upper())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count('m'))
#print(name.replace('m','a'))
#print(name*3)

#x = 1
#y = 1.2
#z = '3'
#z = int(z)

#print(x)
#print((int(y)))
#print(z*3)


#x = 1
#y = 1.2
#z = '3'


#x = float(x)
#y = float(y)
#z = float(z)

#print('X value is: '+str(x))
#print('y value is: '+str(y))
#print(z*3)



#name = input('what is your name?:')
#age = int(input('How old are you?: '))
#height = float(input('How tall are you?: '))
#age = age + 1

#print('hello '+ name) 
#print('Your agr  '+str(age)+' years old')
#print('You are '+str(height)+"cm tall")
 
 
#pi = 3.14
#x = 1
#y = 2
#z = 3

#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(420))
#print(round (pi))
#print(math.ceil (pi))
#print(math.floor(pi))
#print(max(x,y,z))
#print(min(x,y,z))


 #                indexing[] or slice()
 #                [start:stop:step]
#name = 'bro code'
#first_name = name[0:2:] #o numero indica a posição da letra
#last_name = name[4:]
#full_name = name[0:8:3]
#reversed_name = name[ : :-1] #tudo ao contrario
#print(reversed_name) #variavel 

#website = 'html://google.com'
#website = 'html://wikipedia.com'
#slice = slice(7,-4)
#print(website[slice])


            #IF # ELSE #ELIF6
            

#age = int(input('How old are you:?'))

#if age >= 18: 
    #print ("you are an adult!")
#elif age <= 18:
    #print ("you haven´t been born yet!")   
#else :
    #print('you are an child!')     
    
    
#temp = int(input("What is the temperature outside?:")) 

#if temp >= 0 and temp <= 30:
    #print("the temperature is good today!")
    #print("go outside!")
#elif temp < 0 or temp > 30:
    #print("the temperature is bad today!")
    #print('stay inside!')          
    
                                                              #while loop
#while 1==1:
    #name = print('help i´m stuck in a loop')
    
#while len(name) == 0:
    #name = input("Enter your name: ")
#print("Hello "+name)       
    
                                                            #for loop
#for i in range(10):
   #print(i+1)

#for i in range(50,100+1):
    #print(i)
    
#for i in 'bro code':
    #print(i)    
  
  
    
#import time

#for seconds in range(10,0,-1):     
  #print(seconds)
  #time.sleep(1)
#print('Happy new year!')  
                       
                                                          #nestedloops
      
#rows = int(input("how many rows: "))
#columns = int(input("how many columns: "))
#symbol = input("enter a symbol to use: ")
#for i in range(rows):
    #for j in range(columns):
    # print(symbol, end='')
   # print()                                                                   

                                                       #back   #continue #pass
#while true:
    #name = input("enter your name: ")
    #if name !='':
        #break
    
#phone_number = '123-344-54546'    
#for i in phone_number
 #if i =="-":
    #continue
 #print(i, end='')


#for i in range(1,21)
  #if i ==13:
      #pass
  #else:
      #print(i)
                                                    #list
                      
#food = ['pizza', 'hamburguer', 'hotdog','spaghetti','pudding']
#food[0] = 'sushi'
  #food.remove()
  #food.pop()
  #food.append('ice craear') # acrescentar
  #print(food[0])
  # #food.insert(0,'cacke')
#for x in food:
    #print(x)   
 
                                                     #2D list
#drinks = ['coffee','soda','tea']
#dinner = ['pizza','hamburger','hotdog']
#dessert = ['cake','ice cream']  

#food = [drinks,dinner,dessert]       

#print(food[1][1])                                           
                                                 #TUPLAS

#student = ('Bro ',21,'male') 
#print(student.count('Bro'))
#print(student.index('male'))
#for x in student :
    #print(x)
#if 'Bro' in student:
    #print('bro is here')    
                                            #set

#utensils = {'fork','spoon','knife'}   
#dishes = {'bowl','plate','cup'}  
  
  
#utensils.remove('fork')
#utensils.add('napkin')
#utensils.clear()
#dishes.update(utensils)
#dinner_table = utensils.union(dishes)
#for x in dinner_table:
    #print(x)
                                              #Dictionary
#capitals = {'USA':'WASHIGTON DC',
             #'india':'New Dehli',
             #'china':'beijing',
             #'Russia':'Moscow'}
#1capitals.update({'Germany':'Berlim'})
#2capitals.update({'USA':'las Vegas'})
             
#1print(capitals['Germany'])
#2print(capitals.get('Germany'))
#3print(capitals.keys())

#4for key,value in capitals.items():
    #print(key,value)    
    
                                  #index operador
                                  
#name = 'Bro code'

#1if(name[0].islower()):
    #name = name.capitalize()
#firs_name = name[:3].upper()
#last_bname = name [4:].lower()    
#print(firs_name)
#print(last_bname) 
    
                                  #function
#EX1
#def hello(name):
    #print('Hello!'+name)
    #print('Have a nice day!') 
#hello('bro')

#EX2
#def hello(first_name, last_name,age):
    #print('hello'+first_name+' '+last_name)
    #print('You are '+str(age)+' years old') #age
    #print('have a nice day!')
#hello('Bro','Code',21)                        
    
                                    #Return
#def multiply (number1,number2):
    #result = number1 * number2
    #return = result
#x = multiply(6,8)
#print(x)
                                   #keyword

#def hello (first,middle,last):
    #print('hello '+first+' ' +middle' '+last) 
#hello(middle='code',middle='Dude',first='bro')

                                 #nested functions calls
                                 
#num = input('Enter a whole positive number: ')
#mum = float(num)
#num = abs(num)
#num = round(num)
#print(num)
#print(round(abs(float(input('Enter a whole positive number: ')))))   

                                  #scope
#nome = 'bro' #scope global

#def display_name():
    #name = 'code' #scope local
    #print(name)
#print(name)                                                                 
                                    
                                   #args

#def add (*stuff):
    #sum = 0
    #stuff = list(stuff)
    #stuff[0] = 0 
    #for i in stuff:
        #sum += i 
    #return sum
#print(add(1,2,3,4,5,6,7,8,9))  

#def add (num1,num2):
    # sum = num1 + num2
    # return sum
#print(add(1,2,3))

#def add(*args):
    #sum = 0 
    #for i in args:
        #sum +=1
    #return sum 
#print(add(1,2,3))   
    
#def add(*stuff):
    #sum = 0 
    #stuff = list(stuff)
    #stuff[0] = 0
    #for i in stuff:
        #sum += i
    #return sum 
#print(add(1,2,3,4,5,6,))   
  
                          #kwargs

#def hello (first,last):
    #print('hello ' + first+ ' '+last)
    
#hello (first = 'Bro',middle='Dude',last='code') 

                                                                                                                                                                                           
#def hello (***args, **kwargs):
    #print('hello ' +kwargs ['first']+ ' '+kwargs['last'])
    #print('hello' end='')
    #for ke,value in kwargs.items():
        #print(value, end ='')
    
#hello (first = 'Bro',middle='Dude',last='code')



                           #str.formart
#animal = 'com'
#item = 'moon'

#print('The '+animal+' jumped over the '+item)
#print('The {}jumped over the{}'.format(animal,item)) 
#print('The {1} jumped over the {0}'.format(animal,item)) 
#print('the{animal} jumped over the {animal}'.format(animal='cow',item = 'mon'))  

#text = 'the {} jumped over the {}'
#print(text.format(animal,item))


#number = 1000

#print('the number pi is {:.3}'.format(number)) #100.000
#print('the number is {:,}'.format(number))#1,000
#print('the number is{:b}'.format(number))
#print('the number is {:o}'.format(number))
#print('the number is {:X}'.format(number))
#print('the number is {:E}'.format(number))


                             #import 
#x = random.randint(1,6)   
#y = random.random()

#mylist = ['rock','paper','scissors'] 
#z = random.choice(mylist)

#cards = [1,2,3,4,5,6,7,8,9,'j','Q']

#random.shuffle(cards)
#print (x)

#-------------------------------------------------------------------------------------------------------------------
#try:
    #numerator = int(input('Enter a number to devide:' ))
    #demonimator = int(input('Enter a number to devide by: '))
    #result = numerator / demonimator
#except ZeroDivisionError  as e:        #quando digito o zero
    #print("you can´t divide by zero! idiot!") 
    #print(e)  
#except ValueError as e:                 #quando digito palavras
    #print('Enter only numbers plz')
    #print(e)    
#except Exception:
    #print('something went wrong: ')
#else:
    #print(result)   
#finally:
    #print('this will always execute')      
#----------------------------------------------------------------------------------------------------------------------


#import


#try:
   #with opne ('test.txt') as file:
    #print(file.read())
#print    