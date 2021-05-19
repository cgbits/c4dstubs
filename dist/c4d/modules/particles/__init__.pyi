from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import Matrix


class BaseParticle(object):
    ...

class Particle(object):
    ...


def CalcParticleMatrix(cp: Particle) -> Matrix:
    """    
    Calculate the particles matrix, this represents the position and direction of the particle as used when the objects are aligned with a particle using the emitter Tangential option.
    
    :type cp: c4d.modules.particles.Particle
    :param cp: The particle you wish to get the matrix for.
    :rtype: c4d.Matrix
    :return: Details of the particles position and rotation.
    
    
    """
    ...

