n = int(input())

t = 1

while not (t*(t-1)/2  < n < t*(t+1)/2):
    t += 1
    
print(t-1)