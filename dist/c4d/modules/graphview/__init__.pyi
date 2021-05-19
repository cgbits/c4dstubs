from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import BaseList2D, BaseContainer, DescID, BaseTag
from c4d.threading import BaseThread
from c4d.bitmaps import BaseBitmap


class XPressoTag(BaseTag):
    def __init__(self) -> None:
        """    
        :rtype: c4d.modules.graphview.XPressoTag
        :return: The new XPresso tag.
        
        
        """
        ...
    
    def GetNodeMaster(self) -> GvNodeMaster:
        """    
        Returns the nodemaster of this XPressoTag.
        
        :rtype: c4d.modules.graphview.GvNodeMaster
        :return: The nodemaster.
        
        
        """
        ...
    

class GvPort(object):
    def Connect(self, port: GvPort) -> bool:
        """    
        Connects a port with another.
        
        .. note::
        
        Remember, the nodes of the ports have to be in the same :class:`GvNodeMaster <c4d.modules.graphview.GvNodeMaster>`, otherwise the connection fails.
        
        :type port: c4d.modules.graphview.GvPort
        :param port:  The port to connect to.
        :rtype: bool
        :return: **True** on succeeded connection, otherwise **False**.
        
        
        """
        ...
    
    def Remove(self) -> bool:
        """    
        Removes the connections of this port.
        
        :rtype: bool
        :return: **True** if the connection was removed, otherwise **False**.
        
        
        """
        ...
    
    def GetNrOfConnections(self) -> int:
        """    
        Get the number of connections, including both the incoming connection and outgoing connections.
        
        :rtype: int
        :return: Number of connections.
        
        
        """
        ...
    
    def IsIncomingConnected(self) -> bool:
        """    
        Check if there's an incoming connection.
        
        :rtype: bool
        :return: **True** if there's an incoming connection to the port, otherwise **False**.
        
        
        """
        ...
    
    def GetDestination(self) -> None:
        """    
        Returns the port where the port is linked with.
        
        :rtype: list of type :class:`GvPort <c4d.modules.graphview.GvPort>`
        :param: A list with all destinations.
        
        
        """
        ...
    
    def GetNode(self) -> GvNode:
        """    
        Returns the node of this port.
        
        :rtype: c4d.modules.graphview.GvNode
        :param: The container
        
        
        """
        ...
    
    def GetName(self, node: GvNode) -> str:
        """    
        Gets the name of this port.
        
        :type node: c4d.modules.graphview.GvNode
        :param node: The node the port belongs to
        :rtype: str
        :return: Port name.
        
        
        """
        ...
    
    def SetName(self, name: str) -> None:
        """    
        Sets the name of this port.
        
        :type name: str
        :param name: Port name.
        
        
        """
        ...
    
    def GetIO(self) -> int:
        """    
        Gets the IO mode for this port.
        
        :rtype: int
        :return: IO mode:
        
        .. include:: /consts/GV_PORT.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetMainID(self) -> int:
        """    
        Gets the main ID of the port.
        
        :rtype: int
        :return: Main ID.
        
        
        """
        ...
    
    def SetMainID(self, id: int) -> None:
        """    
        Sets the main ID of the port.
        
        :type id: int
        :param id: New main ID.
        
        
        """
        ...
    
    def GetSubID(self) -> int:
        """    
        Gets the sub ID of the port.
        
        :rtype: int
        :return: Sub ID.
        
        
        """
        ...
    
    def SetUserID(self, id: int) -> None:
        """    
        Sets the user ID of the port.
        
        :param id: The user ID to set.
        :type id: int
        
        
        """
        ...
    
    def GetUserID(self) -> int:
        """    
        Gets the user ID of the port.
        
        :rtype: int
        :return: Sub ID.
        
        
        """
        ...
    
    def GetValueType(self) -> int:
        """    
        Gets the value type of the port.
        
        :rtype: int
        :return: The value type.
        
        
        """
        ...
    
    def SetVisible(self, v: bool) -> None:
        """    
        Set the visibility of the port.
        
        :type v: bool
        :param v: **False** for an invisible port.
        
        
        """
        ...
    
    def GetVisible(self) -> bool:
        """    
        Checks if this port is hidden or visible.
        
        :rtype: bool
        :return: **True** if visible, otherwise **False**.
        
        
        """
        ...
    
    def GetUserData(self) -> None:
        """    
        Internal.
        
        .. versionadded:: R17.048
        
        
        """
        ...
    
    def SetUserData(self) -> None:
        """    
        Internal.
        
        .. versionadded:: R17.048
        
        
        """
        ...
    

class GvNodeMaster(BaseList2D):
    def __init__(self, host: BaseList2D) -> None:
        """    
        .. note:
        
        Normally not used, use :meth:`XPressoTag.__init__` instead.
        
        :type host: BaseList2D
        :param host: Attaches a :class:`GvNodeMaster <c4d.modules.graphview.GvNodeMaster>` to a BaseList2D object.
        :rtype: c4d.modules.graphview.GvNodeMaster
        :return: The new nodemaster.
        
        
        """
        ...
    
    def AllocNode(self, id: int) -> GvNode:
        """    
        Allocates a node without inserting it.
        
        :type id: int
        :param id: The id. See :doc:`/types/gvnodes`.
        :rtype: c4d.modules.graphview.GvNode
        :return: The new node.
        
        
        """
        ...
    
    def CreateNode(self, parent: GvNode, id: int, insert: Optional[GvNode] = ..., x: Optional[int] = ..., y: Optional[int] = ...) -> GvNode:
        """    
        Creates a node and inserts it.
        
        :type parent: c4d.modules.graphview.GvNode
        :param parent: Parent node, can be :meth:`GetRoot`.
        :type id: int
        :param id: The id. See :doc:`/types/gvnodes`.
        :type insert: c4d.modules.graphview.GvNode
        :param insert: The insertion point.
        :type x: int
        :param x: X position
        :type y: int
        :param y: Y position.
        :rtype: c4d.modules.graphview.GvNode
        :return: The created node.
        
        
        """
        ...
    
    def GetRoot(self) -> GvNode:
        """    
        Retrieves the root node.
        
        :rtype: c4d.modules.graphview.GvNode
        :return: The root node or **None**.
        
        
        """
        ...
    
    def GetOwner(self) -> BaseList2D:
        """    
        Retrieves the owner.
        
        :rtype: c4d.BaseList2D
        :return: The owner of the :class:`GvNodeMaster <c4d.modules.graphview.GvNodeMaster>`
        
        
        """
        ...
    
    def InsertFirst(self, parent: GvNode, node: GvNode) -> bool:
        """    
        Inserts a node first in the node list of an Xgroup.
        
        .. note::
        
        Equivalent to :meth:`GeListNode.InsertUnder`, but with additional checks that parent is a group node, and that node is removed.
        
        :type parent: c4d.modules.graphview.GvNode
        :param parent: Parent node. Must be in the same node master.
        :type node: c4d.modules.graphview.GvNode
        :param node: Node to insert.
        :rtype: bool
        :return: **True** if the node was inserted, otherwise **False**.
        
        
        """
        ...
    
    def InsertLast(self, parent: GvNode, node: GvNode) -> bool:
        """    
        Inserts a node last in the node list of an Xgroup.
        
        .. note::
        
        Equivalent to :meth:`GeListNode.InsertUnderLast`, but with additional checks that parent is a group node, and that node is removed.
        
        :type parent: c4d.modules.graphview.GvNode
        :param parent: Parent node. Must be in the same node master.
        :type node: c4d.modules.graphview.GvNode
        :param node: Node to insert.
        :rtype: bool
        :return: **True** if the node was inserted, otherwise **False**.
        
        
        """
        ...
    
    def SetHierarchy(self, insert: GvNode, node: GvNode, mode: int) -> bool:
        """    
        Perform a hierarchy operation. Pass the arguments as a dictionary.
        
        :type insert: c4d.modules.graphview.GvNode
        :param insert: Insertion point.
        :type node: c4d.modules.graphview.GvNode
        :param node: The node to perform the operation on.
        :type mode: int
        :param mode: The insertion mode:
        
        .. include:: /consts/GV_INSERT.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the hierarchy was set, otherwise **False**.
        
        
        """
        ...
    
    def IsEnabled(self) -> GvNodeMaster:
        """    
        Checks if the node master is enabled.
        
        :rtype: c4d.modules.graphview.GvNodeMaster
        :return:  **True** if the node master is enabled.
        
        
        """
        ...
    
    def GetPrefs(self) -> BaseContainer:
        """    
        Returns the settings container.
        
        :rtype: c4d.BaseContainer
        :return: A copy of the settings container.
        
        
        """
        ...
    
    def SetPrefs(self, bc: BaseContainer) -> None:
        """    
        Set the settings container.
        
        :type bc: c4d.BaseContainer
        :param bc: The settings container.
        
        
        """
        ...
    
    def AddUndo(self) -> bool:
        """    
        Call this function if you manipulated something with a node master, and you want it to be undoable.
        
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def Execute(self, thread: BaseThread) -> int:
        """    
        Calculates the :class:`GvNodeMaster <c4d.modules.graphview.GvNodeMaster>`.
        
        .. versionchanged:: S22
        
        :param thread:
        :type thread: c4d.threading.BaseThread
        :return:
        
        .. include:: /consts/GV_ERR.rst
        :start-line: 3
        
        :rtype: int
        
        
        """
        ...
    

class GvNode(BaseList2D):
    def Redraw(self) -> None:
        """    
        Redraws the node.
        
        
        """
        ...
    
    def GetOperatorID(self) -> int:
        """    
        Returns the operator ID.
        
        :rtype: int
        :return: The id.
        
        
        """
        ...
    
    def GetOwnerID(self) -> int:
        """    
        Returns the owner ID of the node.
        
        :rtype: int
        :return: The id.
        
        .. include:: /consts/ID_GV.rst
        :start-line: 3
        
        
        """
        ...
    
    def GetNodeMaster(self) -> GvNodeMaster:
        """    
        Returns the GvNodeMaster where the node is attached to.
        
        :rtype: c4d.modules.graphview.GvNodeMaster
        :param mask: The GvNodeMaster or **None** if there is no nodemaster.
        
        
        """
        ...
    
    def IsGroupNode(self) -> bool:
        """    
        Checks if the node is a group node.
        
        :rtype: bool
        :param mask: **True** if the node is a group node, otherwise **False**.
        
        
        """
        ...
    
    def SetPortType(self, port: GvPort, id: int) -> None:
        """    
        Changes the type of a port of this node.
        
        :type port: c4d.modules.graphview.GvPort
        :param port: A port of this node.
        :type id: int
        :param id: The new port ID.
        
        
        """
        ...
    
    def ResetPortType(self, id: int) -> None:
        """    
        Changes the type of the port. Used to manage dynamic data ports.
        
        :type id: int
        :param id: The type.
        
        
        """
        ...
    
    def RemoveUnusedPorts(self, message: bool) -> None:
        """    
        Removes all unused ports - Sends a message to the node.
        
        :type message: bool
        :param message: If this is **True**, the operator receives a message when the ports are removed.
        
        
        """
        ...
    
    def RemoveConnections(self) -> None:
        """    
        Removes all connections of the node.
        
        
        """
        ...
    
    def RemovePort(self, port: GvPort, message: bool) -> None:
        """    
        Removes a port from this node.
        
        :type port: c4d.modules.graphview.GvPort
        :param port: A port of this node to remove.
        :type message: bool
        :param message: If this is **True** the operator receives a message when the port is removed.
        
        
        """
        ...
    
    def RemovePortIsOK(self, port: GvPort) -> bool:
        """    
        Checks if it is OK to remove a port from this node.
        
        .. note::
        
        Used to check if a call to :meth:`GvNode.RemovePort` would succeed.
        
        :type port: c4d.modules.graphview.GvPort
        :param port: A port of this node to remove.
        :rtype: bool
        :return: **True** if this port can be remove.
        
        
        """
        ...
    
    def GetPort(self, sub_id: int) -> GvPort:
        """    
        Retrieves a port by sub ID.
        
        :type sub_id: int
        :param sub_id: Port sub ID.
        :rtype: c4d.modules.graphview.GvPort
        :return: The retrieved port, or **None**.
        
        
        """
        ...
    
    def GetPortIndex(self, id: int) -> int:
        """    
        Gets the index of a port by sub ID.
        
        :type id: int
        :param id: Port sub ID.
        :rtype: int
        :return: Port index.
        
        
        """
        ...
    
    def GetOutPorts(self, type: int) -> None:
        """    
        Retrieves all outports of a node.
        
        :type type: int
        :param type:
        
        | If *type* is set, just the ports with the given type will be returned.
        | Each port has its own type ID's for the ports so check the C-header files of the node.
        
        :rtype: list of :class:`GvPort <c4d.modules.graphview.GvPort>`
        :return: The GvPorts or **None** if no port was found.
        
        
        """
        ...
    
    def GetInPorts(self, type: int) -> None:
        """    
        Retrieves all inports of a node.
        
        :type type: int
        :param type:
        
        | If *type* is set, just the ports with the given type will be returned.
        | Each port has its own type ID's for the ports so check the C-header files of the node.
        
        :rtype: list of :class:`GvPort <c4d.modules.graphview.GvPort>`
        :return: The GvPorts or **None** if no port was found.
        
        
        """
        ...
    
    def GetInPort(self, id: int) -> GvPort:
        """    
        Retrieves an inport by index.
        
        :type id: int
        :param id: the index
        :rtype: c4d.modules.graphview.GvPort
        :return: The GvPort or **None** if no port was found.
        
        
        """
        ...
    
    def GetOutPort(self, id: int) -> GvPort:
        """    
        Retrieves an outport by index.
        
        :type id: int
        :param id: the index
        :rtype: c4d.modules.graphview.GvPort
        :return: The GvPort or **None** if no port was found.
        
        
        """
        ...
    
    def GetInPortCount(self) -> int:
        """    
        Returns the count of the inports.
        
        :rtype: int
        :return: The count.
        
        
        """
        ...
    
    def GetOutPortCount(self) -> int:
        """    
        Returns the count of the outports.
        
        :rtype: int
        :return: The count
        
        
        """
        ...
    
    def SetOperatorContainer(self, bc: BaseContainer) -> None:
        """    
        Set the settings container.
        
        :type bc: c4d.BaseContainer
        :param str: The container.
        
        
        """
        ...
    
    def GetOpContainerInstance(self) -> BaseContainer:
        """    
        | Retrieves a pointer to the internal operator's container.
        | This means that the container can be changed directly.
        
        :rtype: c4d.BaseContainer
        :return: The container.
        
        
        """
        ...
    
    def GetOperatorContainer(self) -> BaseContainer:
        """    
        Returns the settings container.
        
        :rtype: c4d.BaseContainer
        :return: The container.
        
        
        """
        ...
    
    def AddPort(self, io: int, id: Union[int, DescID], flag: Optional[int] = ..., message: Optional[bool] = ...) -> GvPort:
        """    
        Adds a port to the node.
        
        .. note:: To add a port for a user data parameter create the :class:`DescID <c4d.DescID>` of that parameter:
        
        .. code-block:: python
        
        USERDATA_NUMBER = 1
        nodeObjOut.AddPort(c4d.GV_PORT_OUTPUT, c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA, c4d.DTYPE_SUBCONTAINER, 0), c4d.DescLevel(USERDATA_NUMBER)), message=True)
        
        :type io: int
        :param io: The IO mode of the port to create:
        
        .. include:: /consts/GV_PORT.rst
        :start-line: 3
        
        :type id: int
        :param id: The ID of the port to create.
        :type flag: int
        :param flag: Flags:
        
        .. include:: /consts/GV_PORT_FLAG.rst
        :start-line: 3
        
        :type message: bool
        :param message: If **True** the operator receives a message when the port is added.
        :rtype: c4d.modules.graphview.GvPort
        :return: The created port or **None** if creation failed.
        
        
        """
        ...
    
    def AddPortIsOK(self, io: int, id: int) -> bool:
        """    
        Checks if :meth:`AddPort` would be successful.
        
        :type io: int
        :param io: The port mode:
        
        .. include:: /consts/GV_PORT.rst
        :start-line: 3
        
        :type id: int
        :param id: The type id of the port.
        :rtype: bool
        :return: **True** if adding the port would succeed, otherwise **False**.
        
        
        """
        ...
    
    def OperatorSetData(self, type: int, data: Any, mode: int) -> bool:
        """    
        Sets data in the operator. Usually simulates dragging onto the node.
        
        .. versionadded:: R18.057
        
        :type type: int
        :param type: The data type:
        
        .. include:: /consts/GV.rst
        :start-line: 3
        
        :type data: any
        :param data: The data to set. Depends on *type*.
        :type mode: int
        :param mode: The set data mode:
        
        .. include:: /consts/GV_OP.rst
        :start-line: 3
        
        :rtype: bool
        :return: **True** if the data was set, otherwise **False**.
        
        
        """
        ...
    


def GetMaster(id: int) -> GvNodeMaster:
    """    
    Get one of the current active master nodes.
    
    :type id: long
    :param id: The ID of the master node.
    
    :rtype: c4d.modules.graphview.GvNodeMaster
    :return: The master node identified by *id*.
    
    
    """
    ...

def SetPrefs(bc: BaseContainer) -> None:
    """    
    The new preferences. Use these container IDs:
    
    :type bc: c4d.BaseContainer
    :param bc: The new preferences.
    
    .. include:: /consts/GV_WORLD_CONFIG.rst
    :start-line: 3
    
    
    """
    ...

def GetPrefs() -> BaseContainer:
    """    
    Gets the preferences for this world.
    
    :rtype: c4d.BaseContainer
    :return: A copy of the preferences.
    
    .. include:: /consts/GV_WORLD_CONFIG.rst
    :start-line: 3
    
    
    """
    ...

def OpenDialog(id: int, master: GvNodeMaster) -> bool:
    """    
    Opens the Xpresso dialog for a specific node master.
    
    :type id: int
    :param id: Plugin ID.
    :type master: c4d.modules.graphview.GvNodeMaster
    :param master: Node master to open the dialog for.
    :rtype: bool
    :return: **True** if the dialog was opened, otherwise **False**.
    
    
    """
    ...

def CloseDialog(id: int) -> None:
    """    
    Closes a dialog opened with :func:`OpenDialog`.
    
    :type id: int
    :param id: The ID that the dialog was opened with.
    
    
    """
    ...

def RedrawMaster(master: GvNodeMaster) -> None:
    """    
    Redraws the :class:`GvNodeMaster <c4d.modules.graphview.GvNodeMaster>`.
    
    :type master: c4d.modules.graphview.GvNodeMaster
    :param master: The nodemaster to redraw.
    
    
    """
    ...

def GetDefaultOperatorIcon(type: int) -> BaseBitmap:
    """    
    Gets the default operator icon for an operator *type*.
    
    :type type: int
    :param type: Operator type:
    
    .. include:: /consts/GV_OPERATOR_TYPE.rst
    :start-line: 3
    
    :rtype: c4d.bitmaps.BaseBitmap
    :return: The default operator icon.
    
    
    """
    ...

