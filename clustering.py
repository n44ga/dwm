import random
import math

def euclidean(p1, p2):

    return math.sqrt(sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))]))

def kmeans(data, k, max_iters=100):
    centroids = random.sample(data, k)
    
    for _ in range(max_iters):    
        clusters = [[] for _ in range(k)]
        
        for point in data:
            distances = [euclidean(point, c) for c in centroids]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(point)
            

        new_centroids = []
        for cluster in clusters:
            if cluster:
                num_dims = len(cluster[0])
                new_centroid = [
                    sum([point[dim] for point in cluster]) / len(cluster) 
                    for dim in range(num_dims)
                ]
                new_centroids.append(new_centroid)
            else:
                new_centroids.append(random.choice(data))
                
        if new_centroids == centroids:
            break
            
        centroids = new_centroids
        
    return clusters, centroids

data = [
    [1, 2], [2, 1], [3, 1],
    [8, 9], [9, 8], [8, 8]
]

clusters, centroids = kmeans(data, k=2)

print("Clusters:", clusters)
print("Centroids:", centroids)
