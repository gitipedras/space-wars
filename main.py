import pygame
import webbrowser
class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer / self.time


if __name__ == '__main__':

    my_car = Car()
    print("------------------- Space Wars v1.1 Console ----------------------")
    while True:
        action = input("Welcome to Space Wars v1.2 -- Select an option: [P]lay [Q]uit [G]ithub Project [C]redits :>").upper()
        if action not in "PQGC" or len(action) != 1:
            print("Please select a valid option.")
            continue
        if action == 'P':
            exec(open("spacewarsv1-1.py").read())
        elif action == 'Q':
            quit()
        elif action == 'G':
            webbrowser.open('http://github.com/gitipedras/space-wars')     
        elif action == 'C':
            print("This program was created by Gitipedras with program support by Python, Turtle and Pygame!")
        my_car.step()