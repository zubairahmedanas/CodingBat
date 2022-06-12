def squirrel_play(temp, is_summer):
  if is_summer == False and 60<=temp<=90:
    return True
  elif is_summer == True and 60<= temp <=100:
    return True
  else :
    return False
