#There is a bus moving in the city, and it takes and drop some people in each bus stop.
#
# You are provided with a list (or array) of integer arrays (or tuples). Each integer array has two items which represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop.
#
# Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D

PEOPLE_IN = 0
PEOPLE_OUT = 1

def number(bus_stops):
    sleepingPeople = 0
    for stop in bus_stops:
        sleepingPeople += stop[PEOPLE_IN] - stop[PEOPLE_OUT]
    return sleepingPeople

print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))