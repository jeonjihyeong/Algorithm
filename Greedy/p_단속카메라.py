routes=[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    answer = 0
    routes.sort(key= lambda x: x[1])
    camera=[-30001]
    for s, e in routes:
        temp=set()
        for i in range(s,e+1):
            temp.add(i)
        print(temp)
        a=0
        for j in camera:
            if j in temp:
                a=1
                break
            else: continue
        if a==0:
            camera.append(e)

        answer = len(camera)-1
    return answer

print(solution(routes))  