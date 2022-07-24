def xyz_there(str):
	if str[0:3]== "xyz":
		return True
	  for x in range (len(str)-3):
	    if str[x] !='.' and str[x+1 : x+4 ]=="xyz":
	      return True
	return False


print(xyz_there('abcxyz'))