import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_velocity = pygame.Vector2(0, 0)
gravity = pygame.Vector2(0, 500)  # Adjust gravity strength as needed

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from the last frame
    screen.fill("purple")

    # Apply gravity
    player_velocity += gravity * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_velocity.y = -300
    if keys[pygame.K_s]:
        player_velocity.y = 300
    if keys[pygame.K_a]:
        player_velocity.x = -300
    if keys[pygame.K_d]:
        player_velocity.x = 300

    # Update player position based on velocity
    player_pos += player_velocity * dt

    # Keep the player within the screen boundaries
    player_pos.x = max(0, min(player_pos.x, screen.get_width()))
    player_pos.y = max(0, min(player_pos.y, screen.get_height()))

    pygame.draw.circle(screen, "red", (int(player_pos.x), int(player_pos.y)), 40)

    # flip() the display to put your work on the screen
    pygame.display.flip()

    # limit FPS to 60
    # dt is delta time in seconds since the last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
