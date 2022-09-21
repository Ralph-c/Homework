name1=str(input("Enter a name1 "))
name2=str(input("Enter a name2"))


name_x1=name1[0:name1.find(' ')]
name_m1=name1[name1.find(' ')+1:len(name1)]
name_x2=name2[0:name2.find(' ')]
name_m2=name2[name2.find(' ')+1:len(name2)]

#print(name_m)
#print(name_x)
name1_m=int(len(name_m1)/2)
name2_m=int(len(name_m2)/2)
name1_x=int(len(name_x1)/2)
name2_x=int(len(name_x2)/2)

new_name_x1=name_x1[0:name1_x]+name_x2[name2_x:len(name_x2)]

new_name_x2=name_x2[0:name2_x]+name_x1[name1_x:len(name_x1)]

new_name_m1=name_m1[0:name1_m]+name_m2[name2_m:len(name_m2)]

new_name_m2=name_m2[0:name2_m]+name_m1[name1_m:len(name_m1)]

#name3=name1[0:t]

new_name1=new_name_x1+' '+new_name_m1
new_name2=new_name_x2+' '+new_name_m2

print('This is new name1: ',new_name1)
print('This is new name2: ',new_name2)

#print(name3)