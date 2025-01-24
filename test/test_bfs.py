# write tests for bfs
import pytest
import networkx as nx
from search import Graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """

    # my test graph
    test_graph = Graph("data/tiny_network.adjlist")
    bmi_fac = 'Luke Gilbert'

    try:
        bfs_test = test_graph.bfs(start=bmi_fac)
    except Exception as e:
        pytest.fail(f"The bfs function failed with: {e}")
        raise

    # check how many nodes there are
    test_len = len(test_graph.get_nodes())
    test_set = set(test_graph.get_nodes())

    # check the length and items in teh set are the same
    assert len(bfs_test) == test_len, "The length is not as expected"
    assert set(bfs_test) == test_set, "The set returned from bfs is not complete"

    # gold standard graph
    nx_graph = nx.read_adjlist("data/tiny_network.adjlist", create_using=nx.DiGraph, delimiter=";")
    # gold standard traversal
    nx_bfs = list(nx.bfs_tree(nx_graph, bmi_fac))
    assert bfs_test == nx_bfs, "The custom bfs does not match the networkx.bfs_tree() output."
    

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    # my test graph
    test_graph = Graph("data/citation_network.adjlist")
    bmi_fac_start = 'Sergio Baranzini'
    bmi_fac_end = 'Atul Butte'

    try:
        bfs_test = test_graph.bfs(start=bmi_fac_start, end=bmi_fac_end)
    except Exception as e:
        pytest.fail(f"The bfs function failed with: {e}")
        raise

    # bad graph tests
    bad_graph = Graph('test/bad_graph.adjlist')
    assert bad_graph.bfs(start='d', end='a') is None, "BFS does not return None when no path exists"
    assert bad_graph.bfs(start='g', end='a') is None, "The node does not exist, yet it did not return 'None'. Curious."


    # gold standard graph
    nx_graph = nx.read_adjlist("data/citation_network.adjlist", create_using=nx.DiGraph, delimiter=";")
    # gold standard shortest path
    nx_short = list(nx.shortest_path(nx_graph, bmi_fac_start, bmi_fac_end))
    # gold standard shortest path
    assert len(bfs_test) == len(nx_short), "The length of the custom BFS shortest path is not the same as that of the networkx.shortest_path()"
    assert bfs_test == nx_short, "The custom BFS method did not find the exact same shortest path as networkx.shortest_path()"
