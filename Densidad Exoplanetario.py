#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calcular_densidad(self):
    """
    Calcula la densidad del planeta exoplanetario en g/cm³.

    Returns:
        float: La densidad del planeta en g/cm³.
    """
    # Calcula la densidad dividiendo la masa del planeta entre su volumen
    volumen = (4/3) * np.pi * self._radio**3
    densidad = self._masa / volumen
    return densidad

