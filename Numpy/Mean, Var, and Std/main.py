import numpy

if __name__ == "__main__":
    n, m = map(int, input().split())
    source = " ".join(input() for _ in range(n))
    matrix1 = numpy.array(source.split(), int)
    matrix1.shape = (n, m)
    
    print(numpy.mean(matrix1, axis = 1))
    print(numpy.var(matrix1, axis = 0))
    print(numpy.std(matrix1, axis = None))