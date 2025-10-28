
import random
import math

links = {
    'A': ['B', 'C'],
    'B': ['C', 'A'],
    'C': ['A'],
    'D': ['A', 'B', 'C']
}

pages = list(links.keys())
N = len(pages)
damping = 0.85 # standard damping factor
num_iterations = 100
tolerance = 1e-6 # convergence criterion
ranks = {page: 1.0 / N for page in pages} # Start with equal PageRank for all

def find_sink_nodes(links, pages):
    sinks = []
    for page in pages:
        if not links[page]:
            sinks.append(page)
    return sinks

for it in range(num_iterations):
    new_ranks = {}
    sink_rank = sum(ranks[p] for p in pages if not links[p]) / N # distribute sink PR equally
    
    for page in pages:
        total = 0.0
    
        for possible_linker in pages:
            if page in links[possible_linker]:
                # Add the linker's rank divided by its number of outgoing links
                total += ranks[possible_linker] / len(links[possible_linker])
 
        new_ranks[page] = (1 - damping) / N + damping * (total + sink_rank)

    diff = sum(abs(new_ranks[p] - ranks[p]) for p in pages)
    ranks = new_ranks
    if diff < tolerance:
        break

print("PageRank Result:")
for page in sorted(ranks):
    print(f"{page}: {ranks[page]:.4f}")

