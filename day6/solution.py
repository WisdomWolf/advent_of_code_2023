def distance_traveled(held_time, total_time):
    return (total_time - held_time) * held_time


def solution(total_time, distance):
    ways = 0
    for i in range(total_time):
        if distance_traveled(i, total_time) > distance:
            ways += 1
        elif ways > 0:
            break
        return ways