class Time:
    
    def __init__(self):
        self.inputs = []

    def add_time(self, hr, min):
        time = [hr,min]
        self.inputs.append(time)

    def addition(self):
        hr = 0
        min = 0
        for x in self.inputs:
            hr += x[0]
            min += x[1]
        if(min >= 60):
            hr += int(min/60)
            min = min - (60*int(min/60))
        print('Addition of Time is {} hours and {} minutes'.format(hr, min))  

    def add_in_min(self):
        min = 0
        for x in self.inputs:
            min += x[0]*60
            min += x[1]
        print('Addition of Time in minutes ',min)    

obj = Time()

print('Enter hour and minute')
hr = int(input())
min = int(input())

obj.add_time(hr, min)

print('Enter hour and minute')
hr = int(input())
min = int(input())

obj.add_time(hr, min)
obj.addition()
obj.add_in_min()