#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def densidad(self):
    """
    Calcula la densidad de la estrella.

    Returns:
    - La densidad de la estrella.
    """
    return float(self._masa / ((4/3) * np.pi * (self._radioestrella**3)))

