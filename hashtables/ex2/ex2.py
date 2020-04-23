#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Insert all flights into hash table
    for i in range(length): 
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    # Get the first destination
    stop_current = hash_table_retrieve(hashtable, "NONE") 
    # Add current dest to return array
    for i in range(length):
        route[i] = stop_current 
        stop_current = hash_table_retrieve(hashtable, stop_current) # Get next destination
    return route[:-1]
