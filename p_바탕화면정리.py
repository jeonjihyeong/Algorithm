wallpaper = [".#...", "..#..", "...#."]
minx, miny = 50, 50
maxx, maxy = 0, 0

for i in range(len(wallpaper)):
    for j in range(len(wallpaper[i])):
        if wallpaper[i][j]=='#':
            print(wallpaper[i][j])
            print(i,j)
            print(i+1,j+1)
            if i < miny:
                miny= i
            if j < minx:
                minx= j
            if i >= maxy:
                maxy= i+1
            if j >= maxx:
                maxx= j+1

answer = [miny,minx,maxy,maxx]