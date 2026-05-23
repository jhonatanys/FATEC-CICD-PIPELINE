import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest  # noqa: E402
from main import saudacao, calcular_media  # noqa: E402


class TestSaudacao:
    def test_saudacao_nome_valido(self):
        resultado = saudacao("Maria")
        assert "Maria" in resultado

    def test_saudacao_tipo_invalido(self):
        with pytest.raises(TypeError):
            saudacao(123)


class TestCalcularMedia:
    def test_media_simples(self):
        assert calcular_media([10, 8, 6]) == 8.0

    def test_lista_vazia(self):
        with pytest.raises(ValueError):
            calcular_media([])
