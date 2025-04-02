import pytest 

from app.validacao import CPFValidator
 
def test_cpf_valido():
    assert CPFValidator.validar("529.982.247-25")
    assert CPFValidator.validar("12345678909")

def test_cpf_com_letras():
    assert not CPFValidator.validar("122.024.301-az")
        
def test_cpf_numero_igual():
    assert not CPFValidator.validar("000.000.000-00")
    assert not CPFValidator.validar("11111111111")

def test_cpf_com_formatacao():
    assert CPFValidator.validar("529.982.247-25")
    assert CPFValidator.validar("52998224725")

# with pytest.raises(Valueerror)
# with pytest.raises(TypeError)

