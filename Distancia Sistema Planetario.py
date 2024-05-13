#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def distancia_media(self):
    """
    Calcula la distancia media de los planetas alrededor de la estrella en unidades astronómicas (UA).
    
    Retorna:
    - La distancia media de los planetas alrededor de la estrella en UA (float).
    """
    if len(self.planetas) == 0:
        return 0
    
    distancia_total = sum([planeta.distancia_estrella for planeta in self.planetas if planeta.distancia_estrella is not None])
    distancia_media = distancia_total / len(self.planetas)
    
    return distancia_media

