global_var = 10 

def func():
    ans = 0
    local_var = global_var
    for i in range(1000):
        ans += local_var * i
    return ans

print(func())