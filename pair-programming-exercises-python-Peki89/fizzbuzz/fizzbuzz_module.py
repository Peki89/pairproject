def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
 
        


def main():
    lista = list()
    for i in range(1,101):
        s = fizzbuzz(i)
        lista.append(s)
    
    

    
    
    print(lista)

if __name__ == '__main__':
    main()
