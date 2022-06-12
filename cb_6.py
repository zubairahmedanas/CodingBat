def caught_speeding(speed, is_birthday):
  if is_birthday == False and speed<= 60:
    return 0 
  elif is_birthday == False and 61<speed<=80:
    return 1
  elif is_birthday == True and speed<= 65:
    return 0
  elif is_birthday == True and 61<speed<=85:
    return 1
  else:
    return 2