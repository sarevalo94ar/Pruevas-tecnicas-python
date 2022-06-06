theDataOne = "ip vrf"
theDataTwo = " route-target export"
numberDataOne = 0
numberDataTwo = 0
lDataOne = [] 
lDataTwo = []
#print(aDataOne)
f = open("data.txt", "r")
while(True):
    line = f.readline()
    if(line.find(theDataOne) != -1):
        lDataOne.append(line)
        numberDataOne += 1      
    elif(line.find(theDataTwo) != -1):
        lDataTwo.append(line)
        numberDataTwo += 1

    if not line:
        print("The number of matches for data one is:"+str(numberDataOne)+'\n')
        print(lDataOne,"\n")
        print("The number of matches for data two is:"+str(numberDataTwo)+'\n')
        print(lDataTwo,"\n")     
        break
        
f.close()
