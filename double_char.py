def double_char(str):
  result = ""
  for i in range (0,len(str),1):
    # print("the values are :",  i,"->",str[i])
    result  = result+ str[i]+ str[i]
    print("the result is", result)

double_char('The')
