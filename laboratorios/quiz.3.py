def hundreds(number):
    """
    Retorna la centena de un número entero
    :param number: Numero entero
    :type number: int
    :return:
    :rtype: int
    """
    return int(number / 100) * 100  # Retorna centena


def seconds_to_minute(second):
    """
    Calcula los segundos próximos a llegar al minuto y los minutos transcurridos (Si argumento es mayor a 60 segundos)
    :param second: Argumento en segundos
    :type second: int
    :return:
    :rtype: dict
    """
    time = {
        "seconds_left": 0,
        "minute_enlapsed": 0
    }

    if second > 60:
        # @fix
        # La función abs() corrige un glitch donde si el valor es menor a 100, retorna segundos próximos negativos.
        # Creditos Prof. Abdel Martinez por la solución
        time["seconds_left"] = abs(60 - (second - (hundreds(second))))  # Segundos proximo minuto
        time["minute_enlapsed"] = int(second / 60)  # Minutos transcurridos
    elif second < 60:
        time["seconds_left"] = 60 - second
    elif second == 60:
        time["seconds_left"] = 60

    return time


if __name__ == "__main__":
    counter = 0

    while counter < 5:
        # Al menos el valor ingresado debe ser mayor a cero
        try:
            seconds = int(input("Ingrese los segundos a transformar...\nR: "))

            if seconds <= 0:
                raise ValueError("(EXCEPCION OCURRIDO <ValueError>) Valor ingresado menor igual o menor a cero.")
        except ValueError as ex:
            print(ex)
            break  # Halt completamente el programa

        res = seconds_to_minute(seconds)

        print("(#%s)Han transcurrido %s minutos. Faltan %s segundos para el proximo minutos\n" %
              (
                  counter + 1,
                  res.get("minute_enlapsed"),
                  res.get("seconds_left")
              )
              )

        counter += 1
