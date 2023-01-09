def distance_parcourue(marches, hauteur_marche):
  distance = (marches * hauteur_marche * 2) / 100 
  distance_par_semaine = distance * 5 * 7
  print(f"Pour {marches} marches de {hauteur_marche} cm, le gardien parcours {distance_par_semaine:.2f} m par semaine.")

distance_parcourue(10, 15)