class Band:
    instances = []

    def __init__(self, band_name, members):
        self.name = band_name
        self.members = members
        Band.instances.append(self)

    # okay im creating a band and I want to keep track of it in the instances list
    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos
        # return ["face melting guitar solo", "bom bom buh bom", "rattle boom crash"]

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:
    def __init__(self, name="string"):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"


class Guitarist(Musician):
    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"
