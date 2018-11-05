from exception.exception import TipoVacinaInvalida
#Design Pattern Utilizado: Factory Method


class Vacina(object):
    def __init__(self, nomevacina):
        self.nomevacina = nomevacina

    def factory(type):
        if type == 'VacinaIntraVenosa':
            return VacinaIntraVenosa('VacinaIntraVenosa')
        if type == 'VacinaIntraMuscular':
            return VacinaIntraMuscular('VacinaIntraMuscular')
        if type == 'VacinadeSuperficie':
            return VacinadeSuperficie('VacinadeSuperficie')

    factory = staticmethod(factory)

class VacinaIntraVenosa(Vacina):
    def __init__(self, nomevacina):
        Vacina.__init__(self, nomevacina)

class VacinaIntraMuscular(Vacina):
    def __init__(self, nomevacina):
        Vacina.__init__(self, nomevacina)

class VacinadeSuperficie(Vacina):
    def __init__(self, nomevacina):
        Vacina.__init__(self, nomevacina)

class Animal():
    def __init__(self, nome, peso, nomedavacina):
        self.nome = nome
        self.peso = peso
        self.nomedavacina = nomedavacina

    def factory(type):
        if type == 'Cachorro':
            return Cachorro('Cachorro')
        if type == 'Gato':
            return Gato('Gato')
        if type == 'Cavalo':
            return Cavalo('Cavalo')

    factory = staticmethod(factory)

class Cachorro(Animal):
    def __init__(self, nomedavacina):
        Animal.__init__(self, 'Nina', 3,nomedavacina)

    def recebervacina(self):
        return self.nomedavacina

class Gato(Animal):
    def __init__(self, nomedavacina):
        Animal.__init__(self, 'Neko', 3, nomedavacina)

    def recebervacina(self):
        return self.nomedavacina

class Cavalo(Animal):
    def __init__(self, nomedavacina):
        Animal.__init__(self, 'Faisca', 3, nomedavacina)

    def recebervacina(self):
        return self.nomedavacina

class VacinarCachorro(Cachorro, VacinaIntraVenosa):
    def __init__(self, nomedavacina, nomevacina):
        Cachorro.__init__(self, nomedavacina)
        VacinaIntraVenosa.__init__(self, nomevacina)
        if nomevacina != nomedavacina:
           raise TipoVacinaInvalida(nomevacina)
        else:
            return ('Vacina Aplicada')

class VacinarGato(Gato, VacinaIntraMuscular):
    def __init__(self, nomedavacina, nomevacina):
        Gato.__init__(self, nomedavacina)
        VacinaIntraMuscular.__init__(self, nomevacina)
        if nomevacina != nomedavacina:
           raise TipoVacinaInvalida(nomevacina)
        else:
            return ('Vacina Aplicada')

class VacinarCavalo(Cavalo, VacinadeSuperficie):
    def __init__(self, nomedavacina, nomevacina):
        Cavalo.__init__(self, nomedavacina)
        VacinadeSuperficie.__init__(self, nomevacina)
        if nomevacina != nomedavacina:
           raise TipoVacinaInvalida(nomevacina)
        else:
            return ('Vacina Aplicada')

