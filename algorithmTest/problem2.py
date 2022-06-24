import sys
from collections import defaultdict 
input=sys.stdin.readline
# grades 에 입력 저장
grades = ["DS7651 A0", "CA0055 D+", "AI5543 C0", "OS1808 B-", "DS7651 B+", "AI0001 F", "DB0001 B-", "AI5543 D+", "DS7651 A+", "OS1808 B-"]
for c in range(len(grades)):
    if len(grades[c])!=9:
        grades[c]=grades[c]+"0"
score=defaultdict(list)
score["A+"]=[13]
score["A0"]=[12]
score["A-"]=[11]
score["B+"]=[10]
score["B0"]=[9]
score["B0"]=[8]
score["C+"]=[7]
score["C0"]=[6]
score["C-"]=[5]
score["D+"]=[4]
score["D0"]=[3]
score["D-"]=[2]
score["F0"]=[1]


def removeRe(grades,score):
    
    result=[]
    for i in range(len(grades)):
        testNumber=[]
        for j in range(len(grades)):
            if j==i:
                continue
            else:
                if grades[i][0:7] != grades[j][0:7]:
                    continue
                else: 
                    testNumber.append(j)
##testNumber 에 아무것도 없으면 중복이 없다는 얘기이기 때문에 grades[i]를 result에 append한다.
        print(testNumber)
        if testNumber == []:
            result.append(grades[i])           
#testNumber에 수가 있으면 그 수와 현재 수를 비교한다.             
        else:
            for f in testNumber: #비교를 하기 위해  score변수 해쉬를 통해 점수를 산출하여 비교함
                
                h=i
                if score[grades[h][7:9]]>score[grades[f][7:9]]:
                    print(grades[h][7:9],grades[f][7:9])
                elif score[grades[h][7:9]]==score[grades[f][7:9]]:
                    print(grades[i])
                    
                else:
                    h=f
                    
            if h==i:
                result.append(grades[i])
            else: continue

    #딕셔너리로 변환했다가 리스트로 되돌리는 방식을 사용하여 중복제거
    result1=dict.fromkeys(result)
    result=list(result1)
    temp=[]
    for i in result:
        temp.append(i.split(' '))
    temp.sort(key=lambda x:x[1])
    print(temp)
    #정렬한 코드를 다시 result 변수에 넣어 합친다. 
    for i in range(len(temp)):
        result[i]=" ".join(temp[i])
    for i in  range(len(result)):
        if result[i][8]=='F':
            result.pop()
        
    return result
print(removeRe(grades,score))