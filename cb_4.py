def date_fashion(you, date):
  # if (2<you <8 or 2<=date <8):
  # 	return 0
   if(you <= 2 or date <=2):
  	return 0
  elif (you >=8 or date>=8):
    return 2
  # elif(you <= 2 or date <=2):
  # 	return 0
  else:
  	return 1
  
 

print(date_fashion(2, 9))