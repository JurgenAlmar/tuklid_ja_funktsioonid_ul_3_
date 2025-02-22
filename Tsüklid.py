import pygame
import sys

pygame.init()

ekraani_laius = 640
ekraani_korgus = 480
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
pygame.display.set_caption("Ruudustik")

punane = (255, 0, 0)
hele_roheline = (153, 255, 153)

def joonista_ruudustik(ruudu_suurus, joone_varv):
    read = ekraani_korgus // ruudu_suurus
    veerud = ekraani_laius // ruudu_suurus

    for rida in range(read):
        for veerg in range(veerud):
            x = veerg * ruudu_suurus
            y = rida * ruudu_suurus
            pygame.draw.rect(ekraan, joone_varv, (x, y, ruudu_suurus, ruudu_suurus), 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ekraan.fill(hele_roheline)

    joonista_ruudustik(20, punane)

    pygame.display.flip()

pygame.quit()
sys.exit()