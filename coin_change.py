def mini(coins,n,amount):
    
    coin_count = 0
    coins.sort()
    coins = coins[::-1]
    ind = 0
    
    change_set = {}
    
    while amount != 0:
        if ind < len(coins):
            if amount>=coins[ind]:
                coin = coins[ind]
                amount -= coins[ind]
                coin_count += 1
                if str(coin) in change_set:
                    change_set[str(coin)] += 1
                else:
                    change_set[str(coin)] = 1
            else:
                ind += 1
        else:
            break
        
    print(change_set)
            
    print(coin_count)
    print(amount)
    
     
    
n = int(input())
coins = list(map(int,input().split()))
amount = int(input())

mini(coins,n,amount)
