import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 600
screen_height = 400
cell_size = 20
grid_width = screen_width // cell_size
grid_height = screen_height // cell_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Función principal del juego
def main():
    snake = Snake()
    apple = Apple()
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(1, 0)
        
        snake.update()
        
        if snake.check_collision():
            pygame.quit()
            sys.exit()
        
        if snake.eat_apple(apple):
            apple.move()
        
        # Dibujar en la pantalla
        screen.fill(black)
        snake.draw()
        apple.draw()
        pygame.display.update()
        
        clock.tick(10)

# Clase Snake
class Snake:
    def __init__(self):
        self.positions = [(grid_width // 2, grid_height // 2)]
        self.direction = (0, -1)
        self.length = 1
        self.color = green
    
    def change_direction(self, x, y):
        if (x, y) != (-self.direction[0], -self.direction[1]):
            self.direction = (x, y)
    
    def update(self):
        head_x, head_y = self.positions[0]
        new_head = ((head_x + self.direction[0]) % grid_width, (head_y + self.direction[1]) % grid_height)
        
        if new_head in self.positions[2:]:
            return False
        
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()
        
        return True
    
    def check_collision(self):
        head_x, head_y = self.positions[0]
        return head_x < 0 or head_x >= grid_width or head_y < 0 or head_y >= grid_height
    
    def eat_apple(self, apple):
        if self.positions[0] == apple.position:
            self.length += 1
            return True
        return False
    
    def draw(self):
        for position in self.positions:
            rect = pygame.Rect(position[0] * cell_size, position[1] * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, self.color, rect)

# Clase Apple
class Apple:
    def __init__(self):
        self.position = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))
        self.color = red
    
    def move(self):
        self.position = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))
    
    def draw(self):
        rect = pygame.Rect(self.position[0] * cell_size, self.position[1] * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, self.color, rect)

# Ejecutar el juego
if __name__ == '__main__':
    main()
