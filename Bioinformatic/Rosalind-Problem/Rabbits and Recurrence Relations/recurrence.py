
file = open("rosalind_fib.txt", "r")

data = file.read().strip().split(' ')

# Pull the 
months = int(data[0])

birthRate = int(data[1])


def fib(n, k):
    previous1, previous2 = 1, 1
    for i in range(2, n):
        previous1, previous2 = previous2, previous1 * k + previous2
    return previous2


Rn = fib(months,birthRate)

print("After Month {} months, there will be {} rabbits".format(months, Rn))