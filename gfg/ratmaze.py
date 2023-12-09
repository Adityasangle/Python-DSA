def solve(i,j,a,ans,move,vis,di,dj,n):
    if i==n-1 and j==n-1:
        ans.append(move)
        return
    dir = "DLRU"
    for ind in range(4):
        nexti = i+di[ind]
        nextj = j+dj[ind]
        if nexti>=0 and nextj>=0 and nexti<n and nextj<n and not vis[nexti][nextj] and a[nexti][nextj]==1:
            vis[i][j]=1
            solve(nexti,nextj,a,ans,move+dir[ind],vis,di,dj,n)
            vis[i][j]=0


def findpath(a,n):
    ans = []
    di = [+1,0,0,+1]
    dj = [0,-1,1,0]
    if a[0][0]==1:
        solve(0,0)