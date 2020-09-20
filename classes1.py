class Flight:
    def __init__(self, origin, destination, duration):
      self.origin = origin
      self.destination = destination
      self.duration = duration
      
def main():
    #Create Flight
    f= Flight(origin="Istanbul", destination="New York", duration=540)

    #Change the value of variable.
    f.duration += 10

    #Print detailes obout flight.
    print(f.origin)
    print(f.destination)
    print(f.duration)

#if im raunning the classes1.py file run the main def. 
if __name__ == "__main__":
    main()