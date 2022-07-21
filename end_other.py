def end_other(a, b):
  lower_str = a.lower()
  higher_str = b.lower()
  if len(b)> len(a):
      higher_str=a.lower()
      lower_str= b.lower()
  if higher_str == lower_str[len(lower_str)-len(higher_str):len(lower_str)]:
    return True
  return False
print(end_other('abc', 'abXabc'))