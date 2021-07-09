import pytest, forming_magic_square_v3

@pytest.mark.parametrize('entrada, retorno_esperado', [
    ([[5, 3, 4], [1, 5, 8], [6, 4, 2]], 7),
    ([[4, 9, 2], [3, 5, 7], [8, 1, 5]], 1),
    ([[4, 8, 2], [4, 5, 7], [6, 1, 6]], 4),
    ([[4, 9, 2], [3, 5, 7], [8, 1, 6]], 0),
    ([[4, 9, 2], [5, 3, 7], [8, 1, 6]], 4),
    ([[4, 9, 2], [3, 5, 7], [6, 1, 8]], 4),
    ([[4, 9, 2], [3, 5, 7], [1, 8, 6]], 14),
    ([[4, 9, 2], [7, 5, 3], [8, 1, 6]], 8)
])

def test_forming_magic_square(entrada, retorno_esperado):
    assert forming_magic_square_v3.formingMagicSquare(entrada) == retorno_esperado
