# File: main.py
# Author: Eashwar Sathyamurthy
# Date: June 09, 2024
# Description: This script containts infomation on how to access the dataset.
# Copyright (c) 2023 Eashwar Sathyamurthy
# MIT License

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
plt.rcParams['figure.dpi'] = 300

def main(instance_name='dearmon', weather=False, plot_graph=False):
    if instance_name == 'dearmon':
        ## For accessing Dearmon instances
        position = list(np.load('../dataset/dearmon graph info/pos.npy', allow_pickle=True))
        nodeColor = list(np.load('../dataset/dearmon graph info/node_color.npy', allow_pickle=True))
        depotNodeColor = list(np.load('../dataset/dearmon graph info/depot_node_color.npy', allow_pickle=True))
        Edges = list(np.load('../dataset/dearmon graph info/edges.npy', allow_pickle=True))
        vehCap = list(np.load('../dataset/dearmon graph info/vehicleCapacity.npy', allow_pickle=True))
        nuNod = list(np.load('../dataset/dearmon graph info/numNodes.npy', allow_pickle=True))
        required_edges = list(np.load('../dataset/dearmon graph info/feasibleRequiredNodes.npy', allow_pickle=True))
        deNo = list(np.load('../dataset/dearmon graph info/depotNodes.npy', allow_pickle=True))
        TotalUAVs = list(np.load('../dataset/dearmon graph info/totalUAVs.npy', allow_pickle=True))
        TotalUAVs = list(np.load('../dataset/dearmon graph info/totalUAVs.npy', allow_pickle=True))

        folderPath = '../dataset/dearmon graph files'

        for i, file in enumerate(os.listdir(folderPath)):        
            if file.endswith(".net"):
                instanceName = file[0:len(file)-4]
                index = int(file.split('.')[0])
                file_path = f"{folderPath}/{file}"
                # G = nx.read_gpickle(file_path)
                G = nx.read_pajek(file_path)
                mapping = {}
                for node in list(G.nodes()):
                    mapping[node] = int(node)
                G = nx.relabel_nodes(G, mapping) # G - multi-undirected unweighted graph

                if plot_graph:
                    plt.figure(figsize=(10, 10))
                    G.add_weighted_edges_from(Edges[index])
                    pos = nx.spring_layout(G)
                    nx.draw(G, pos, node_color=depotNodeColor[index], with_labels=True)
                    nx.draw_networkx_edges(G, pos, edgelist=required_edges[index], edge_color="red")
                    nx.draw_networkx_edge_labels(G, pos, edge_labels={(e1,e2): w for e1, e2, w in Edges[index]})
                    plt.title(f'Graph instance name: {index}.net')
                    plt.show()

    elif instance_name == 'real-world':
        position = list(np.load('../dataset/real world graph info/pos.npy', allow_pickle=True))
        nodeColor = list(np.load('../dataset/real world graph info/node_color.npy', allow_pickle=True))
        depotNodeColor = list(np.load('../dataset/real world graph info/depot_node_color.npy', allow_pickle=True))
        Edges = list(np.load('../dataset/real world graph info/edges.npy', allow_pickle=True))
        vehCap = list(np.load('../dataset/real world graph info/vehicleCapacity.npy', allow_pickle=True))
        nuNod = list(np.load('../dataset/real world graph info/numNodes.npy', allow_pickle=True))
        required_edges = list(np.load('../dataset/real world graph info/feasibleRequiredNodes1.npy', allow_pickle=True))
        deNo = list(np.load('../dataset/real world graph info/depotNodes.npy', allow_pickle=True))
        depotNodesLatLong = list(np.load('../dataset/real world graph info/depotNodesLatLong.npy', allow_pickle=True))
        normalNodesLatLong = list(np.load('../dataset/real world graph info/normalNodesLatLong.npy', allow_pickle=True))
        requiredEdgesID = list(np.load('../dataset/real world graph info/feasibleRequiredEdgesID.npy', allow_pickle=True))
        nonrequiredEdgesID = list(np.load('../dataset/real world graph info/nonrequiredEdgesID.npy', allow_pickle=True))
        dic = list(np.load('../dataset/real world graph info/dic.npy', allow_pickle=True))
        timeStamp = list(np.load('../dataset/real world graph info/timeStamp.npy', allow_pickle=True))
        dicMapList = list(np.load('../dataset/real world graph info/dicMapList.npy', allow_pickle=True))
        if weather:
            folderPath = '../dataset/real world graph files/icy road weather instance graph/'
        else:
            folderPath = '../dataset/real world graph files/new icy road instance graph/'
        actuaLGraphPath = '../dataset/real world graph files/new graph/'
        unfilteredGraphPath = '../dataset/real world graph files/unfiltered new graph/'
        for i, file in enumerate(os.listdir(folderPath), position=0):
            if file.endswith(".pkl"):
                index = int(file.split('.')[0].split('US')[-1])
                instanceName = file[0:len(file)-4]
                file_path = f"{folderPath}/{file}"
                actual_file_path = f"{actuaLGraphPath}/{file}"
                unfiltered_file_path = f"{unfilteredGraphPath}/{file}"
                with open(actual_file_path, 'rb') as f:
                    graph = pickle.load(f)
                # nx.write_pajek(graph, f"{actuaLGraphPath}/{file1}")
                with open(unfiltered_file_path, 'rb') as f:
                    Ugraph = pickle.load(f)
                # nx.write_pajek(Ugraph, f"{unfilteredGraphPath}/{file1}")
                with open(file_path, 'rb') as f:
                    G = pickle.load(f)

                if plot_graph:
                    plt.figure(figsize=(10, 10))
                    G.add_weighted_edges_from(Edges[index])
                    pos = nx.spring_layout(G)
                    nx.draw(G, pos, node_color=depotNodeColor[index], with_labels=True)
                    nx.draw_networkx_edges(G, pos, edgelist=required_edges[index], edge_color="red")
                    nx.draw_networkx_edge_labels(G, pos, edge_labels={(e1,e2): round(w,1) for e1, e2, w in Edges[index]})
                    plt.title(f'Graph instance name: {instance_name}.pkl')
                    plt.show()

if __name__ == "__main__":
    main(instance_name='dearmon', plot_graph=True)       # For plotting dearmon instances
    main(instance_name='real-world', weather=False, plot_graph=True) # For plotting real-world road networks without considering wind directions
    main(instance_name='real-world', weather=True, plot_graph=True)  # With considering wind directions when the graph was generated. This is a directed graph