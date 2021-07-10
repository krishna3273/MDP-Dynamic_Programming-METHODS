from copy import deepcopy

n, m = map(int, raw_input().split())
reward = [[0] * m for i in range(n)]
for i in range(n):
    reward[i] = map(float, raw_input().split())
e,w=map(int, raw_input().split())
terminals=[[0] * m for i in range(n)]
walls=[[0] * m for i in range(n)]
for i in range(0,e):
    p,q=map(int, raw_input().split())
    terminals[p][q]=1
for i in range(0,w):
    p,q=map(int, raw_input().split())
    walls[p][q]=1
    reward[p][q]=0
start=[0 for x in range(2)]
start=map(int, raw_input().split())
reward1=input()
gamma=0.99
previousreward=[[0 for x in range(m)] for y in range(n)]
prev=0
cnt=0
error=float("inf")
while(error >= 0.01*abs(prev)):
    cnt+=1
#storing previous values for checking wether it has converged
    error = -1000
    previousreward = deepcopy(reward)
    for i in range(0,n):
        for j in range(0,m):
#if it is not a terminal state and not a walls calculate
            if not(terminals[i][j] == 1 or walls[i][j] == 1):
#checking wether it will collide with a walls if this action is taken
                if i>0 and walls[i-1][j]!=1:
                    leftreward = previousreward[i-1][j]
                else:
                    leftreward = previousreward[i][j]
                if i<n-1 and walls[i+1][j]!=1:
                    rightreward = previousreward[i+1][j]
                else:
                    rightreward = previousreward[i][j]
                if j<m-1 and walls[i][j+1]!=1:
                    downreward = previousreward[i][j+1]
                else:
                    downreward = previousreward[i][j]        
                if j>0 and walls[i][j-1]!=1:
                    upreward = previousreward[i][j-1]
                else:
                    upreward = previousreward[i][j]
#selecting which direction gives maximum reward
                ans = 0.8*upreward + 0.1*rightreward + 0.1*leftreward
                if(ans<0.8*downreward + 0.1*rightreward + 0.1*leftreward): ans=0.8*downreward + 0.1*rightreward + 0.1*leftreward
                if(ans<0.8*leftreward + 0.1*upreward + 0.1*downreward): ans=0.8*leftreward + 0.1*upreward + 0.1*downreward
                if(ans<0.8*rightreward + 0.1*upreward + 0.1*downreward): ans=0.8*rightreward + 0.1*upreward + 0.1*downreward

                reward[i][j] = reward1 + gamma * ans
#calculating maximum error among all the states
                if abs(previousreward[i][j] - reward[i][j]) > error:
                    error = abs(reward[i][j] - previousreward[i][j])
                    prev=previousreward[i][j]
    for i in range(n):
        for j in range(m):
            reward[i][j]=round(reward[i][j],3)
    for i in range(n):
        print(reward[i])
    print("\n")   
#checking wether it has converged
    # if error < 0.01*abs(prev):
    #     break            
# print(cnt)
