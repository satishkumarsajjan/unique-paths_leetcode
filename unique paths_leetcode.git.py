class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lst=[[0 for x in range(0,n)] for y in range(0,m)]
        
        for i in range(0,m):
            lst[i][0]=1
            
        for i in range(0,n):
            lst[0][i]=1
            
        for i in range(1,m):
            for j in range(1,n):
                lst[i][j]=lst[i-1][j]+lst[i][j-1]
                
        return lst[m-1][n-1]
