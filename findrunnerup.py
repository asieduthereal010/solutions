if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))


    maximum = max(arr)
    while maximum in arr:
        arr.remove(maximum)
        
    maximum = max(arr) 
    print(maximum);
