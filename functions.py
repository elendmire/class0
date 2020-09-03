def square(x):
    return x*x
for i in range(10):
   #f bilmemne yapmak yerine bu şekilde bağlama da yapabiliriz print olaylarında
    print("{} squared is {}".format(i, square(i)))