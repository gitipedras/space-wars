import pyglet
from pyglet.window import key

# Add window title
window = pyglet.window.Window(width=800, height=600, caption="Space Wars 1.2")

# Load images
background_image = pyglet.image.load('spacewars-wallpaper.png')
logo_image = pyglet.image.load('spacewars-logo.png')

# Center the logo image on the screen
logo_sprite = pyglet.sprite.Sprite(logo_image,
                                    x=(window.width - logo_image.width) // 2,
                                    y=(window.height - logo_image.height) // 2)

# Set background color
background_color = (0, 0, 0, 255)  # RGBA color format

# Create a label for the start game button
start_game_label = pyglet.text.Label('Start Game',
                                     font_name='Comic Neue',
                                     font_size=24,
                                     x=window.width // 2, y=100,
                                     anchor_x='center', anchor_y='center')

# Registering event handlers
@window.event
def on_draw():
    window.clear()
    background_image.blit(0, 0)
    logo_sprite.draw()
    start_game_label.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ENTER:
        start_game()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        if start_game_label.x - start_game_label.content_width // 2 < x < start_game_label.x + start_game_label.content_width // 2 and \
           start_game_label.y - start_game_label.content_height // 2 < y < start_game_label.y + start_game_label.content_height // 2:
            start_game()

def start_game():
    # Execute another Python program
    import subprocess
    subprocess.Popen(['python', 'spacewars.py'])

# Start the application
if __name__ == "__main__":
    pyglet.app.run()

