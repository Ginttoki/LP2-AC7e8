from models.models import Cachorro, Gato, Cavalo, VacinadeSuperficie, VacinaIntraMuscular, VacinaIntraVenosa, VacinarCachorro, VacinarGato, VacinarCavalo, Vacina, Animal
from exception.exception import TipoVacinaInvalida
import pytest

def test_factory_cachorro():
    assert Animal.factory('Cachorro')
    assert Cachorro('VacinaIntraVenosa')

def test_factory_gato():
    assert Animal.factory('Gato')
    assert Gato('VacinaIntraMuscular')

def test_factory_cavalo():
    assert Animal.factory('Cavalo')
    assert Cavalo('VacinadeSuperficie')


def test_vacinar_cachorro():
    with pytest.raises(TipoVacinaInvalida):
        assert Vacina.factory('VacinaIntraVenosa')
        assert Animal.factory('Cachorro')
        assert VacinarCachorro('VacinadeSuperficie', 'VacinaIntraVenosa')

def test_vacinar_gato():
    with pytest.raises(TipoVacinaInvalida):
        assert Vacina.factory('VacinaIntraMuscular')
        assert Animal.factory('Gato')
        assert VacinarGato('VacinaIntraVenosa', 'VacinaIntraMuscular')

def test_vacinar_cavalo():
    with pytest.raises(TipoVacinaInvalida):
        assert Vacina.factory('VacinadeSuperficie')
        assert Animal.factory('Cavalo')
        assert VacinarCavalo('VacinaIntraMuscular', 'VacinadeSuperficie')