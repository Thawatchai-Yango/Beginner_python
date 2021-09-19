
St_idBeforeHyphen,st_idAfterHyphen=map(int,input("Enter Student ID = ").split("-"))

if(st_idAfterHyphen % 2) == 0:
   print("{0}".format(St_idBeforeHyphen),end ="")
   print("-{0}".format(st_idAfterHyphen),end ="")
   print(" Your student is Even")
else:
   print("{0}".format(St_idBeforeHyphen),end ="")
   print("-{0}".format(st_idAfterHyphen),end ="")
   print(" Your student ID is Odd")
