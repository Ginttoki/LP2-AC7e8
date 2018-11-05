from models.models import Cachorro, Gato, Cavalo, VacinadeSuperficie, VacinaIntraMuscular, VacinaIntraVenosa, VacinarCachorro, VacinarGato, VacinarCavalo
from exception.exception import TipoVacinaInvalida
import pytest

def test_vacina_cachorro():
    assert Cachorro('VacinaIntraVenosa')

def test_vacina_gato():
    assert Gato('VacinaIntraMuscular')

def test_vacina_cavalo():
    assert Cavalo('VacinadeSuperficie')

def test_vacinar_cachorro():
    with pytest.raises(TipoVacinaInvalida):
        assert VacinarCachorro('VacinadeSuperficie', 'VacinaIntraVenosa')

def test_vacinar_gato():
    with pytest.raises(TipoVacinaInvalida):
        assert VacinarGato('VacinaIntraVenosa', 'VacinaIntraMuscular')

def test_vacinar_cavalo():
    with pytest.raises(TipoVacinaInvalida):
        assert VacinarCavalo('VacinaIntraMuscular', 'VacinadeSuperficie')