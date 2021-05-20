from copy import copy
import time

num_items = 4
items = ["book",
         "vacuum",
         "picture",
         "statue",
         ]
values = [10, 100, 70, 80]
weights = [1, 15, 6, 14]
limit = 20
min_val = 120

def item_is_in_knapsack(it, knapsack):
    for i in knapsack:
        if i == it:
            return True
    return False


def end_state(knapsack):
    sum_val = 0
    sum_wei = 0
    for i in knapsack:
        sum_val = sum_val + values[i]
        sum_wei = sum_wei + weights[i]
    if sum_wei <= limit and sum_val > min_val:
        return True
    else:
        return False



def breadth_first_search():
    queue = [[]]
    while True:

        if not queue:
            return False

        knapsack = queue.pop(0)

        if end_state(knapsack):
            print("We have  found a solution!")
            print(knapsack)
            return True


        if not knapsack:
            knapsack_max = -1
        else:
            knapsack_max = max(knapsack)

        for i in range(knapsack_max+1,num_items):
            if not item_is_in_knapsack(i, knapsack):
                son = copy(knapsack)
                son.append(i)
                queue.append(son)


start = time.time()
breadth_first_search()
end = time.time()
print("The total time [ms] of the algorithm is: ")
print(end - start)