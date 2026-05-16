class Vertex:
    def __init__(self):
        self._links = list()

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1: Vertex, v2: Vertex):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value


class LinkedGraph:
    def __init__(self):
        self._links = list()
        self._vertex = list()

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        for l in self._links:
            if (link.v1 == l.v1 and link.v2 == l.v2) or (link.v1 == l.v2 and link.v2 == l.v1):
                return
        self._links.append(link)

        self.add_vertex(link.v1)
        self.add_vertex(link.v2)

        self.set_links_for_vertexes()

    def set_links_for_vertexes(self):
        for vertex in self._vertex:
            for link in self._links:
                if vertex == link.v1 and link.v2 not in vertex._links:
                        vertex._links.append(link.v2)
                if vertex == link.v2 and link.v1 not in vertex._links:
                        vertex._links.append(link.v1)

    def find_path(self, start_v, stop_v):
        ...


class Station(Vertex):
    def __init__(self, name: str):
        self.name = name
        super().__init__()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1: Station, v2: Station, dist: (int, float)):
        self.dist = dist
        super().__init__(v1, v2)


map_metro = LinkedGraph()

v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))
