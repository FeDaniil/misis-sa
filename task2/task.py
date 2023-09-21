import csv
import argparse
import os
from io import StringIO
from itertools import chain

def read_graph_csv(file):    
    try:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
    except csv.Error:
        raise Exception("Failed to parse the CSV file.")
    
    graph = dict()
    n = 1
    for line in data:
        a, b = int(line[0]), int(line[1])
        n = max(n, a, b)
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph, n


def dfs(v, graph, used, rel3, rel5):
    used.add(v)
    neigh = []
    h = 0
    for u in graph[v]:
        if u not in used:
            neigh.append(u)
            h = max(h, 1 + dfs(u, graph, used, rel3, rel5))
    if h >= 2:
        rel3.append(v)
    if len(neigh) > 1:
        for u in neigh:
            rel5.append(u)
    return h


def get_relationships(graph, n):
    ans = []
    rel3, rel5 = [], []
    dfs(1, graph, set(), rel3, rel5)
    ans.append([i for i in range(1, n + 1) if len(graph[i]) != 1 or i == 1]) # type 1
    ans.append([i for i in range(2, n + 1)]) # type 2
    ans.append(rel3) # type 3
    neigh_1 = set(graph[1])
    ans.append([i for i in range(1, n + 1) if i != 1 and i not in neigh_1]) # type 4
    ans.append(rel5)
    for lst in ans:
        lst.sort()
    return ans


def task(csv_str):
    grah, n = dict(), 0
    with StringIO(csv_str) as f:
        graph, n = read_graph_csv(f)
    print(get_relationships(graph, n))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reads a graph as list of edges in CSV and prints some weird relationships as per the homework task")
    parser.add_argument("file", help="CSV file path")

    args = parser.parse_args() 
    if not os.path.isfile(args.file):
        raise Exception("File does not exist.")
    graph, n = dict(), 0
    with open(args.file) as f:
        graph, n = read_graph_csv(f)
    print(get_relationships(graph, n))
