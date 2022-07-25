pass_Number=0
foodList=0


for i in  actions:
    temp = i.split(' ')
    if len(temp)==3:
        act=temp[0]
        key=temp[1]
        password=temp[2]
        if pass_Number ==0:
            if 


        elif pass_Number==1:
            print('false')

    elif len(temp)==2:
        act=temp[0]
        key=temp[1]
    
    else: act=temp[0]


        info_key[a]=temp[0]
    info_password[a]=temp[1]


    if key in info_key:
                    if password in info_password:
                        result.append('true')
                        pass_Number+=1
                    else: result.append('false')
                else: result.append('false')