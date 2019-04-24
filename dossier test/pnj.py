hits = pg.sprite.spritecollide(self.player, self.pngs, False, collide_hit_rect)
dialogue = 0
police = pg.font.SysFont('arial', 72)

if hits:
    dialogue = 1
    print("collision ok")
elif hits == False:
    dialogue = 0

if dialogue == 1:
    Quete_texte = police.render('Houillon shallah tu meurt', True, (50, 50, 50))
    self.screen.blit(Quete_texte, (PNG_HIT_RECT.x + 50, PNG_HIT_RECT.y + 50))
    pg.display.flip()

else:
    pass