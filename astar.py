import matplotlib.pyplot as plt


class SearchGraph(Object):

	def __init__(self):
		self.barriers = []
		self.barriers.append([(1,3),(1,4),(1,5),(1,6),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(7,6),(7,5),(7,4),(7,3),(7,2),(6,2),(5,2),(4,2),(3,2),(2,2),(1,2)])


	def heuristic(self, start, goal):
		d=1
		d2=1
		dx = abs(start[0] - goal[0])
		dy = abs(start[1] - goal[1])
		return d * (dx + dy) + (d2-2*d) * min(dx,dy)

	def get_vertex_neighbors(self, pos):
		n = []
		for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]:
			x2 = pos[0] + dx
			y2 = pos[1] + dy
			if x2 < 0 or y2 < 0:
				continue
			n.append((x2,y2))
		return n


	def move_cost(self, a , b):
		for barrier in self.barriers:
			if b in barrier:
				return 100
		return 1

	def A_Star_Search(start, end, graph):
		G = {}
		F = {}


		G[start] = 0
		F[start] = graph.heuristic(start, end)

		closedVertices = set()
		openVertices = set([start])
		cameFrom = {}

		while True:
			current = None
			current_F_Score = None
			for pos in openVertices:
				if current is None or F[pos] < current_F_Score:
					current_F_Score = f[pos]
					current = pos

			if current == end:
				path = [current]
				while current in cameFrom:
					current = cameFrom[current]
					path.append(current)
				path.reverse()
				return path, F[end]

			openVertices.remove(current)
			closedVertices.add(current)


			for neighbor in graph.get_vertex_neighbors(current):
				if neighbor in closedVertices:
					continue
				candidateG = G[current] + graph.move_cost(current,neighbor)

				if neighbor not in openVertices:
					openVertices.add(neighbor)
				elif candidateG >= G[neighbor]:
					continue


				cameFrom[neighbor] = current
				g[neighbor] = candidateG
				H = graph.heuristic(neighbor, end)
				F[neighbor] = G[neighbor] + H

	raise RuntimeError("The algorithm couldn't find a solution")


if __name__=="__main__":
	graph = SearchGraph()
	result, cost = A_Star_Search((0,0), (9,9), graph)
	print("route: ", result)
	print("cost: ", cost)
	plt.plot([v[0] for v  in result], [v[1] for v in result])
	for barrier in graph.barriers:
		plt.plot([v[0] for v  in result], [v[1] for v in result])
	plt.xlim(-1,10)
	plt.ylim(-1,10)
	plt.show()
