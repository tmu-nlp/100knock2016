def chiper(s):
  s = list(s)	
  t = []
  for x in s:
    if x.islower():
      t.append(chr(219 - ord(x)))
    else:
      t.append(x)
  return "".join(t)
  
print(chiper("I am a student."))
print(chiper("I zn z hgfwvmg."))

