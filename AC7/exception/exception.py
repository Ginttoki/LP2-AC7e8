class TipoVacinaInvalida(Exception):
    def __init__(self, VacinaCorreta):
        self.VacinaCorreta = VacinaCorreta