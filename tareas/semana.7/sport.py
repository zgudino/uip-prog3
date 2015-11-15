class Sport:
    def __new__(cls, enums):
        obj = super(Sport, cls).__new__(cls)

        for e in enums:
            setattr(obj, e.name, {
                'id': e.value,
                'favorites': 0
            })

        return obj

    def findById(self, evals):
        members = self.__dict__

        for member in [members[key] for key in members.keys() if members[key]['id'] == evals]:
            return member

    def upFav(self, eid):
        eid['favorites'] += 1

        return eid
