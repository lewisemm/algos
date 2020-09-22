def reverse_string(string):
    """
    Using recursion to reverse a string.
    """
    if (len(string) < 2):
        return string
    return reverse_string(string[1::]) + string[0]

# print(reverse_string('recursion'))

def print_array(array, index=0):
    """
    Using recursion to print all the elements of an array.
    """
    if (index >= len(array)):
        return
    print('array[{}] is {}'.format(index, array[index]))
    print_array(array, index + 1)

# array = [3, 4, 1, 8, 2, 6, 5, 7, 9]
# print_array(array)

def is_palindrome(string, left_index, right_index):
    """
    Using recursion to determine if a string is palindrome.
    """
    if len(string) < 1:
        return True
    if string[left_index] != string[right_index]:
        return False
    if left_index == right_index or left_index > right_index:
        return True
    return is_palindrome(string, left_index + 1, right_index - 1)

# string = 'racecar'
# print(is_palindrome(string, 0, len(string) - 1))

path = []
def depth_first_traversal(tree, start, stack=[]):
    """
    Traverses a tree in a depth first manner.
    """
    stack.append(start)
    if tree.get(start) == None:
        path.append(stack[::])
        return stack
    for node in tree.get(start):
        stack = depth_first_traversal(tree, node, stack)
        stack.pop()
    return stack

# tree = {
#     'A': ['B', 'C'],
#     'B': ['D']
# }
# depth_first_traversal(tree, 'A')
# print(path)


path = []
def depth_first_traversal_graph(graph, start, stack=[]):
    """
    Traverses a graph in a depth first manner.
    """
    stack.append(start)
    if graph.get(start) == None:
        path.append(stack[::])
        return stack
    for node in graph.get(start):
        if node in stack:
            path.append(stack[::])
            break
        stack = depth_first_traversal_graph(graph, node, stack)
        stack.pop()
    return stack

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}

depth_first_traversal_graph(graph, 'A')
print(path)
