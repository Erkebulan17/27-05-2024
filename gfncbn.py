
# a=4
# while a<5:
#     print("hello")
#     a+=1

# s=0
# while True:
#     if s==3: 
#      break
# print("hi")  
# s+=1

a=[(1,2),(4,5),(5,6),1]
c = 0
b = 0
while True:
      if c >= len(a):
            break
      if type(a[c]) ==tuple:
            b += 1
      c += 1
print(b)
      
     
    
