a="Hello"
print(a)

txt=""" This world shall know pain ,        
Those who do not understand pain
will nerver understand true peace."""    #multiline string
print(txt)              


z="Hello ,World !"                       #string in the python are aarays of bytes 
print(z[7:13])

for x in "Mumbai":                      # for loop through a string
    print(x)


#string LENGTH
print(len(txt))


#check string                       
print("understand " in txt)             #check understand is present or not in txt


#check if Not 
if "God" not in txt:
    print("No,'God'is Not preseent in txt")     #print only if "expensive is NOT present"


# Slicing
print(txt[5:27])
print(z[:5])                  #slice from the start
print(z[7:])                  #slice to the end
print(z[-7:-2])               # Negative Indexing (start from last)

print(z[::-1])                #reverse string from start to end
