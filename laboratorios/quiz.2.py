if __name__ == "__main__":
    persons = []
    count = 0


    def checkout(sale):
        if sale >= 500:
            discount = sale - (sale * 0.30)
        elif 500 > sale >= 200:
            discount = sale - (sale * 0.20)
        elif 200 > sale >= 100:
            discount = sale - (sale * 0.10)
        else:
            discount = sale

        return discount


    while count < 5:
        i = count

        print("CLIENTE #%s" % str(i + 1))

        amount = input("Ingrese Total de Venta: ")
        total = checkout(int(amount))

        persons.append({
            "id": i + 1,
            "totalSale": total
        })

        count += 1

    for person in persons:
        print("Venta de Cliente #%s: $%.2d" % (person["id"], person["totalSale"]))
