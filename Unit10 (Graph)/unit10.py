# The following graph represents the different flights offered by CodePath Airlines. Each node or vertex represents an airport (JFK - New York City, LAX - Los Angeles, DFW - Dallas Fort Worth, and ATL - Atlanta), and an edge between two vertices indicates that CodePath airlines offers flights between those two airports.

# Create a variable flights that represents the undirected graph below as an adjacency dictionary, where each node's value is represented by a string with the airport's name (ex. "JFK").


# """
# JFK ----- LAX
# |
# |
# DFW ----- ATL
# """

# No starter code is provided for this problem
# Add your code here

# create dictionary

flights = {
    'JFK' : ['LAX', 'DFW'],
    'LAX' : ['JFK'],
    'DFW' : ['JFK', 'ATL'],
    'ATL' : ['DFW']
}

# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])

# ['JFK', 'LAX', 'DFW', 'ATL']
# [['LAX', 'DFW'], ['JFK'], ['ATL', 'JFK'], ['DFW']]
# ['LAX', 'DFW']



# Problem 2: There and Back

# As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list flights with n nodes where each node represents the ID of a different destination and flights[i] is an integer array indicating that there is a flight from destination i to each destination in flights[i]. 

# Write a function bidirectional_flights() that returns True if for any flight from a destination i to a destination j there also exists a flight from destination j to destination i.      

# i <--> j True / False 

# Return False otherwise.

def bidirectional_flights(flights):
    connections = set()

    for city, destinations in enumerate(flights):
        for destination in destinations:
            connections.add((city, destination))
    
    for start, destination in connections:
        reverse = (destination, start)
        if reverse not in connections:
            return False
    
    return True

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

# print(bidirectional_flights(flights1))
# print(bidirectional_flights(flights2))

# True
# False



# Problem 3: Finding Direct Flights

# Given an adjacency matrix flights of size n x n where each of the n nodes in the graph represent a distinct destination and n[i][j] = 1 indicates that there exists a flight from destination i to destination j and n[i][j] = 0 indicates that no such flight exists. Given flights and an integer source representing the destination a customer is flying out of, return a list of all destinations the customer can reach from source on a direct flight. You may return the destinations in any order.

# A customer can reach a destination on a direct flight if that destination is a neighbor of source.

def get_direct_flights(flights, source):
    newSources = flights[source]
    
    result = []

    # if element in list contains 1, extract index and append it to result
    # print(newSources)

    for start, destination in enumerate(newSources):
        # print(i)
        if start == 1:
            result.append(destination)
    
    return result

    # return result 

flights = [
            [0, 1, 1, 0], # source 0
            [1, 0, 0, 0], # source 1
            [1, 1, 0, 1], # source 2
            [0, 0, 0, 0]] # source 3

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))
# Example Output:

# [0, 1, 3]
# []