class Mtrx:
    def __init__(self,name, n_row, n_col, lst_data):
        a=[]
        # 배열반복문을 통해 행렬을 저장한다.
        for i in n_row:
            for j in n_col:
                a=lst_data[i,j]
        return a
