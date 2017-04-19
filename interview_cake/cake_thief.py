# Interview Cake: Cake Thief
# https://www.interviewcake.com/question/python/cake-thief
# Miguel Aroca-Ouellette
# 11/10/2016

def max_duffel_bag_value(cake_types, weight_cap):
    """
    Calculates maximum value the duffel bag can hold. Dynamic programming approach.
    Time Complexity: O(n**k) [n is len(cake_types)] [k is the weight_cap]
    Space Complexity: O(k)
    :param cake_types: List of tuples of the form (Weight, Value)
    :param weight_cap: Maximum allowable weight.
    :return: Maximum monetary value given the weight capacity.
    """

    val_cap = [0] * (weight_cap + 1)

    for i in range(1, weight_cap + 1):
        # Find best capacity for each smaller weight cap
        val_cap[i] = val_cap[i - 1]
        for weight, value in cake_types:
            if weight == 0 and value == 0 :
                return float("inf")
            if weight > i:
                continue
            elif (value + val_cap[i - weight]) > val_cap[i]:
                #print value
                val_cap[i] = (value + val_cap[i - weight])

    print [(i, val) for i,val in enumerate(val_cap)][50:]
    return val_cap[-1]

cake_types = [(7, 8), (65, 90), (10,13)]

print max_duffel_bag_value(cake_types, 70)