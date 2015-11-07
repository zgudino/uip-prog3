if __name__ == "__main__":
    number = input("Ingrese un numero: ")
    counter = 0

    while counter < int(number):
        counter += 1
        result = (counter * (counter + 1)) / 2

        print("%d - %d" % (counter, result))
