from exception.exception import TipoVacinaInvalida
class Vacina():
    def __init__(self, nomevacina):
        self.nomevacina = nomevacina

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

