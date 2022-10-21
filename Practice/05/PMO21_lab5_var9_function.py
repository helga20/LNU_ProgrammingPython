import math
def create_client(coord = [], count = 0):
    print("Введіть координати кожного клієнта.\n"
    "Коли вони закінчаться, просто нічого більш не вводьте і нажміть Enter")
    while True:
        count += 1
        client = input("Введіть координати " + str(count) + " клієнта: ")
        if client == "":
          break
        else:
          coord.append(client)
    for i in range(len(coord)):
        coord[i] = list(map(int, coord[i].split()))

def min_distance_cable(coord = [], count = 0):
    max_x = min_x = coord[0][0]
    max_y = min_y = coord[0][1]

    for i in range(len(coord)):
        if coord[i][0] < min_x:
            min_x = coord[i][0]
        if coord[i][0] > max_x:
            max_x = coord[i][0]
        if coord[i][1] < min_y:
            min_y = coord[i][1]
        if coord[i][1] > max_y:
            max_y = coord[i][1]
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    min_distance = [math.sqrt((center_x - coord[0][0])**2 + \
        (center_y - coord[0][1])**2), 0]

    for i in range(len(coord)):
        if math.sqrt((center_x - coord[i][0])**2 + \
            (center_y - coord[i][1])**2) < min_distance[0]:
            min_distance = [math.sqrt((center_x - coord[i][0])**2\
                 + (center_y - coord[i][1])**2), i]
    center = coord[min_distance[1]]

    length_cable = 0
    for i in range(len(coord)):
        length_cable += math.sqrt((center[0] - coord[i][0]) **2 \
            + (center[1] - coord[i][1])**2)
    print("Мінімальна довжина кабелю буде " + str(length_cable))
