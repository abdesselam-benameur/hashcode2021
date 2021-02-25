import random

datasets = [
    "a.txt",
    "b.txt",
    "c.txt",
    "d.txt",
    "e.txt",
    "f.txt"
]


#%%
class Street:
    def __init__(self, start, end, name, duration):
        self.name = name
        self.start = start
        self.end = end
        self.duration = duration
        self.lignt = False
        self.cars = 0

    def __str__(self):
        return "name{%s} start{%s} end{%s} duration{%s}" % (
            self.name, self.start, self.end, self.duration)


class Intersection:
    def __init__(self, id):
        self.id = id
        self.street_on = None
        self.streets_in = {}
        self.streets_out = []


class Car:
    def __init__(self, path):
        self.path = path
        self.position = 0

#%%

# for dataset in datasets:
for dataset in datasets:
    streets = {}
    cars = []
    file = open(dataset)
    D, I, S, V, F = list(map(int, file.readline().strip().split()))
    intersections = [Intersection(i) for i in range(I)]

    for i in range(S):
        line = file.readline().strip().split()
        start = intersections[int(line[0])]
        end = intersections[int(line[1])]
        name = line[2]
        street = Street(start, end, name, int(line[3]))
        streets[name] = street
        start.streets_out.append(street)
        end.streets_in[street.name] = 0

    for i in range(V):
        line = file.readline().strip().split()[1:]
        path = []
        for street in line:
            # path.append(streets[street])
            streets[street].cars += 1
        # car = Car(path)
        # cars.append(car)
        # path[0].cars.append(car)

    file.close()

    # %%

    with open('submissions/{}'.format(dataset), 'w') as file:
        print(I, file=file)
        for i in range(I):
            print(i, file=file)
            streets_in = intersections[i].streets_in
            streets_in = sorted(list(streets_in.keys()), key=lambda e: streets[e].cars, reverse=True)
            print(len(streets_in), file=file)
            n = 4 
            for street in streets_in:
                # n = random.randint(1, 20)
                print(street, n, file=file)     
                if n > 1:
                    n -= 1


#%%

    # for intersection in intersections:
    #     if intersection.street_on != None:
    #         street_cars = streets[intersection.street_on].cars
    #         if len(street_cars) != 0:
    #             car = street_cars.pop(0)
    #             if car.position < len(car.path):
    #                 car.position += 1

    # with open('drafts/intersecations.txt', 'w') as file:
    #     for i in range(I):
    #         print(i, file=file)
    #         print(*intersections[i].streets_in, file=file)
    #         print(*list(map(lambda e: e.name, intersections[i].streets_out)), file=file)