import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    position: pygame.Vector2
    velocity: pygame.Vector2
    radius: float

    def __init__(self, x: float, y: float, radius: float):
        # we will be using this later
        containers = getattr(self, "containers", None)
        if containers is not None:
            super().__init__(containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collides_with(self, other) -> bool:
        distance = self.position.distance_to(other.position)
        radius = self.radius + other.radius
        if distance <= radius:
            return True
        else:
            return False

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
