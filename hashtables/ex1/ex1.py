#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i in range(len(weights)):
            hash_table_insert(ht, weights[i], i)
    if len(weights) <= 1:
        print_answer(None)
    elif len(weights) == 2:
        a= weights[0]
        b= weights[1]
        if a + b == limit:
            if a > b:
                answer = (0, 1) #index of a and b
                return answer
            else:
                answer = (1, 0) #index of a and b
                return answer 
        else:
            print_answer(None)     
    else:
        for pair in ht.storage:
            for k in weights:
                a = k
                b = pair.key
                while a + b != limit:
                    print(a)
                    if a > b:
                        c = hash_table_retrieve(ht, a)
                        d = hash_table_retrieve(ht, b)
                        answer = (c, d)
                    else:
                        answer = (d,c)
                return answer
    

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
