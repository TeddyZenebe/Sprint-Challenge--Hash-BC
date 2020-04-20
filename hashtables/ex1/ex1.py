#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    #Inserts weight and its index into hash table
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    #finds two weights whose sum of weights equals the weight limit
    for j in range(length):
        #the next weight which is required to satsfy the limit
        next_weight = limit-weights[j]
        #get the index of the weight using the function imported
        next_weight_index = hash_table_retrieve(ht, next_weight)
        #if the the next index exist, compare the index value and place in the proper place (large, small)
        if next_weight_index:
            if j > next_weight_index:
                return (j, next_weight_index) 
            else:
                return(next_weight_index, j)  
    return None
    

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
