import shutil
device = ['','Air conditioner','Light']

i = 1
while i <= 2 :
    print(i, device[i])
    i = i+1

n = int(input("Select the device you want to create. : "))
if n == 1 :
    shutil.copy('Resource/oic.d.airconditioner.json','../example.json')
    print (device[n]," device resource is created.")
elif n == 2 :
    shutil.copy('Resource/oic.d.light.json','../example.json')
    print (device[n]," device resource is created.")
else :
    print ("Please select the correct number.")
