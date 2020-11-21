"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('non-existent vertex')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

        # init
        q.enqueue(starting_vertex)

        # while queue isn't empty
        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v)

                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
        
        return visited


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()

        s.push(starting_vertex)

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                print(v)
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

        return visited


    def dft_recursive(self, starting_vertex, path=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # if it is an invalid vertex...
        if starting_vertex is None:
            # do nothing
            return path

        # if the starting vertex is not in our list
        elif starting_vertex not in path:
            # print the starting vertex
            print(starting_vertex)
            # add it to the list
            path.append(starting_vertex)

            # loop through each neighboring node
            for neighbor in self.vertices[starting_vertex]:
                
                self.dft_recursive(neighbor, path)
        
        return path
                



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue a path to the starting vertex
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first PATH
            path = q.dequeue()
			# Grab the last vertex from the PATH
            last_vert = path[-1]
			# If that vertex has not been visited...
            if last_vert not in visited:
				# CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
				  # IF SO, RETURN PATH
                  return path
				# Otherwise Mark it as visited...
                visited.add(last_vert)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_vert):
                    # COPY THE PATH
                    new_path = path.copy()
                    # add the new vertex to it
                    new_path.append(neighbor)
                    # enqueue the new path
                    q.enqueue(new_path)
        return None



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty queue and equeue a path to the starting vertex
        q = Stack()
        q.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first PATH
            path = q.pop()
			# Grab the last vertex from the PATH
            last_vert = path[-1]
			# If that vertex has not been visited...
            if last_vert not in visited:
				# CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
				  # IF SO, RETURN PATH
                  return path
				# Otherwise Mark it as visited...
                visited.add(last_vert)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_vert):
                    # COPY THE PATH
                    new_path = path.copy()
                    # add the new vertex to it
                    new_path.append(neighbor)
                    # enqueue the new path
                    q.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        
        if visited is None:
            # create a set to hold which nodes we have visited
            visited = set()
        
        if path is None:
            # create a list to hold the path that we will
            # ultimately return
            path = [starting_vertex]
        
        # mark starting index as visited
        visited.add(starting_vertex)

        # visit each neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                # create a new path to that node
                new_path = path + [neighbor]

                if neighbor == destination_vertex:
                    # return the new path if it's the value we're searching for
                    return new_path
                # otherwise, call the method recursively using the new path
                # and the new set of visited nodes
                dfs_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)

                # return the path
                if dfs_path is not None:
                    return dfs_path
        
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print('bft')
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('dft')
    graph.dft(1)
    print('dft recursion')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('DFS')
    print(graph.dfs(1, 6))
    print('DFS recursive')
    print(graph.dfs_recursive(1, 6))
