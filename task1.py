def task(number: int):
  """returns the number of bits that are equal to one in the binary representation of that number."""
    
    binary = bin(number)    
    counter = 0
    number1 = binary[2:]
    for i in number1: 
        i = int(i)
        if i == 1:
            counter = counter + 1
    return counter

def main():
    n = int(input("Введіть число "))
    print(task(n))

if __name__ =='__main__':
    main()