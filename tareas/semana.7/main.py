if __name__ == "__main__":
    from enum import Enum
    from sport import Sport
    from collections import OrderedDict

    sports = Enum('sports', 'AJEDREZ FUTBOL BALONCESTO ATLETISMO')
    sport = Sport(sports)
    people = range(0, 10)

    print("[[ Encuesta - Deportes populares ]]")

    for person in people:
        print("\nEncuestado #%s" % (person + 1))
        print("Seleccione su deporte favorito\n")

        for s in sports:
            print("%s. %s" % (s.value, s.name))

        choice = input("\n[1-4] ")
        sport.upFav(sport.findById(int(choice)))

    # Implemento una instancia de dict con la ayuda de la clase OrderedDict. Este dict cuenta con los deportes
    # ordenados del mas popular al menos popular.
    favSportsDesc = OrderedDict(sorted(sport.__dict__.items(), key=lambda k: k[1]['favorites'], reverse=True))

    print("\n[[ Resultado ]]")
    print("%s encuentados opinan que los deportes populares son: \n" % len(people))

    for sk in favSportsDesc:
        print(str(sk).capitalize(), "(%s votos)" % favSportsDesc[sk]['favorites'])
