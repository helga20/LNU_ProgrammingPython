class Route:
    def __init__(self, start, end, distances):
        self.start = start
        self.end = end
        self.distances = distances

    def __str__(self) -> str:
        return f"{self.start} - {self.end} "\
                f"загальної довжини {sum(self.distances)} км "\
                f"з {len(self.distances)-1}-ма привалами"\
                f"({len(self.distances)}-ма переходами)" 

    def get_route_distance(self): # отримання довжини маршруту
        return sum(self.distances)

    def get_stop_number(self): # кількість привалів
        return len(self.distances) - 1

    def __gt__(self, other):
        return self.get_stop_number() > other.get_stop_number()

        
    def get_max_stop(self): # отримання найдовшої дистанції
        return max(self.distances)
  
def print_on(routes_list):
    for r in routes_list:
        print(r)

def routes_max_stop(routes_list): # максимальна к-сть привалів
    routes_l = []
    for r in routes_list:
        if r.get_stop_number() ==  max(routes_list).get_stop_number():
            routes_l.append(r)
    return routes_l

def longest_distance(routes_list): # маршрут з найдовшим переходом
    l_routes = []
    for r in routes_list:
        if r.get_max_stop() == max(routes_list,\
            key=lambda x: x.get_max_stop()).get_max_stop():
            l_routes.append(r)
    return l_routes

def start_in_certain_point(point, routes_list): #з початком у певній точці
    start_l = []
    for r in routes_list:
        if r.start == point:
            start_l.append(r)
    return start_l

def end_in_certain_point(point, routes_list): #з кінцем у певній точці
    end_l = []
    for r in routes_list:
        if r.end == point:
            end_l.append(r)
    return end_l


