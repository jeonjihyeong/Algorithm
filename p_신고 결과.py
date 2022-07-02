from collections import defaultdict

id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2

def solution(id_list,report, k):
    answer=[]
    report=list(set(report))
    name=[]
    temp_num=0

    for j in range(len(id_list)):
        answer.append(0)
    id_report_list=[]
    id_reporting=defaultdict(list)
    count_report=defaultdict(int)
    for x in id_list:
        count_report[x]=0

    for i in range(len(report)):
        temp = report[i].split(' ')
        id_report_list.append(temp)
        count_report[temp[1]]+=1

    for a,n in id_report_list:
        id_reporting[a].append(n)
    
    for s in id_list:
        if s not in id_list:
            continue
        else:
            if count_report[s]>=k:
                name.append(s)
    print(count_report)
    for m in id_reporting:
        for j in name:
            if j in id_reporting[m]:
                answer[temp_num]+=1
        temp_num+=1
    print(answer)
    return answer

solution(id_list, report, k)