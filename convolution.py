def convolve(x, h):
    out_length = len(x) + len(h) - 1
    out_signal = []
    
    for i in range(0, out_length):
        sum = 0
        for j in range(0, len(h) - 1):
            if i - j >= 0 and j < len(h) and i - j < len(x):
                #print("i={0} j={1}".format(i,j))
                sum = sum + (h[j] * x[i-j])
        out_signal.append(sum)

    return out_signal


a = [0, 1, 0]
b = [0, .5, 1, .5, 0]
print(a)
print(b)
print("convolved identity")
print(convolve(b, a))
print()
        

c = [1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d = [1,2,3,4,5,7,9,11]
print(c)
print(d)
print("convolved first difference")
print(convolve(c,d))
print()

e = [1,1,1,1,1,1,1,1,1,1]
print(d)
print(e)
print("convolved running sum")
print(convolve(d,e))
print()


h = [1, .7, .5, .3, .1]
i = [.1, -.5, .2, -.3, 1, .7, .5, .3, .1, .2, -.3]
print(h)
print(i)
print("cross-correlation")
h.reverse()
print(convolve(h, i))
