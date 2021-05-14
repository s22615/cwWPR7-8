n = 100
for i in range(n, -1, -1):
    if i<= 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, ",n,"bottles of beer on the wall...")
    else:
        print(i," bottles of beer on the wall, ",i," bottles of beer")
        print("Take one down, pass it around, ", i-1, " bottles of beer on the wall...")


