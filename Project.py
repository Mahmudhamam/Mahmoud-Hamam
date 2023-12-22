while True :
      num_1 =  (float(input("enter first number : ")))
      print ("( + ) or " , " ( - ) or " , " ( * ) or " , " ( / ) or " , " ( ^ ) or " , " ( roots(r) ) or" , " ( first number pinary(p) )")
      opp = input ("choose from this operation : " )
      num_2 =  (float(input("enter sacend number : "))) 

      try :
          if opp == '+' :
                print (float( str(num_1 + num_2)))
          if opp == '-' :
                print  (float( str(num_1 - num_2)))
          if opp == '*' :
              
                print(float( str(num_1 * num_2)))
          if opp == '/' :
             
                print (float( str(num_1 / num_2)))
          if opp == '^' :
      
                print (float( str(num_1 ** num_2)))
          while opp == 'r' :
          
                def p (num_1 , num_2) :
                     reslt=1
                     for q in range(num_2) : 
                      reslt += reslt * num_1
                     return num_1**(1/num_2)
                print(p(int((num_1)) ,int((num_2)))) # دي داله عشان نجيب نجيب منها الجزر
                break
          if opp == 'p' :
     
                 def decmil_to_binary (num_1) :
                      
                   binary = ""
                   if num_1 == 0 :
                              binary += "0"
                   while num_1 > 0 :
                              binary = str(num_1 %2) + binary
                              num_1 = num_1 // 2
                   return(binary)
                 print (decmil_to_binary (int(num_1)))
             
      except ZeroDivisionError as err :
                       print (err)
      except ValueError as err2 :
                       print (err2)