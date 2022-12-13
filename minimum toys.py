def minimum_toys(prices,n,amount):
    
    toy_count = 0
    prices.sort()
    prices = prices[::-1]
    ind = 0
    
    while amount != 0:
        if ind < n:
            if amount>=prices[ind]:
                amount -= prices[ind]
                toy_count += 1
            else:
                ind += 1
        else:
            break
            
    print(toy_count)
    print(amount)
    
    
    
n = int(input())
prices = list(map(int,input().split()))
amount = int(input())

minimum_toys(prices,n,amount)
