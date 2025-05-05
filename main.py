import time 
import random
from numpy import insert
import pygame

# Initialize the pygame font 
pygame.font.init()
textFont = pygame.font.SysFont('Arial', 30)

# Insertion sort
def insertionSort(screen, ar):
    # Run the sorting algorithm
    for i in range(1, len(ar)):
        while ar[i-1] > ar[i] and i > 0:
            ar[i-1], ar[i] = ar[i], ar[i-1]
            i -= 1
            drawAr(screen, ar, 'Insertion Sort')
    return ar

# Bubble sort 
def bubbleSort(screen, ar):
    # Run sorting algorithm
    length = len(ar)
    for i in range(length):
        for j in range(length - i):
            a = ar[j]
            if a != ar[-1]:
                b = ar[j + 1]
                if a > b:
                    ar[j] = b
                    ar[j + 1] = a
            drawAr(screen, ar, 'Bubble Sort')
    return ar

# Quick Sort 
def partition(array, low, high, screen):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element 
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1 
            (array[i], array[j]) = (array[j], array[i])

            # Draw after each swap
            drawAr(screen, array, 'Quick Sort', True)

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    
    # Draw after the final swap
    drawAr(screen, array, 'Quick Sort', True)

    return i + 1

def quickSort(array, low, high, screen):
    # Run the algorithm
    if low < high:
        pi = partition(array, low, high, screen)
        quickSort(array, low, pi - 1, screen) 
        quickSort(array, pi + 1, high, screen)

# Array creation
def createAr(len):
    ar = []
    for i in range(1, len+1):
        ar.append(i)
    return ar

# Draw array to the screen
def drawAr(screen, ar, algorithmName, delay=False):

    # Clear only the portion of the screen where the array gets drawn and not the algo name
    screen.fill((0, 0, 0), (0, 50, 1000, 950)) # Clear below thetext 

    # Draw the name of the algorithm once it changes 
    if not hasattr(drawAr, 'lastAlgorithm') or drawAr.lastAlgorithm != algorithmName:
        # Clear the text area 
        screen.fill((0, 0, 0), (0, 0, 1000, 50))
        text = textFont.render(algorithmName, True, (255, 255, 255))
        screen.blit(text, (10,10))

    # only turn on the delay for quick sort
    if delay:
        time.sleep(.01) # incredibly small delay

    # for every number in the array, draw a rectangle of the same height
    x_pos = 0
    y_pos = 990
    width = 4
    height = 100


    # make the rectangle variable
    for num in ar:
        x_pos += width
        rectangle = pygame.Rect(x_pos, y_pos-num, width, num+height)
        pygame.draw.rect(screen, (255, 255, 255), rectangle)
        
    # This is what allows things to show up on screen 
    pygame.display.flip()


def main():

    pygame.init()
    screen = pygame.display.set_mode([1000,1000])

    # Initial draw of a black background 
    screen.fill((0,0,0))
    pygame.display.flip()

    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Run until the user asks to quit
        LENGTH = 250

        # Create the array and randomize
        ar = createAr(LENGTH)
        random.shuffle(ar)

        # insertion sort
        insertStart = time.time()
        insertionSort(screen, ar)
        insertEnd = time.time()
        print(f'\n The time to do Insertion Sort was: {insertEnd - insertStart}\n')

        # reset the array for bubble sort
        random.shuffle(ar)

        # bubble sort
        bubbleStart = time.time()
        bubbleSort(screen, ar)
        bubbleEnd = time.time()
        print(f'The time to do Bubble Sort was: {bubbleEnd - bubbleStart}\n')

        # reset the array for quick sort 
        random.shuffle(ar)

        # quick sort 
        quickStart = time.time()
        quickSort(ar, 0, len(ar) - 1, screen)
        quickEnd = time.time()
        print(f'The time to do a Quick Sort was: {quickEnd - quickStart}\n')


        # All done, end it
        running = False


    # time to quit
    pygame.quit()


if __name__ == '__main__':
    main()