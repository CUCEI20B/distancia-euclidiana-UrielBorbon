import algoritmos

def test_distancia1():
    assert algoritmos.distancetwopoints(7, 5, 4, 1) == 5.0
    print(algoritmos.distancetwopoints(7,5,4,1))

test_distancia1()


def test_distancia2():
    assert algoritmos.distancetwopoints(100, 200, 200, 1) == 222.71281956816046
    print(algoritmos.distancetwopoints(100,200,200,1))

test_distancia2()

def test_distancia3():
    assert algoritmos.distancetwopoints(500, 500, 200, 200) == 424.26406871192853
    print(algoritmos.distancetwopoints(500,500,200,200))

test_distancia3()