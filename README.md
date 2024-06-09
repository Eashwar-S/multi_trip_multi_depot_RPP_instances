# Multi-trip-Algorithm


## Information on the dataset:
The dataset consists of undirected weighted multi-graphs stored in .pkl or .net formats. These undirected graphs form instances for the multi-trip multi-depot rural postman problem which is solved using the multi-trip algortihm. The dataset consists of instances obtained from the literature and also from real-world road networks. Please refer to networkx python package documentation on how use the instances for your own usecase.

## Dataset structure
```
dataset/
    dearmon graph files/   -- .net or .pkl graph files
    dearmon graph info/    -- .npy files containing depot and
                                requirededge information
    real world graph files/
        icy road weather instance graph/       --road network with considering wind conditions
        icy road instance graph/        --road network without considering wind conditions
    real world graph info/    -- .npy files containing depot and
                                requirededge information

```


## Software Required
1. [Python >=3.9](https://www.python.org/downloads/release/python-390/)

## Package Dependencies
1. [Networkx](https://networkx.org/documentation/stable/index.html)


## How to use the dataset
```bash
cd multi_trip_multi_depot_RRP_instances/src
python main.py
```

## References
1. Sathyamurthy, E. (2021). Multi-Flight Algorithms for Multi-UAV Arc Routing Problem (Master's thesis, University of Maryland, College Park).
2. Sathyamurthy, E., Herrmann, J. W., & Azarm, S. (2023). Multi-trip algorithm for multi-depot rural postman problem with rechargeable vehicles. arXiv preprint arXiv:2303.03481.