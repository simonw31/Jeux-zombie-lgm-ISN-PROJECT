def show_start_screen(self):
    game_folder = path.dirname(__file__)
    img_folder = path.join(game_folder, 'img')
    BG_IMG = 'bg_main_menu.jpg'
    image = pg.image.load(path.join(img_folder, BG_IMG)).convert_alpha()
    ecran = pg.display.set_mode((1024, 768))
    done = False
    ecran.blit(image, (0, 0))
    pg.display.flip()

    # MUSIQUE MENU
    # TODO voir si possibilité de fadeout le son.
    pg.mixer.init()
    sound = pg.mixer.music.load("music.mp3")
    pg.mixer.music.play(-1)  # repeat 5 times

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                done = True
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                print("ok")
                pg.mixer.music.stop()
                pg.display.flip()
                g.new()
                g.run()
