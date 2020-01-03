import sys

sys.path.insert(0, '../../')

import os
import pygame
import pygameMenu

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (228, 100, 36)
WINDOW_SIZE = (480, 640)

surface = None
main_menu = None


def main_background():
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.
    :return: None
    """
    global surface
    surface.fill((40, 40, 40))


def main():
    global main_menu
    global surface

    # Init pygame
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    # Create pygame screen and objects
    surface = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Test")
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Create menus
    # -------------------------------------------------------------------------

    # Settings menu
    note_training = pygameMenu.Menu(surface,
                                    bgfun=main_background,
                                    color_selected=COLOR_WHITE,
                                    font=pygameMenu.font.FONT_COMIC_NEUE,
                                    font_color=COLOR_BLACK,
                                    font_size=30,
                                    font_size_title=40,
                                    menu_alpha=100,
                                    menu_color=MENU_BACKGROUND_COLOR,
                                    menu_height=int(WINDOW_SIZE[1]),
                                    menu_width=int(WINDOW_SIZE[0]),
                                    title='Note Training',
                                    widget_alignment=pygameMenu.locals.ALIGN_CENTER,
                                    window_height=WINDOW_SIZE[1],
                                    window_width=WINDOW_SIZE[0]
                                    )

    menu_cfg = {
        'color_selected': COLOR_WHITE,
        'font': pygameMenu.font.FONT_COMIC_NEUE,
        'font_color': COLOR_BLACK,
        'font_size': 30,
        'font_size_title': 40,
        'menu_alpha': 100,
        'menu_color': MENU_BACKGROUND_COLOR,
        'menu_height': int(WINDOW_SIZE[1]),
        'menu_width': int(WINDOW_SIZE[0]),
        'widget_alignment': pygameMenu.locals.ALIGN_CENTER,
        'window_height': WINDOW_SIZE[1],
        'window_width': WINDOW_SIZE[0]
    }

    scale_training = pygameMenu.Menu(surface,
                                     bgfun=main_background,
                                     title='Scale Training',
                                     **menu_cfg
                                     )

    photo_gallery = pygameMenu.Menu(surface,
                                    bgfun=main_background,
                                    title='Photo Gallery',
                                    **menu_cfg
                                    )

    # Main menu
    main_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                title="Recomaster",
                                **menu_cfg
                                )
    main_menu.set_fps(FPS, recursive=True)

    main_menu.add_option('Note Training', note_training)
    main_menu.add_option("Scale Training", scale_training)
    main_menu.add_option("Photo Gallery", photo_gallery)
    main_menu.add_option('Quit', pygameMenu.events.EXIT)

    # Main loop
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Main menu
        main_menu.mainloop()

        # Flip surface
        pygame.display.flip()

        # print("*")


if __name__ == '__main__':
    main()
