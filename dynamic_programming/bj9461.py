#피보나치랑 비슷
#바로 전 항과 5번째 전 항을 더하면 현재 항을 구할 수 있다
#f(n) = f(n-1) + f(n-5)

arr = [1,1,1,2,2]

def pado(num):
    if num > len(arr):
        for i in range(len(arr), num):
            arr.append(arr[i-1]+arr[i-5])
    return arr[num-1]

n = int(input())
for _ in range(n):
    m = int(input())
    print(pado(m))