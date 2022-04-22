class DisjointSet:
    def __init__(self):
        # maintains mapping of a set's root and the set's size
        self.sets = {}
        # maintains a mapping of nodes and their parent.
        self.parents = {}
    
    def add_edge(self, source, dest):
        """
        Establishes a connection between the set containing source and the set
        containing dest.

        NOTE: source and dest should be the roots of their respective sets.
        """
        # ensure both source and dest are the roots of their respective sets
        if (self.parents.get(source) != None or
                self.parents.get(dest) != None
            ):
            raise Exception(
                "source and dest should be the roots of their respective sets.")
        source_size = self.sets.get(source, 1)
        dest_size = self.sets.get(dest, 1)
        # merge the smaller set to the larger set then delete the smaller set. 
        if source_size >= dest_size:
            self.sets[source] = source_size + dest_size
            if self.sets.get(dest, False):
                self.sets.pop(dest)
            self.parents[dest] = source
        else:
            self.sets[dest] = source_size + dest_size
            if self.sets.get(source, False):
                self.sets.pop(source)
            self.parents[source] = dest
    
    def intersection(self, node1, node2):
        """
        Resolves the root of the sets containing node1 and node2. If they belong
        to the same set, then there is an intersection (and no intersection
        otherwise).

        Returns a tuple where:
        index 0 - contains True/False to indicate whether there is an
            intersection or not.
        index 1 - contains parent of node1, which can be of use to the caller.
        index 2 - contains parent of node2, which can be of use to the caller.
        """
        parent1 = self.find_set_root(node1)
        parent2 = self.find_set_root(node2)
        if parent1 and parent2 and parent1 != parent2:
            return False, parent1, parent2
        return parent1 == parent2, parent1, parent2
    
    def find_set_root(self, node):
        """
        Finds and returns the root of the set in which node belongs.
        """
        current = node
        while self.parents.get(current, None) != None:
            current = self.parents[current]
        return current
