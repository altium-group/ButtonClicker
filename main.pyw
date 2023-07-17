import pygame

# Initialisation de Pygame
pygame.init()

fenetre = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Cookie Clicker")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Position et taille des boutons
bouton_clic_x = 350
bouton_clic_y = 250
bouton_clic_largeur = 100
bouton_clic_hauteur = 100

bouton_boost_x = 350
bouton_boost_y = 400
bouton_boost_largeur = 100
bouton_boost_hauteur = 50

# Compteur de clics et d'argent
clics = 0
argent = 0
boost_actif = False

# Valeurs d'argent et de boost
boost = 1
boost_prix = 10

# Chargement des images des boutons
bouton_clic_image = pygame.image.load("button.png")
bouton_boost_image = pygame.image.load("button2.png")

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Gestion du clic de souris
            if bouton_clic_x < event.pos[0] < bouton_clic_x + bouton_clic_largeur and bouton_clic_y < event.pos[1] < bouton_clic_y + bouton_clic_hauteur:
                clics += 1
                argent += boost

            elif bouton_boost_x < event.pos[0] < bouton_boost_x + bouton_boost_largeur and bouton_boost_y < event.pos[1] < bouton_boost_y + bouton_boost_hauteur:
                if argent >= boost_prix:
                    argent -= boost_prix
                    boost += 1
                    boost_prix += boost * 1.2
                    boost_actif = True

    # Affichage des éléments du jeu
    fenetre.fill(BLANC)
    fenetre.blit(bouton_clic_image, (bouton_clic_x, bouton_clic_y))
    fenetre.blit(bouton_boost_image, (bouton_boost_x, bouton_boost_y))
    
    # Affichage du compteur de clics et d'argent
    police = pygame.font.Font(None, 36)
    texte_clics = police.render(f"Clics: {clics:,}", True, NOIR)
    texte_argent = police.render(f"Argent: {round(argent, 2):,}$", True, NOIR)
    texte_prix = police.render(f"Prochain boost : {round(boost_prix, 2):,}$", True, NOIR)
    fenetre.blit(texte_clics, (10, 50))
    fenetre.blit(texte_argent, (10, 75))
    fenetre.blit(texte_prix, (10, 100))

    if boost_actif:
        texte_boost_actif = police.render(f"Boost (x{round(boost, 2):,})", True, NOIR)
        fenetre.blit(texte_boost_actif, (10, 125))

    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
