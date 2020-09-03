def square(x):
    return x*x
def main():
    for i in range(10):
     #f bilmemne yapmak yerine bu şekilde bağlama da yapabiliriz print olaylarında
        print("{} squared is {}".format(i, square(i)))

    #ayrıca python yukarıdan aşağıya kodu okur yani fonksiyonu yukarıda yazman lazım!

if __name__ == "__main__":
    main()