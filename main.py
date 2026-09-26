import pygame
import math

from blackjack_game import BlackjackGame
from button import Button
from deck import Deck


WIDTH, HEIGHT = 1200, 800

def get_player_positions(num_players):
    positions = []

    center_x = WIDTH // 2
    center_y = HEIGHT // 2 + 100

    radius_x = 450
    radius_y = 250

    # Spread players across bottom half of ellipse
    start_angle = math.radians(210)
    end_angle = math.radians(330)

    if num_players == 1:
        angles = [math.radians(270)]
    else:
        angles = [
            start_angle + (end_angle - start_angle) * i / (num_players - 1)
            for i in range(num_players)
        ]

    for angle in angles:
        x = center_x + radius_x * math.cos(angle)
        y = center_y + radius_y * math.sin(angle)
        positions.append((x, y))

    return positions


def draw_hand(screen, card_image, hand, center_x, center_y, dealer_flag=0):

    if not hand:
        return

    card_w, card_h = None, None

    # Figure out card size from the first image we can grab
    sample_key = str(hand.cards[0])
    if sample_key in card_image:
        sample = card_image[sample_key]
        card_w, card_h = sample.get_width(), sample.get_height()
    else:
        card_w, card_h = 80, 120

    overlap = card_w * 0.4
    total_width = card_w + overlap * (len(hand.cards) - 1)
    start_x = center_x - total_width / 2

    for i, card in enumerate(hand.cards):
        key = str(card)
        image = card_image.get(key)
        if image is None:
            continue
        x = start_x + i * overlap
        y = center_y - card_h / 2
        screen.blit(image, (x, y))


game = BlackjackGame()
game.deal()

print(game.dealer)
print(game.players)


pygame.init()

# Display Window
WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

# Images
button_names = ["start", "sim", "settings", "exit", "menu", "deal", "left", "right"]

btn_image = {name: pygame.image.load(f'images/{name}_btn.png').convert_alpha() for name in button_names}
'''
card_image = {f'{rank}_{suit}': pygame.image.load(f'images/cards/{rank}_{suit}.png').convert_alpha() for rank in
              Deck.ranks for suit in Deck.suits}
'''
card_image_scale = 0.6
card_image = {
    f'{rank}_{suit}': pygame.transform.smoothscale(
        pygame.image.load(f'images/cards/{rank}_{suit}.png').convert_alpha(),
        (
            int(pygame.image.load(f'images/cards/{rank}_{suit}.png').get_width() * card_image_scale),
            int(pygame.image.load(f'images/cards/{rank}_{suit}.png').get_height() * card_image_scale)
        )
    )
    for rank in Deck.ranks
    for suit in Deck.suits
}

# Button Instance
start_button = Button(0,100, WIDTH, btn_image["start"])
sim_button = Button(0,250, WIDTH, btn_image["sim"], scale=.5)
settings_button = Button(0,400, WIDTH, btn_image["settings"], scale=.18)
exit_button = Button(0,550, WIDTH, btn_image["exit"])

menu_button = Button(30,30, WIDTH, btn_image["menu"], False,.08)
deal_button = Button(30,HEIGHT - 50, WIDTH, btn_image["deal"], scale=.15)
left_button = Button(WIDTH - 120,HEIGHT - 50, WIDTH, btn_image["left"], False,.08)
right_button = Button(WIDTH - 70,HEIGHT - 50, WIDTH, btn_image["right"], False,.08)

clock = pygame.time.Clock()

# Game Loop
MENU = 0
GAME = 1
SIM = 2

current_screen = MENU

# Dealer position stays fixed near the top of the table
DEALER_X = WIDTH // 2
DEALER_Y = 150

running = True
while running:

    screen.fill((0, 120, 0))

    # ---------------- MENU SCREEN ----------------
    if current_screen == MENU:

        if start_button.draw(screen):
            current_screen = GAME

        if sim_button.draw(screen):
            current_screen = SIM

        if settings_button.draw(screen):
            print("SETTINGS")

        if exit_button.draw(screen):
            running = False

    # ---------------- GAME SCREEN ----------------
    elif current_screen == GAME:

        if menu_button.draw(screen):
            current_screen = MENU

        if deal_button.draw(screen):
            current_screen = MENU

        if left_button.draw(screen):
            current_screen = MENU

        if right_button.draw(screen):
            current_screen = MENU

        # Draw the dealer's hand
        draw_hand(screen, card_image, game.dealer, DEALER_X, DEALER_Y)

        # Draw each player's hand at its seat position
        player_positions = get_player_positions(len(game.players))
        for player, (x, y) in zip(game.players, player_positions):
            for hand in player.hand:  # player.hand is a list of Hand objects (splits)
                draw_hand(screen, card_image, hand, x, y)


    # ---------------- SIM SCREEN ----------------
    elif current_screen == SIM:

        if menu_button.draw(screen):
            current_screen = MENU

        if left_button.draw(screen):
            current_screen = MENU

        if right_button.draw(screen):
            current_screen = MENU

    # ------------------------------------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


'''

import pygame
import math

from blackjack_game import BlackjackGame
from button import Button
from deck import Deck


WIDTH, HEIGHT = 1200, 800

def get_player_positions(num_players):
    positions = []

    center_x = WIDTH // 2
    center_y = HEIGHT // 2 + 100

    radius_x = 450
    radius_y = 250

    # Spread players across bottom half of ellipse
    start_angle = math.radians(210)
    end_angle = math.radians(330)

    if num_players == 1:
        angles = [math.radians(270)]
    else:
        angles = [
            start_angle + (end_angle - start_angle) * i / (num_players - 1)
            for i in range(num_players)
        ]

    for angle in angles:
        x = center_x + radius_x * math.cos(angle)
        y = center_y + radius_y * math.sin(angle)
        positions.append((x, y))

    return positions

game = BlackjackGame()
game.deal()

print(game.dealer)
print(game.players)


pygame.init()

# Display Window
WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

# Images
button_names = ["start", "sim", "settings", "exit", "menu", "deal", "left", "right"]

btn_image = {name: pygame.image.load(f'images/{name}_btn.png').convert_alpha() for name in button_names}
card_image = {f'{rank}_{suit}': pygame.image.load(f'images/cards/{rank}_{suit}.png').convert_alpha() for rank in
              Deck.ranks for suit in Deck.suits}

# Button Instance
start_button = Button(0,100, WIDTH, btn_image["start"])
sim_button = Button(0,250, WIDTH, btn_image["sim"], scale=.5)
settings_button = Button(0,400, WIDTH, btn_image["settings"], scale=.18)
exit_button = Button(0,550, WIDTH, btn_image["exit"])

menu_button = Button(30,30, WIDTH, btn_image["menu"], False,.08)
deal_button = Button(30,HEIGHT - 50, WIDTH, btn_image["deal"], scale=.15)
left_button = Button(WIDTH - 120,HEIGHT - 50, WIDTH, btn_image["left"], False,.08)
right_button = Button(WIDTH - 70,HEIGHT - 50, WIDTH, btn_image["right"], False,.08)

clock = pygame.time.Clock()

# Game Loop
MENU = 0
GAME = 1
SIM = 2

current_screen = MENU

running = True
while running:

    screen.fill((0, 120, 0))

    # ---------------- MENU SCREEN ----------------
    if current_screen == MENU:

        if start_button.draw(screen):
            current_screen = GAME

        if sim_button.draw(screen):
            current_screen = SIM

        if settings_button.draw(screen):
            print("SETTINGS")

        if exit_button.draw(screen):
            running = False

    # ---------------- GAME SCREEN ----------------
    elif current_screen == GAME:
        get_player_positions(len(game.players))

        if menu_button.draw(screen):
            current_screen = MENU

        if deal_button.draw(screen):
            current_screen = MENU

        if left_button.draw(screen):
            current_screen = MENU

        if right_button.draw(screen):
            current_screen = MENU

    # ---------------- SIM SCREEN ----------------
    elif current_screen == SIM:

        if menu_button.draw(screen):
            current_screen = MENU

        if left_button.draw(screen):
            current_screen = MENU

        if right_button.draw(screen):
            current_screen = MENU

        # Draw your blackjack game here
        font = pygame.font.SysFont(None, 60)
        text = font.render("BLACKJACK GAME", True, (255, 255, 255))
        screen.blit(text, (200, 200))

    # ------------------------------------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
'''