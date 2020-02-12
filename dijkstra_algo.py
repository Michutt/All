# dijkstra algorithm
import math


def dijkstra_algo(graph, a_start, a_end):
    used = [str(a_start)]
    values = {item: math.inf for item in graph}
    values["a{}".format(a_start)] = 0

    for i in range(len(graph) - 1):
        a_next = math.inf
        for item, value in graph["a{}".format(a_start)].items():
            if values[item] > values["a{}".format(a_start)] + value:
                values[item] = values["a{}".format(a_start)] + value

        for item in values:
            if a_next >= values[item] and item[1] not in used:
                a_next = values[item]
                a_next_addr = item

        a_start = a_next_addr[1]
        # print(values, "nastepny krok to: ", a_start)
        used.append(a_start)

    return values["a{}".format(a_end)]





# number of apex: {number of neighbour apex : distance between}
graph = {
    "a1": {
        "a2": 10, "a3": 5, "a4": 4
    },
    "a2": {
        "a1": 10, "a4": 3, "a5": 2
    },
    "a3": {
        "a1": 5, "a5": 8, "a6": 10
    },
    "a4": {
        "a1": 4, "a2": 3, "a7": 9
    },
    "a5": {
        "a2": 2, "a3": 8, "a7": 6, "a8": 7
    },
    "a6": {
        "a3": 10
    },
    "a7": {
        "a4": 9, "a5": 6, "a9": 2
    },
    "a8": {
        "a5": 7, "a9": 1
    },
    "a9": {
        "a7": 2, "a8": 1
    }
}


print(dijkstra_algo(graph, 1, 9))

