
# QUE: Print all perfect square numbers from 1 to 500

for i in range(1, 501):
    if i ** 0.5 == int(i ** 0.5):
        print(i)
