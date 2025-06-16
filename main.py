import time 
import random
from numpy import insert
import pygame

# Initialize the pygame font 
pygame.font.init()
textFont = pygame.font.SysFont('Arial', 30)
#
# Insertion sort
#
def insertionSort(screen, ar):
    # Run the sorting algorithm
    for i in range(1, len(ar)):
        while ar[i-1] > ar[i] and i > 0:
            ar[i-1], ar[i] = ar[i], ar[i-1]
            i -= 1
            drawAr(screen, ar, 'Insertion Sort')
    return ar

#
# Bubble sort 
#
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

#
# Quick Sort 
#
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

#
# Radix Sort
#
def countingSort(array, exp1, screen):
    n = len(array)
    
    # The output array eleements that will have sorted arr 
    output = [0] * n

    # initialize coutn array as 0 
    count = [0] * (10) 

    # Store the count of occurences in count[]
    for i in range(0, n):
        index = (array[i]/exp1) 
        count[int((index) % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array 
    i = n - 1
    while i >= 0:
        index = (array[i] / exp1)
        output[count[int((index) % 10)] - 1] = array[i]
        count[int((index) % 10)] -= 1 
        i -= 1 

    # Copy the output array to array[]
    i = 0 
    for i in range(0, len(array)):
        array[i] = output[i]

    # Draw the array after sorting by this digit
    drawAr(screen, array, 'Radix Sort', True)

    
def radixSort(screen, ar):
    # Find the maximum 
    max1 = max(ar)

    # Do counting sort for every digit 
    exp = 1 
    while max1 // exp > 0:
        countingSort(ar, exp, screen)
        exp *= 10


#
# Array creation
#
def createAr(len):
    ar = []
    for i in range(1, len+1):
        ar.append(i)
    return ar

#
# Draw array to the screen
#
def drawAr(screen, ar, algorithmName, delay=False):
    screen_width, screen_height = screen.get_size()
    
    # Clear only the portion of the screen where the array gets drawn and not the algo name
    screen.fill((0, 0, 0), (0, 50, screen_width, screen_height-50)) # Clear below the text 

    # Draw the name of the algorithm once it changes 
    if not hasattr(drawAr, 'lastAlgorithm') or drawAr.lastAlgorithm != algorithmName:
        # Clear the text area 
        screen.fill((0, 0, 0), (0, 0, screen_width, 50))
        text = textFont.render(algorithmName, True, (255, 255, 255))
        screen.blit(text, (10,10))
        drawAr.lastAlgorithm = algorithmName

    # Calculate dynamic width and spacing based on array length
    max_bar_width = 4  # Maximum width we'd like for bars when array is small
    spacing = 1  # Minimum spacing between bars
    
    # Calculate bar width to fit all bars on screen
    total_bars = len(ar)
    available_width = screen_width - (total_bars * spacing)
    bar_width = max(1, min(max_bar_width, available_width / total_bars))
    
    # Adjust spacing if bars are too thin
    if bar_width < 1:
        bar_width = 1
        spacing = max(0, (screen_width - (total_bars * bar_width)) / total_bars)
    
    # Calculate scaling factor for height
    max_value = max(ar) if ar else 1
    height_scale = (screen_height - 100) / max_value  # Leave some margin at the top
    
    # Draw each bar
    x_pos = 0
    for num in ar:
        bar_height = num * height_scale
        rectangle = pygame.Rect(
            x_pos, 
            screen_height - bar_height,  # Position from bottom
            bar_width, 
            bar_height
        )
        pygame.draw.rect(screen, (255, 255, 255), rectangle)
        x_pos += bar_width + spacing
        
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
        LENGTH = 500

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

        # reset the array for radix sort
        random.shuffle(ar)  

        # radix sort
        radixStart = time.time()
        radixSort(screen, ar)
        radixEnd = time.time()
        print(f'The time to do a Radix Sort was: {radixEnd - radixStart}\n')


        # All done, end it
        running = False


    # time to quit
    pygame.quit()


if __name__ == '__main__':
    main()