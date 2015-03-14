######################################################################
# Task 14: Modify the fibo class so that instead of iterating over the
# first n Fibonacci numbers, successive calls iterate over the next n 
# numbersmodify fibo
######################################################################
class fibo:
    '''
        The original code is shown below:
    def __init__(self, n=0):
        self.n = n
        self.x1 = 0
        self.x2 = 1

    def next(self):
        if self.n == 0:
            raise StopIteration
        else:
            self.n = self.n -1
            tmp = self.x1
            self.x1, self.x2 = self.x2, self.x1 + self.x2
        return tmp

    def __iter__(self):
        return self
    '''
    
    
    # every time the count decrease to 0, iterate stops
    # the iteration would not reactivate unless the counter was reset  
    def __init__(self, n=0):
        self.n = n
        self.x1 = 0
        self.x2 = 1
        self.initialCount=n  # remember the counter

    def next(self):
        if self.n == 0:
            self.n=self.initialCount # reset the counter for next iteration
                                     # before raising error
            raise StopIteration
        else:
            self.n = self.n -1
            tmp = self.x1
            self.x1, self.x2 = self.x2, self.x1 + self.x2
            return tmp

    def __iter__(self):
        return self
