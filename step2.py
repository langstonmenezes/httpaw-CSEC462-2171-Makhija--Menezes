import re
import random
#test = raw_input("Step 2: Enter the file of type csv:")
test=open('step1.csv')
test2=open('step2.csv','w')

for line in test:
	
        cols = line.split() # split line at whitespace
        ip = cols[0] # get last column
        ip = ip.strip('.') # remove brackets
	
	i=ip+','+line[12:-1]+','+str(random.randint(0,10))
        #print(i) # print the IP address
	test2.write(i)
	test2.write('\n')


test.close()
test2.close()
