from collections import deque
import datetime


class Factory:
    robots = []
    starting_time = None
    products_on_line = deque()

    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = processing_time
        self.busy_until = self.starting_time

    def get_item(self):
        self.busy_until = self.starting_time + datetime.timedelta(0, self.processing_time)
    @staticmethod
    def adding_time():
        Factory.starting_time += datetime.timedelta(0, 1)


Robots = input().split(";")
hours, minutes, seconds = [int(x) for x in input().split(":")]

Factory.starting_time = datetime.datetime(100, 1, 1, hours, minutes, seconds)
product = input()

while product != "End":
    Factory.products_on_line.append(product)
    product = input()

for robo in Robots:
    name, time = [int(x) if x.isdigit() else x for x in robo.split("-")]
    Factory.robots.append(Factory(name, time))


while Factory.products_on_line:
    Factory.adding_time()
    item = Factory.products_on_line.popleft()

    for robot in Factory.robots:
        if robot.busy_until <= Factory.starting_time:
            robot.get_item()
            print(f"{robot.name} - {item} [{Factory.starting_time.time()}]")
            break

    else:
        Factory.products_on_line.append(item)











