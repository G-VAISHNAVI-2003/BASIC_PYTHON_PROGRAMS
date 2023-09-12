arr = list(map(int,input().split()))
n = int(input())
arr[:]=arr[n:]+arr[:n]
print(arr)


"""
arr= 1 2 3 4 5
n= 1
output:[2,3,4,5,1]
"""