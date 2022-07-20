import time 
import random
from numpy import insert
import pygame

# Insertion sort
def insertionSort(screen, ar):
    for i in range(1, len(ar)):
        while ar[i-1] > ar[i] and i > 0:
            ar[i-1], ar[i] = ar[i], ar[i-1]
            i -= 1
            drawAr(screen, ar)
    return ar

# Bubble sort 
def bubbleSort(ar):
    length = len(ar)
    for i in range(length):
        for j in range(length - i):
            a = ar[j]
            if a != ar[-1]:
                b = ar[j + 1]
                if a > b:
                    ar[j] = b
                    ar[j + 1] = a
    return ar

# Quick Sort 
def quickSort(ar): 
    if len(ar) < 2:
        return ar 
    else: 
        pivot = ar[0]
        less = [i for i in ar[1:] if i <= pivot]
        greater = [i for i in ar[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

def createAr(len):
    ar = []
    for i in range(1, len+1):
        ar.append(i)
    return ar

def drawAr(screen, ar):
    # for ever number in the array, draw a rectangle of the same height
    x_pos = 0
    y_pos = 990
    width = 5
    height = 10

    screen.fill((0, 0, 0))

    # make the rectangle variable
    for num in ar:
        x_pos += width + 1
        # height += num
        # y_pos -= num
        rectangle = pygame.Rect(x_pos, y_pos-num, width, num+height)
        pygame.draw.rect(screen, (255,255,255), rectangle)
        
        # This is what allows things to show up on screen 
        pygame.display.flip()

def main():

    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([1000,1000])

    # Run until the user asks to quit
    LENGTH = 100

    ar = createAr(LENGTH)
    random.shuffle(ar)

    insertionSort(screen, ar)

    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white

        # for num in ar:
        #     x_pos += 10



        # insertStart = time.time()
        # insertionSort(ar)
        # insertEnd = time.time()
        # print(f'The time to do Insertion Sort was: {insertEnd - insertStart}\n')

        # # scramble the recently sorted list
        # random.shuffle(ar)

        # bubbleStart = time.time()
        # bubbleSort(ar)
        # bubbleEnd = time.time()
        # print(f'The time to do Bubble Sort was: {bubbleEnd - bubbleStart}\n')
        
        # # scramble the recently sorted list
        # random.shuffle(ar)

        # quickStart = time.time()
        # quickSort(ar)
        # quickEnd = time.time()
        # print(f'The time to do Quick Sort was {quickEnd - quickStart}\n')


    # time to quit
    pygame.quit()


if __name__ == '__main__':
    main()