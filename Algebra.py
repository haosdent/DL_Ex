import theano
a = theano.tensor.vector() # declare variable
b = theano.tensor.vector() # declare variable
out = a ** 2 + b ** 2 + 2 * a * b # build symbolic expression
f = theano.function([a, b], out)   # compile function
print f([0, 1, 2], [4, 5, 6])  # prints `array([0, 2, 1026])`
