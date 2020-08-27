let makeGraph = () => {
  let graph = {}

  graph.contains = (node) => {
    return !!graph[node]
  }
  graph.addVertex = (node) => {
    if (!graph.contains(node)) {
      graph[node] = {
        edges: {}
      }
    }
  }
  graph.removeVertex = (node) => {
    if (graph.contains(node)) {
      // first remove any connected edges this node may have.
      for (let connectedNode in graph[node].edges)
        graph.removeEdge(node, connectedNode)
      delete graph[node]
    }
  }
  graph.addEdge = (startNode, endNode) => {
    if (graph.contains(startNode) && graph.contains(endNode)) {
      graph[startNode].edges[endNode] = true
      graph[endNode].edges[startNode] = true
    }
  }
  graph.removeEdge = (startNode, endNode) => {
    if (graph.contains(startNode) && graph.contains(endNode)) {
      delete graph[startNode].edges[endNode]
      delete graph[endNode].edges[startNode]
    }
  }
  return graph
}

let devBook = makeGraph()
devBook.addVertex('James Gosling')
devBook.addVertex('Guido Rossum')
devBook.addVertex('Linus Torvalds')
devBook.addVertex('Michael Olorunnisola')

devBook.addEdge('James Gosling', 'Guido Rossum')
devBook.addEdge('Linus Torvalds', 'Michael Olorunnisola')
console.log(devBook)
devBook.removeEdge('Linus Torvalds', 'Michael Olorunnisola')
console.log(devBook)
devBook.removeVertex('Linus Torvalds')
console.log(devBook)
