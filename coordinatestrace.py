import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Freehand Drawing with Mouse")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Button properties
next_button_rect = pygame.Rect(700, 550, 80, 30)
save_button_rect = pygame.Rect(600, 550, 80, 30)

# Variables to track mouse state and drawing points
drawing = False
points = []
all_drawings = []

# Function to save points to a text file with reduced coordinates
def save_points(points, filename='contourcoordinates.txt'):
    with open(filename, 'w') as f:
        for drawing in points:
            for segment in drawing:
                for point in segment:
                    reduced_point = (point[0] // 3, point[1] // 3)
                    f.write(f'({reduced_point[0]},{reduced_point[1]}),\n')
                f.write('\n')  # Separate segments by a blank line
            f.write('\n')  # Separate drawings by a blank line

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_points(all_drawings)  # Save all drawings when quitting
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if next_button_rect.collidepoint(event.pos):
                    if points:  # Save current points before starting new drawing
                        all_drawings.append(points)
                        points = []
                    print("Next button clicked.")
                    print(f"All drawings: {all_drawings}")
                elif save_button_rect.collidepoint(event.pos):
                    if points:  # Save current points before saving
                        all_drawings.append(points)
                        points = []
                    save_points(all_drawings)  # Save all drawings when clicking Save button
                    print("Save button clicked.")
                    subprocess.Popen(['python', 'epicycle_draw.py'])  # Run the second script
                else:
                    drawing = True
                    points.append([])  # Start a new line segment

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                points[-1].append(event.pos)  # Add the current position to the current segment
                print(f'Current point: {event.pos}')  # Print the current point

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                drawing = False
                points[-1].append(event.pos)  # Add the final position to the current segment
                print(f'Final point: {event.pos}')  # Print the final point

    # Clear the screen
    screen.fill(WHITE)

    # Draw the "Next" button
    pygame.draw.rect(screen, GREEN, next_button_rect)
    font = pygame.font.SysFont(None, 24)
    next_text = font.render('Next', True, BLACK)
    screen.blit(next_text, (next_button_rect.x + 10, next_button_rect.y + 5))

    # Draw the "Save" button
    pygame.draw.rect(screen, GREEN, save_button_rect)
    save_text = font.render('Save', True, BLACK)
    screen.blit(save_text, (save_button_rect.x + 10, save_button_rect.y + 5))

    # Draw all points if there are any
    for segment in points:
        if len(segment) > 1:
            pygame.draw.lines(screen, RED, False, segment, 2)

    # Update the display
    pygame.display.flip()
