s = "aabbaccc"

def solution(s):
    answer = len(s)
    string_zip=[]
    for i in range(1,(len(s)//2)+1):
        a= ''
        cnt=1
        tmp=s[:i]
        for j in range(i,len(s),i):
            if s[j:j+i]==tmp:
                cnt+=1
            else:
                if cnt==1:
                    a+=tmp
                else: a+=str(cnt)+tmp
                tmp=s[j:j+i]
                cnt=1
        if cnt==1:
            a+=tmp
        else: a+=str(cnt)+tmp
        string_zip.append(len(a))
    
    result= min(string_zip)
    return result

solution(s)