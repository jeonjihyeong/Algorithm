import sys
input=sys.stdin.readline

infos = ["kim password", "lee abc"]
actions = [
		"ADD 30", 
		"LOGIN kim abc", 
		"LOGIN lee password", 
		"LOGIN kim password", 
		"LOGIN kim password", 
		"LOGIN lee abc", 
		"ADD 30", 
		"ORDER", 
		"ORDER", 
		"ADD 40", 
		"ADD 50" 
] 
info_key=[]
info_password=[]
for i in infos:
    temp=i.split(' ')
    info_key.append(temp[0])
    info_password.append(temp[1])
print(info_key, info_password)

pass_Number=0
foodList=0

def bedal(info_key, info_password,actions):
    pass_Number=0
    foodList=0
    result=[]
    for i in  actions:
        

        temp = i.split(' ')
        if len(temp)==3:
            key=temp[1]
            password=temp[2]
            if pass_Number ==0:
                count=0
                for i in range(len(info_key)):
                    if key==info_key[i]:
                        if password==info_password[i]:
                            count+=1
                        else: continue
                    else: continue
                if count==1:
                    result.append('true')
                else: result.append('false')            
            elif pass_Number==1:
                result.append('false')

        elif len(temp)==2:
            key=temp[1]
            if pass_Number==0:
                result.append('false')
            else:
                result.append('true')
                foodList+=1
        
        else: 
            if foodList >=1:
                result.append('true')
                foodList=0
            else: result.append('false')
    return result


print(bedal(info_key, info_password,actions))









