from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import BaseObject, BaseContainer, BaseTime, Vector, Matrix, BaseList2D
from c4d.modules.graphview import GvNode


class TP_MasterSystem(BaseList2D):
    def AllocParticle(self) -> int:
        """    
        Allocates a particle.
        
        :rtype: int
        :return: The particle ID of the allocated particle, or *NOTOK* if the allocation failed.
        
        
        """
        ...
    
    def AllocParticles(self, num: int) -> List[int]:
        """    
        Allocates *num* particles and stores their particles IDs.
        
        .. note::
        
        | The count of allocated particles might be unequal to *num* due to the limit in the settings *Max Particles*.
        | Change it to increase the count of allocatable particles.
        
        .. image:: /_imgs/modules/modules/thinkingparticles/tp_mastersystem_maxparticles.png
        
        :type num: int
        :param num: The number of particles to allocate.
        :rtype: List[int]
        :return: The list with the allocated particle IDs.
        
        
        """
        ...
    
    def FreeParticle(self, pid: int) -> None:
        """    
        Allocates *num* particles and stores their particles IDs.
        
        .. note::
        
        | Normally this should not be used.
        | Instead you should use :meth:`SetLife` with a negative time, so that the particle in question dies immediately.
        
        :type pid: int
        :param pid: Particle ID of the particle to free. Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        
        
        """
        ...
    
    def FreeAllParticles(self) -> None:
        """    
        Frees all particles.
        
        .. note::
        
        | Normally this should not be used.
        | Instead you should use :meth:`SetLife` with a negative time, so that the particle in question dies immediately.
        
        
        """
        ...
    
    def AllocParticleGroup(self) -> TP_PGroup:
        """    
        Allocates a new particle group.
        
        .. warning::
        
        Must be freed with :meth:`FreeParticleGroup`, or inserted into the list with :meth:`SetPGroupHierarchy`.
        
        :rtype: c4d.modules.thinkingparticles.TP_PGroup
        :return: The new particle group.
        
        
        """
        ...
    
    def FreeParticleGroup(self, group: TP_PGroup) -> None:
        """    
        Frees a particle group, removing it from the list.
        
        :type group: c4d.modules.thinkingparticles.TP_PGroup
        :param group: The group to free.
        
        
        """
        ...
    
    def SetPGroupHierarchy(self, parent: TP_PGroup, group: TP_PGroup, mode: int) -> None:
        """    
        Performs a hierarchy action on a particle group.
        
        :type parent: c4d.modules.thinkingparticles.TP_PGroup
        :param parent: Parent parameter.
        :type group: c4d.modules.thinkingparticles.TP_PGroup
        :param group: Group to act on.
        :type mode: int
        :param mode: Action:
        
        .. include:: /consts/TP_INSERT.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetRootGroup(self) -> TP_PGroup:
        """    
        Returns the root group.
        
        .. image:: /_imgs/modules/modules/thinkingparticles/tp_mastersystem_rootgroup.png
        
        :rtype: c4d.modules.thinkingparticles.TP_PGroup
        :return: The root group.
        
        
        """
        ...
    
    def GetParticleGroups(self, ingroup: TP_PGroup, mode: int, subgroups: bool) -> None:
        """    
        Returns the particle groups in *ingroup*, specified by *mode*.
        
        :type ingroup: c4d.modules.thinkingparticles.TP_PGroup
        :param ingroup: In-group parameter.
        :type mode: int
        :param mode: Mode:
        
        .. include:: /consts/TP_GETPGROUP.rst
        :start-line: 3
        
        :type subgroups: bool
        :param subgroups: If this is **True** sub groups are included.
        :rtype: list of :class:`TP_PGroup <c4d.modules.thinkingparticles.TP_PGroup>`
        :return: The root group.
        
        
        """
        ...
    
    def GetGroupParticleCount(self, ingroup: TP_PGroup, subgroups: bool) -> int:
        """    
        Calculates the number of particles in the ingroup *group*.
        
        :type ingroup: c4d.modules.thinkingparticles.TP_PGroup
        :param ingroup: In-group parameter.
        :type subgroups: bool
        :param subgroups: If this is **True** sub groups are included.
        :rtype: int
        :return: The number of particles.
        
        
        """
        ...
    
    def GetParticles(self, all: bool) -> List[int]:
        """    
        Retrieve a list of all particles Id.
        
        :param all: If **True** all particles added, otherwise only alive particle.
        :type all: bool
        :return: list(int)
        :rtype: A list with all particles ID.
        
        
        """
        ...
    
    def GetVirtualObjects(self, ingroup: TP_PGroup, inRender: bool, subgroups: bool, hh: Any) -> BaseObject:
        """    
        Creates the virtual object hierarchy for a particle group, i.e. an object group containing all particles. Used by the ParticleGeometry object.
        
        :type ingroup: c4d.modules.thinkingparticles.TP_PGroup
        :param ingroup: In-group parameter.
        :type inRender: bool
        :param inRender: **True** if this is for rendering, otherwise the objects are built for the editor view.
        :type subgroups: bool
        :param subgroups: If this is **True** sub groups are included.
        :type hh: HierarchyHelp - Not implemented
        :param hh:
        
        | A hierarchy helper for the operation.
        | Usually passed through from a calling function, for example from :meth:`ObjectData.GetVirtualObjects` or a Python generator `main()`.
        
        :rtype: c4d.BaseObject
        :return: Virtual object or **None** if there was an error.
        
        
        """
        ...
    
    def GetGroupInfo(self, group: TP_PGroup) -> BaseContainer:
        """    
        Retrieves the group information for a *group*.
        
        :type group: c4d.modules.thinkingparticles.TP_PGroup
        :param group: Group to get the information for.
        :rtype: c4d.BaseContainer
        :return: The group information for the group.
        
        
        """
        ...
    
    def GetGroupFromInfo(self, info: BaseContainer) -> TP_PGroup:
        """    
        Retrieves a group from the information in *info*.
        
        :type info: c4d.BaseContainer
        :param info: The information to search for.
        :rtype: c4d.modules.thinkingparticles.TP_PGroup
        :return: The retrieved group or **None** if no group matched.
        
        
        """
        ...
    
    def UpdateGroup(self, group: TP_PGroup, timeDelta: BaseTime) -> bool:
        """    
        Updates a *group* at a given time difference since the last update.
        
        .. note::
        
        Use a default *timeDelta* of `0` to update at the current time.
        
        .. versionadded:: R16.050
        
        :type group: c4d.modules.thinkingparticles.TP_PGroup
        :param group: The group to update.
        :type timeDelta: c4d.BaseTime
        :param timeDelta: The time difference since the last update.
        :rtype: bool
        :return: **True** if the update was done successfully, otherwise **False**.
        
        
        """
        ...
    
    def NumParticles(self) -> int:
        """    
        | Retrieves the number of allocated particles.
        | All particles IDs are less than this value.
        
        :rtype: int
        :return: Number of particles.
        
        
        """
        ...
    
    def Alive(self, pid: int) -> bool:
        """    
        Retrieves the alive bit of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: bool
        :return: **True** if the particle is alive, otherwise **False**.
        
        
        """
        ...
    
    def IsBorn(self, pid: int) -> bool:
        """    
        Retrieves the is-born bit of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: bool
        :return: **True** if the particle was just born, otherwise **False**.
        
        
        """
        ...
    
    def IsDie(self, pid: int) -> bool:
        """    
        Retrieves the is-die bit of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: bool
        :return: **True** if the particle just died, otherwise **False**.
        
        
        """
        ...
    
    def EntersGroup(self, pid: int) -> bool:
        """    
        Retrieves the enters-group bit of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: bool
        :return: **True** if the particle just entered a group, otherwise **False**.
        
        
        """
        ...
    
    def Group(self, pid: int) -> bool:
        """    
        Retrieves the group of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: bool
        :return: The group that the particle currently is in, otherwise **None**.
        
        
        """
        ...
    
    def Position(self, pid: int) -> Vector:
        """    
        Retrieves the position of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: c4d.Vector
        :return: Particle position.
        
        
        """
        ...
    
    def Velocity(self, pid: int) -> Vector:
        """    
        Retrieves the velocity of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: c4d.Vector
        :return: Particle velocity.
        
        
        """
        ...
    
    def Mass(self, pid: int) -> float:
        """    
        Retrieves the mass of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: float
        :return: Particle mass.
        
        
        """
        ...
    
    def Spin(self, pid: int) -> float:
        """    
        Retrieves the spin of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: float
        :return: Particle spin.
        
        
        """
        ...
    
    def Size(self, pid: int) -> float:
        """    
        Retrieves the size of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: float
        :return: Particle size.
        
        
        """
        ...
    
    def Scale(self, pid: int) -> Vector:
        """    
        Retrieves the scale of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: c4d.Vector
        :return: Particle scale.
        
        
        """
        ...
    
    def Age(self, pid: int) -> BaseTime:
        """    
        Retrieves the age of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: c4d.BaseTime
        :return: Particle age.
        
        
        """
        ...
    
    def Life(self, pid: int) -> BaseTime:
        """    
        Retrieves the lifetime of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: c4d.BaseTime
        :return: Particle lifetime.
        
        
        """
        ...
    
    def Alignment(self, pid: int) -> Matrix:
        """    
        Retrieves the alignment matrix of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: c4d.Matrix
        :return: Particle alignment matrix.
        
        
        """
        ...
    
    def Randomseed(self, pid: int) -> Matrix:
        """    
        Retrieves the random seed of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: c4d.Matrix
        :return: Particle random seed.
        
        
        """
        ...
    
    def Transform(self, pid: int) -> Matrix:
        """    
        Retrieves the transformation matrix of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: c4d.Matrix
        :return: Particle transformation matrix.
        
        
        """
        ...
    
    def Flags(self, pid: int) -> Matrix:
        """    
        Retrieves the transformation matrix of a particle.
        
        .. note:: These are private. Use the functions like :meth:`Alive` instead.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: c4d.Matrix
        :return: Particle flags.
        
        
        """
        ...
    
    def DTFactor(self, pid: int) -> float:
        """    
        Retrieves the delta time factor of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: float
        :return: Particle flags.
        
        
        """
        ...
    
    def Color(self, pid: int) -> Vector:
        """    
        Retrieves the color of a particle.
        
        .. versionadded:: R16.038
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :rtype: c4d.Vector
        :return: Particle color.
        
        
        """
        ...
    
    def SetPosition(self, pid: int, p: Vector) -> None:
        """    
        Retrieves the delta time factor of a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type p: c4d.Vector
        :param p: New particle position.
        
        
        """
        ...
    
    def SetVelocity(self, pid: int, p: Vector) -> None:
        """    
        Sets the velocity for a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type p: c4d.Vector
        :param p: New particle velocity.
        
        
        """
        ...
    
    def SetMass(self, pid: int, mass: float) -> None:
        """    
        Sets the mass for a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type mass: float
        :param mass: New particle velocity.
        
        
        """
        ...
    
    def SetSpin(self, pid: int, axis: Vector, speed: float) -> None:
        """    
        Sets the spin for a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type axis: c4d.Vector
        :param axis: Rotation axis.
        :type speed: float
        :param speed: Rotation speed
        
        
        """
        ...
    
    def SetAge(self, pid: int, age: BaseTime) -> None:
        """    
        Sets the age for a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type age: c4d.BaseTime
        :param age: New particle age.
        
        
        """
        ...
    
    def SetLife(self, pid: int, life: BaseTime) -> None:
        """    
        Sets the age for a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type life: c4d.BaseTime
        :param life: New particle lifetime.
        
        
        """
        ...
    
    def SetGroup(self, pid: int, group: TP_PGroup) -> None:
        """    
        Inserts a particle into another group.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type group: c4d.modules.thinkingparticles.TP_PGroup
        :param group: The group to place the particle in.
        
        
        """
        ...
    
    def SetSize(self, pid: int, size: float) -> None:
        """    
        Sets the size for a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type size: float
        :param size: New particle size.
        
        
        """
        ...
    
    def SetScale(self, pid: int, scale: Vector) -> None:
        """    
        Sets the size for a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type scale: c4d.Vector
        :param scale: New particle scale.
        
        
        """
        ...
    
    def SetAlignment(self, pid: int, align: Matrix) -> None:
        """    
        Sets the alignment matrix for a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type align: c4d.Matrix
        :param align: New particle alignment matrix.
        
        
        """
        ...
    
    def SetRandomseed(self, pid: int, seed: int) -> None:
        """    
        Sets the alignment matrix for a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type seed: int
        :param seed: New particle random seed.
        
        
        """
        ...
    
    def SetCollision(self, pid: int, collision: int) -> None:
        """    
        Sets the collision handling information for a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type collision: int
        :param collision: Collision ID. This is :meth:`GetOperatorID` for the node responsible for the collision handling.
        
        
        """
        ...
    
    def SetDTFactor(self, pid: int, dt: float) -> None:
        """    
        Sets the delta time factor for a particle.
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type dt: float
        :param dt: New particle delta time factor.
        
        
        """
        ...
    
    def SetColor(self, pid: int, color: Vector) -> None:
        """    
        Sets the color for a particle.
        
        .. versionadded:: R16.038
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type color: c4d.Vector
        :param color: New particle color.
        
        
        """
        ...
    
    def SetPData(self, pid: int, chan: int, value: Union[int, float, str, Vector, BaseTime, Matrix, BaseList2D]) -> bool:
        """    
        Sets the data channel value for a particle:
        
        .. code-block:: python
        
        pid = 1
        chan = 0
        ms.SetPData(pid, chan, "Hello World!")
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type chan: int
        :param chan: Channel index.
        :raise IndexError: If *chan* is out of range : *0<=chan<*:meth:`NumDataChannels`.
        :type value: Union[int, float, str, c4d.Vector, c4d.BaseTime, c4d.Matrix, c4d.BaseList2D]
        :param value: The new value to set.
        :rtype: bool
        :return: **True** on success, otherwise **False**.
        
        
        """
        ...
    
    def GetPData(self, pid: int, chan: int) -> Any:
        """    
        Sets the data channel value for a particle:
        
        .. code-block:: python
        
        pid = 1
        chan = 0
        value = ms.GetPData(pid, chan, "Hello World!")
        
        :type pid: int
        :param pid: Particle ID.
        :raise IndexError: If *pid* is out of range : *0<=pid<*:meth:`NumParticles`.
        :type chan: int
        :param chan: Channel index.
        :raise IndexError: If *chan* is out of range : *0<=chan<*:meth:`NumDataChannels`.
        :rtype: Any
        :return: Depends on the type of the channel.
        
        
        """
        ...
    
    def AddDataChannel(self, type: int, str: str) -> bool:
        """    
        Adds a new data channel.
        
        :type type: int
        :param type: Channel data type.
        :type str: str
        :param str: Channel
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def RemoveDataChannel(self, chan: int) -> bool:
        """    
        Removes a data channel.
        
        :type chan: int
        :param chan: Channel index.
        :raise IndexError: If *chan* is out of range : *0<=chan<*:meth:`NumDataChannels`.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def NumDataChannels(self) -> int:
        """    
        Retrieves the data channel count.
        
        :rtype: int
        :return: Number of data.
        
        
        """
        ...
    
    def DataChannelType(self, chan: int) -> int:
        """    
        Retrieves the data type of a data channel.
        
        :type chan: int
        :param chan: Channel index.
        :raise IndexError: If *chan* is out of range : *0<=chan<*:meth:`NumDataChannels`.
        :rtype: int
        :return: Data type of channel *chan*.
        
        
        """
        ...
    
    def DataChannelName(self, chan: int) -> str:
        """    
        Retrieves the name of a data channel.
        
        :type chan: int
        :param chan: Channel index.
        :raise IndexError: If *chan* is out of range : *0<=chan<*:meth:`NumDataChannels`.
        :rtype: str
        :return: Number of data.
        
        
        """
        ...
    
    def DataChannelUniqueID(self, chan: int) -> int:
        """    
        Retrieves a unique ID for a data channel that's independent of its index.
        
        :type chan: int
        :param chan: Channel index.
        :raise IndexError: If *chan* is out of range : *0<=chan<*:meth:`NumDataChannels`.
        :rtype: int
        :return: Unique ID of channel *chan*.
        
        
        """
        ...
    
    def DataChannelID(self, unique_id: int) -> int:
        """    
        Retrieves the index of a data channel from its unique ID.
        
        :type unique_id: int
        :param unique_id: Channel ID.
        :rtype: int
        :return: Data channel index.
        
        
        """
        ...
    
    def GetOperatorID(self, op: GvNode) -> int:
        """    
        Retrieves an ID for *op*
        
        :type op: c4d.modules.graphview.GvNode
        :param op: A node.
        :rtype: int
        :return: ID for *op*.
        
        
        """
        ...
    
    def GetDirty(self) -> int:
        """    
        | A dirty counter for the master system.
        | This can be used to see if anything has changed. Use :meth:`SetDirty` to increment the counter.
        
        :rtype: long
        :return: Dirty counter. Is incremented when something changes in the system.
        
        
        """
        ...
    
    def SetDirty(self) -> None:
        """    
        Increments the dirty counter, i.e. tells anyone using :meth:`GetDirty` that something has changed.
        
        .. note::
        
        This has to be used whenever an operator affects particle shapes, like the ObjectShape operator does.
        
        
        """
        ...
    
    def CheckCollision(self, collision: int, pid: int, t: float, pos: Vector, vel: Vector, dt: float) -> None:
        """    
        Finds the node responsible for collision, the one that called SetCollision(),
        and tells it to evaluate the passed collision parameters.
        
        .. note::
        
        Normally Thinking Particles evaluates this function automatically for registered collisions.
        
        :param collision: The collision ID. This is GetOperatorID() for the node responsible for the collision.
        :type collision: int
        :param pid: The particle ID: 0 <= pid < NumParticles()
        :type pid: int
        :param t:
        
        | Time to evaluate the collision at.
        | Collisions are detected between t - dt and t.
        
        :type t:  float
        :param pos: Assigned the new position of the object if there is a collision.
        :type pos: c4d.Vector
        :param vel: Assigned the new velocity of the object if there is a collision.
        :type vel: c4d.Vector
        :param dt: 	The time since the last evaluation, i.e. the time to look backwards for collisions.
        :type dt: float
        :rtype: tuple(bool, dict("axis": c4d.Vector, "speed": float), float)
        :return: A tuple filled in this order:
        
        - **True** if there was a collision, otherwise **False**.
        - dict with the next entries:
        
        - "axis": Rotation axis.
        - "speed": Rotation speed.
        - The collision time, if there was a collision. This is generally less than t.
        
        
        """
        ...
    

class TP_PGroup(BaseList2D):
    def GetLevel(self) -> int:
        """    
        Calculates the level of this group. This is the number of parents that the group has.
        
        :rtype: int
        :return: The group level.
        
        
        """
        ...
    
    def NumParticles(self) -> int:
        """    
        Returns the count of particles which belong to this group.
        
        :rtype: int
        :return: The number of particles.
        
        
        """
        ...
    
    def IsSubGroup(self, group: TP_PGroup) -> bool:
        """    
        Checks if *group* is a subgroup of the group.
        
        :type group: c4d.modules.thinkingparticles.TP_PGroup
        :param group: A TP particle group.
        :rtype: bool
        :return: **True** if *group* is a subgroup of the group, otherwise **False**.
        
        
        """
        ...
    
    def GetGroupID(self) -> int:
        """    
        Returns the ID of the group. This is only based on the order in the group list, so it can change when the user reorders the groups.
        
        :rtype: int
        :return: The group ID.
        
        
        """
        ...
    
    def GetParticles(self) -> List[int]:
        """    
        Returns the particles which belong to this group.
        
        :rtype: List[int]
        :return: The particles.
        
        
        """
        ...
    
    def SetTitle(self, title: str) -> None:
        """    
        Sets the group title.
        
        :type title: str
        :param title: The new group title.
        
        
        """
        ...
    
    def GetTitle(self) -> str:
        """    
        Returns the group title.
        
        :rtype: str
        :return: The group title.
        
        
        """
        ...
    
    def SetViewType(self, type: Any) -> None:
        """    
        Sets the group view type.
        
        :type title: int
        :param title: The new view type. See *PGROUP_VIEWTYPE* in `description/tp_group.h`
        
        
        """
        ...
    
    def GetViewType(self) -> int:
        """    
        Returns the group view type.
        
        :rtype: int
        :return: The group view type.
        
        
        """
        ...
    
    def SetShowObjects(self, bool: Any) -> None:
        """    
        Sets the show-objects flag of the group.
        
        :type show: bool
        :param show: The new show-objects flag.
        
        
        """
        ...
    
    def GetShowObjects(self) -> int:
        """    
        Returns the show-objects flag of the group.
        
        :rtype: int
        :return: The show-objects flag.
        
        
        """
        ...
    
    def SetColor(self, col: Vector) -> None:
        """    
        Sets the color of the group.
        
        :type col: c4d.Vector
        :param col: The new group color.
        
        
        """
        ...
    
    def GetColor(self) -> Vector:
        """    
        Returns the color of the group.
        
        :rtype: c4d.Vector
        :return: The group color.
        
        
        """
        ...
    
    def EditSettings(self) -> bool:
        """    
        Opens the edit dialog for the group.
        
        :rtype: bool
        :return: **True** if the user clicked `OK`, otherwise **False**.
        
        
        """
        ...
    
    def IsSelected(self) -> bool:
        """    
        Checks if the group is selected in the group list.
        
        :rtype: bool
        :return: **True** if the group is selected, otherwise **False**.
        
        
        """
        ...
    
    def IsOpened(self) -> bool:
        """    
        Checks if the group is opened in the group list.
        
        :rtype: bool
        :return: **True** if the group is opened, otherwise **False** if it is closed.
        
        
        """
        ...
    
    def Select(self, mode: int) -> None:
        """    
        Sets the selection mode of the group in the group list.
        
        :type mode: int
        :param mode: The selection mode:
        
        .. include:: /consts/SELECTION.rst
        :start-line: 3
        
        
        """
        ...
    
    def Open(self, onoff: bool) -> None:
        """    
        Opens or closes the group in the group list.
        
        :type onoff: bool
        :param onoff: **True** if the group should be opened, otherwise **False** if it should be closed.
        
        
        """
        ...
    
    def SetUseColor(self, use: bool) -> None:
        """    
        Sets the use color state of the group.
        
        .. versionadded:: R16.038
        
        :type use: bool
        :param use: **True** if use color should be enabled, otherwise **False**.
        
        
        """
        ...
    
    def GetUseColor(self) -> bool:
        """    
        Gets the use color state of the group.
        
        .. versionadded:: R16.038
        
        :rtype: bool
        :return: **True** if use color is enabled, otherwise **False**.
        
        
        """
        ...
    
    def Cache(self, onoff: bool) -> None:
        """    
        Sets the group to contain only cached data. This will prevent the particle system from doing simulation calculations for the group.
        
        .. versionadded:: R16.050
        
        :type onoff: bool
        :param onoff: **True** if cached data is used, otherwise **False**.
        
        
        """
        ...
    
    def IsCache(self) -> bool:
        """    
        Checks if the group is used to represent cached particle data only.
        
        .. versionadded:: R16.050
        
        :rtype: bool
        :return: **True** if the group represents cached data, otherwise **False**.
        
        
        """
        ...
    

