import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    valor1 = 5
    valor2 = 2

    # when we calculate the sum
    output = methods.soma_calculadora(valor1, valor2)

    # then the sum should be 7
    assert output == 7

def test_subtracao():
    valor1 = 5
    valor2 = 2

    # when we calculate the subtracao
    output = methods.subtracao_calculadora(valor1, valor2)

    # then the sum should be 3
    assert output == 3
    
def test_multiplicacao():
    valor1 = 5
    valor2 = 2

    # when we calculate the multiplicacao
    output = methods.multiplicacao_calculadora(valor1, valor2)

    # then the sum should be 10
    assert output == 10