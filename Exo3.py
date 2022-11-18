#EXO3 Multiplication de matrice


mA=[[1,2,3],[1,2,3],[1,2,3]]
mB=[[4,5,6],[4,5,6],[4,5,6]]

def multiplication(A,B):
    C=[[],[],[]]
    i=0
    j=0
    while i<=2:
        while j<=2:
            C[i].append(A[i][0]*B[0][j]+A[i][1]*B[1][j]+A[i][2]*B[2][j])
            j+1
        i+1
    return C



print(f"Voici C: {multiplication(mA,mB)}")