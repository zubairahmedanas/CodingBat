def date_fashion(you, date):
  # if (2<you <8 or 2<=date <8):
  # 	return 0
  if (you >2 and date>2):
    return 2
  elif (2<you <8 or 2<=date <8):
  	return 0
  else: 
    return 1

print(date_fashion(5, 2))