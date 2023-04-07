import math

C = 50
H = 30

def calculateQ(D):
    Q = math.sqrt((2 * C * D) / H)
    return round(Q)

inputstr = int(input())
list = inputstr.split(',')
outputlist = []

for D in list:
    Q = calculateQ(int(D))
    outputlist.append(str(Q))

output=  ','.join(outputlist)
print(output)
