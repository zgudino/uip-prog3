from modules.timeutil import minutes, hours, days

if __name__ == "__main__":
    try:
        _seconds = int(input("Ingrese los segundos a transformar: "))

        if not (_seconds is None or _seconds == ""):
            _minutes = minutes(_seconds)
            _hours = hours(_minutes)
            _days = days(_hours)
            print("\nResultado de %d segundos:\n\tDias(%d) \n\tHoras(%d) \n\tMinutos(%d)" % (
                _seconds,
                _days,
                _hours,
                _minutes
            ))

    except IOError as error:
        print(error)
