def task(number):
    
    binary = bin(number)
    # print(binary)
    counter =0
    for i in binary:
        if (i =="1"):
            counter = counter +1
    print(counter)
n = int(input("Введіть число "))
task(n)
