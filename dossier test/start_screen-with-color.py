 def show_start_screen(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(BGCOLOR)
        done = False
        pg.display.flip()

        # MUSIQUE MENU
        # TODO voir si possibilité de fadeout le son.
        pg.mixer.init()
        sound = pg.mixer.music.load("music.mp3")
        pg.mixer.music.play(-1)  # repeat 5 times

# TODO L'affichage de l'image dans le menu modifie le spawn de la position des entités !!!!
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    done = True
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    print("ok")
                    pg.mixer.music.stop()
                    done = True