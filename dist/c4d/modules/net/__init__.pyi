from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable

from c4d import BaseContainer
from c4d.threading import BaseThread
from c4d.documents import BaseDocument
from uuid import UUID


class UserPool(object):
    def AddUser(self, username: str, password: str, description: str, isAdmin: bool) -> bool:
        """    
        Adds a user.
        
        :type username: str
        :param username: The user's name.
        :type password: str
        :param password: The user's password.
        :type description: str
        :param description: The user's description.
        :type isAdmin: bool
        :param isAdmin: Set to **True** if the user to add is administrator, **False** otherwise.
        :rtype: bool
        :return: **True** if the user was successfully added, **False** otherwise.
        
        
        """
        ...
    
    def DeleteUser(self, userUuid: Any) -> bool:
        """    
        Deletes a user.
        
        :type userUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param userUuid:
        
        .. versionadded:: R16.021
        
        The user UUID.
        
        :rtype: bool
        :return: **True** if the user was successfully deleted, **False** otherwise.
        
        
        """
        ...
    
    def CheckUserCredentials(self, username: str, password: str) -> bool:
        """    
        Checks a user's credentials.
        
        :type username: str
        :param username: The user name.
        :type password: str
        :param password: The user password.
        :rtype: bool
        :return: **True** if the user's credentials were successfully checked, otherwise **False**.
        
        
        """
        ...
    
    def EditUserInfo(self, userUuid: Any, description: str) -> bool:
        """    
        Sets a user's information.
        
        .. versionadded:: R16.021
        
        :type userUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param userUuid: The user UUID.
        :type description: str
        :param description: The new user description/information.
        :rtype: bool
        :return: **True** if the user's information was successfully set, otherwise **False**.
        
        
        """
        ...
    
    def EditUserPassword(self, userUuid: Any, password: str) -> bool:
        """    
        Sets a user's password.
        
        .. versionadded:: R16.021
        
        :type userUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param userUuid: The user UUID.
        :type password: str
        :param password: The new password.
        :rtype: bool
        :return: **True** if the user's password was successfully set, otherwise **False**.
        
        
        """
        ...
    
    def ChangeUserAccountType(self, userUuid: Any, isAdmin: bool) -> bool:
        """    
        Changes a user's account type.
        
        .. versionadded:: R16.021
        
        :type userUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param userUuid: The user UUID.
        :type isAdmin: bool
        :param isAdmin: Set to **True** to change the user's account type to administrator, **False** otherwise.
        :rtype: bool
        :return: **True** if the user's account type was successfully changed, otherwise **False**.
        
        
        """
        ...
    
    def ChangeLanguage(self, userUuid: Any, language: str) -> bool:
        """    
        Sets the language for a user.
        
        .. versionadded:: R16.021
        
        :type userUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param userUuid: The user UUID.
        :type language: str
        :param language: The new language.
        :rtype: bool
        :return: **True** if the user's password was successfully set, otherwise **False**.
        
        
        """
        ...
    
    def ChangePassword(self, userUuid: Any, oldPassword: str, newPassword: str) -> bool:
        """    
        Changes a user's password.
        
        :type userUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param userUuid:
        
        .. versionadded:: R16.021
        
        The user UUID.
        
        :type oldPassword: str
        :param oldPassword: The old user's password.
        :type newPassword: str
        :param newPassword: The new user's password.
        :rtype: bool
        :return: **True** if the user's password was successfully changed, otherwise **False**.
        
        
        """
        ...
    
    def GetUsers(self) -> None:
        """    
        Retrieves the users information from the pool.
        
        .. versionadded:: R16.021
        
        :rtype: list of dict{**username**, str, **description**: str, **uuid**: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_, , **isadmin**: bool, **language**: str}
        :return: The users information.
        
        
        """
        ...
    

class Repository(object):
    def GetRepositoryPath(self) -> str:
        """    
        Gets the repository path.
        
        .. versionadded:: R16.021
        
        :rtype: str
        :return: The default repository path.
        
        
        """
        ...
    
    def GetJobsPath(self, server: bool) -> str:
        """    
        Gets the jobs path.
        
        .. versionadded:: R16.021
        
        :type server: bool
        :param server: Pass **True** to ask for the jobs path on the server.
        :rtype: str
        :return: The jobs path.
        
        
        """
        ...
    
    def SetRepositoryPath(self, repositoryPath: str) -> None:
        """    
        Sets the repository path.
        
        .. versionadded:: R16.021
        
        :type repositoryPath: str
        :param repositoryPath: The repository path to set.
        
        
        """
        ...
    
    def ConvertRelative2Absolute(self) -> None:
        """    
        .. versionadded:: R16.021
        
        
        """
        ...
    
    def ConvertAbsolute2RelativePath(self) -> None:
        """    
        .. versionadded:: R16.021
        
        
        """
        ...
    

class RenderJob(object):
    def GetUuid(self) -> str:
        """    
        Get the uuid of the render job.
        
        :rtype: str
        :return: The uuid of the service.
        
        
        """
        ...
    
    def GetDefaultScene(self) -> None:
        """    
        Private.
        
        
        """
        ...
    

class NetRenderService(object):
    def GetUuid(self) -> None:
        """    
        Gets the UUID of the service.
        
        :rtype: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :return: The UUID of the service.
        
        
        """
        ...
    
    def Message(self, userUuid: Any, op: object, isPrivate: bool, msg: BaseContainer, result: Optional[BaseContainer] = ...) -> bool:
        """    
        Sends a message to the render service.
        
        .. versionadded:: R16.021
        
        :type userUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param userUuid: The user UUID.
        :type op: object
        :param op:
        :type isPrivate: bool
        :param isPrivate:
        :type msg: c4d.BaseContainer
        :param msg: The message container.
        :type result: c4d.BaseContainer
        :param result: The optional result container.
        :rtype: bool
        :return:
        
        
        """
        ...
    
    def ClearResults(self, jobUuid: Any) -> bool:
        """    
        Clears the results.
        
        .. versionadded:: R16.021
        
        :type jobUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid: The job UUID.
        :rtype: bool
        :return: **True** if results were cleared, otherwise **False**.
        
        
        """
        ...
    
    def RemoveResult(self, jobUuid: Any, relResultPath: str) -> bool:
        """    
        Remove the result for the given job.
        
        :type jobUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid: The job UUID.
        :type relResultPath: str
        :param relResultPath: File Path of the result path?
        :rtype: bool
        :return: **True** if results were removed, otherwise **False**.
        
        
        """
        ...
    
    def GetNetPreferences(self) -> BaseContainer:
        """    
        Retrieves the NET preferences.
        
        .. versionadded:: R16.021
        
        :rtype: c4d.BaseContainer
        :return: The NET preferences container. For the container IDs, see preferences dialog and `WPREF_NET` in the C++ API header `ge_prepass.h`.
        
        
        """
        ...
    
    def CopyRenderTaskFrom(self, jobUuid: Any, resolveMachineUuids: bool) -> None:
        """    
        Copy the Render Task matching the jobUuid.
        
        :type jobUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid: The job UUID.
        :type resolveMachineUuids: bool
        :param resolveMachineUuids: Currently ignored.
        :rtype: list(dict{"_frame": long, "_state": int, "_renderTime": int, "_machines": list[uuid]})
        :return: a list filled with dictionary representing each render task
        - _frame: The frame number.
        - _state: The render state.
        - _renderTime: The render time.
        - _machines: A list with all the machines assigned to the job.
        
        
        """
        ...
    
    def AddMachine(self, address: str, securityToken: str, allowGui: bool, uuidOfMachineToOverwrite: Any) -> bool:
        """    
        Adds a machine.
        
        .. versionadded:: R16.038
        
        :type address: str
        :param address: The machine address.
        :type securityToken: str
        :param securityToken: The security token.
        :type allowGui: bool
        :param allowGui: **True** to allow GUI, otherwise **False**.
        :type uuidOfMachineToOverwrite: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param uuidOfMachineToOverwrite: The UUID of the machine to overwrite.
        :rtype: bool
        :return: **True** if the machine was added successfully, otherwise **False**.
        
        
        """
        ...
    
    def GetAllMachineUuids(self, list: int, bits: int, includeLocalMachine: bool, includeBonjourMachines: bool) -> None:
        """    
        | Retrieves the UUIDs of all machines (with default parameters).
        | Parameters can be changed to filter the machines.
        
        :type list: int
        :param list: Machine list flags:
        
        .. include:: /consts/MACHINELIST.rst
        :start-line: 3
        
        :type bits: int
        :param bits: Verification bits:
        
        .. include:: /consts/VERIFICATIONBIT.rst
        :start-line: 3
        
        :type includeLocalMachine: bool
        :param includeLocalMachine: Pass **False** to not include local machine. Default to **True**.
        :type includeBonjourMachines: bool
        :param includeBonjourMachines: Pass **False** to not include Bonjour machines. Default to **True**.
        :rtype: list of `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :return: The list of all machine UUIDs.
        
        
        """
        ...
    
    def GetMachinesList(self, logCount: int, getOnlyThisMachine: Any) -> None:
        """    
        Retrieves the information of all machines.
        
        .. versionadded:: R16.021
        
        :type logCount: int
        :param logCount:
        
        .. versionadded:: R16.050
        
        The log count.
        
        :type getOnlyThisMachine: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param getOnlyThisMachine: Pass a machine UUID to get only the information for this machine.
        :rtype: list of :class:`BaseContainer <c4d.BaseContainer>`
        :return: The list of machines.
        
        
        """
        ...
    
    def GetUserPool(self) -> UserPool:
        """    
        Gets the user pool.
        
        :rtype: c4d.modules.net.UserPool
        :return: The user pool.
        
        
        """
        ...
    
    def GetJobsList(self, triggerWatchDog: bool, rdata: int, assets: int, results: int, log: int, selectedJob: Any, selectedJobOnly: bool, user: Any, settings: BaseContainer) -> None:
        """    
        Retrieves the render jobs.
        
        .. versionadded:: R16.021
        
        :type triggerWatchDog: bool
        :param triggerWatchDog:
        :type rdata: int
        :param rdata: The render data select flags:
        
        .. include:: /consts/DETAILSELECTOR.rst
        :start-line: 3
        
        :type assets: int
        :param assets: The assets data select flags:
        
        .. include:: /consts/DETAILSELECTOR.rst
        :start-line: 3
        
        :type results: int
        :param results: The results data select flags:
        
        .. include:: /consts/DETAILSELECTOR.rst
        :start-line: 3
        
        :type log: int
        :param log: The log data select flags:
        
        .. include:: /consts/DETAILSELECTOR.rst
        :start-line: 3
        
        :type selectedJob: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param selectedJob:
        :type selectedJobOnly: bool
        :param selectedJobOnly:
        :type user: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param user: The user UUID.
        :type settings: c4d.BaseContainer
        :param settings:
        
        .. versionadded:: R16.038
        
        The settings container.
        
        :rtype: list of :class:`BaseContainer <c4d.BaseContainer>`
        :return: The render jobs.
        
        
        """
        ...
    
    def CreateRenderJob(self, docName: str, jobUuid: Any, creator: int, username: str, bt: BaseThread, watchFolderName: str) -> int:
        """    
        Creates a render job.
        
        .. versionadded:: R16.021
        
        :type docName: str
        :param docName: The document name.
        :type jobUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid: The job UUID.
        :type creator: int
        :param creator: The render job creator:
        
        .. include:: /consts/RENDERJOBCREATOR.rst
        :start-line: 3
        
        :type username: str
        :param username: The user name.
        :type bt: c4d.threading.BaseThread
        :param bt: The thread.
        :type watchFolderName: str
        :param watchFolderName: The name of the folder to watch.
        :rtype: int
        :return: The result:
        
        .. include:: /consts/CREATEJOBRESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def StartRendering(self, mode: int, doc: BaseDocument, jobUuid: Any, bt: BaseThread) -> int:
        """    
        Starts a render job.
        
        .. versionadded:: R16.021
        
        :type mode: int
        :param mode: The thread mode:
        
        .. include:: /consts/THREADMODE.rst
        :start-line: 3
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :type jobUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid: The job UUID.
        :type bt: c4d.threading.BaseThread
        :param bt: The thread for the operation.
        :rtype: int
        :return: The result:
        
        .. include:: /consts/RENDERRESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def InitRendering(self, doc: BaseDocument, rdata: BaseContainer, jobUuid: UUID, flags: int, machines: BaseContainer) -> int:
        """    
        Initializes a render job.
        
        .. versionadded:: R16.021
        
        :type doc: c4d.documents.BaseDocument
        :param doc: The document.
        :type rdata: c4d.BaseContainer
        :param rdata: The render data.
        :type jobUuid: uuid.Uuid
        :param jobUuid: The job UUID.
        :type flags: int
        :param flags: The NET render flags:
        
        .. include:: /consts/NETRENDERFLAGS.rst
        :start-line: 3
        
        :type machines: c4d.BaseContainer
        :param machines: The machines container.
        :rtype: int
        :return: The result:
        
        .. include:: /consts/RENDERRESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def InitAndStartRenderingFullAsync(self, jobUuid: UUID) -> bool:
        """    
        Starts a render job fully asynchronous.
        
        .. versionadded:: R16.021
        
        :type jobUuid: uuid.Uuid
        :param jobUuid: The job UUID.
        :rtype: bool
        :return: **True** if rendering was started, otherwise **False**.
        
        
        """
        ...
    
    def StopRendering(self, mode: int, jobUuid: Any, result: int) -> None:
        """    
        Stops a render job.
        
        .. versionadded:: R16.021
        
        :type mode: int
        :param mode: The thread mode:
        
        .. include:: /consts/THREADMODE.rst
        :start-line: 3
        
        :type jobUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid: The job UUID.
        :type result: int
        :param result: The result:
        
        .. include:: /consts/RENDERRESULT.rst
        :start-line: 3
        
        
        """
        ...
    
    def DeleteRenderJob(self, jobUuid: Any, informClients: bool) -> bool:
        """    
        Deletes a render job.
        
        .. versionadded:: R16.021
        
        :type jobUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid: The job UUID.
        :type informClients: bool
        :param informClients:
        :rtype: bool
        :return: **True** if the render job was deleted, otherwise **False**.
        
        
        """
        ...
    
    def InsertJobAfter(self, jobUuid1: Any, jobUuid2: Any) -> bool:
        """    
        Inserts *jobUuid1* after *jobUuid2*.
        
        .. versionadded:: R16.021
        
        :type jobUuid1: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid1: The job to insert after *jobUuid2*.
        :type jobUuid2: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid2: The job to insert *jobUuid1* after.
        :rtype: bool
        :return: **True** if *jobUuid1* was inserted after *jobUuid2* otherwise **False**.
        
        
        """
        ...
    
    def InsertJobBefore(self, jobUuid1: Any, jobUuid2: Any) -> bool:
        """    
        Inserts *jobUuid1* before *jobUuid2*.
        
        .. versionadded:: R16.021
        
        :type jobUuid1: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid1: The job to insert before *jobUuid2*.
        :type jobUuid2: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid2: The job to insert *jobUuid1* before.
        :rtype: bool
        :return: **True** if *jobUuid1* was inserted before *jobUuid2* otherwise **False**.
        
        
        """
        ...
    
    def SetDefaultSceneName(self, jobUuid: Any, defaultSceneName: str) -> bool:
        """    
        Sets the Default Scene Name.
        
        .. versionadded:: R16.021
        
        :type jobUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid: The job UUID.
        :type defaultSceneName: str
        :param defaultSceneName: The default scene name.
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetRepository(self) -> Repository:
        """    
        Retrieves the repository for the service.
        
        .. versionadded:: R16.021
        
        :rtype: c4d.modules.net.Repository
        :return: The repository.
        
        
        """
        ...
    
    def AddLogToJob(self, jobUuid: Any, log: str, doLock: bool, append: bool) -> bool:
        """    
        Add a string to the job log.
        
        .. versionadded:: R16.021
        
        :type jobUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param jobUuid: The job UUID.
        :type log: str
        :param log: The string to add.
        :type doLock: bool
        :param doLock:
        :type append: bool
        :param append:
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def AddLogToMachine(self, jobUuid: Any, log: str, doLock: bool) -> bool:
        """    
        Adds a string to the machine log.
        
        .. versionadded:: R16.021
        
        :type machineUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
        :param machineUuid: The machine UUID.
        :type log: str
        :param log: The string to add.
        :type doLock: bool
        :param doLock:
        :rtype: bool
        :return: **True** if successful, otherwise **False**.
        
        
        """
        ...
    
    def GetName(self) -> str:
        """    
        Gets the name of the service.
        
        .. versionadded:: R16.021
        
        :rtype: str
        :return: The name of the service.
        
        
        """
        ...
    
    def NetConsoleOutput(self, flags: int, value: str) -> None:
        """    
        Prints a string to the service.
        
        .. versionadded:: R16.021
        
        :type flags: int
        :param flags: The console ouput flags:
        
        .. include:: /consts/OUTPUT.rst
        :start-line: 3
        
        :type value: str
        :param value: The string to output.
        
        
        """
        ...
    


def SetErrorLevel(printDebugErrors: bool, stackInErrors: bool, locationInErrors: bool) -> None:
    """    
    Sets the level for stack and location in errors.
    
    .. versionadded:: R16.038
    
    :type printDebugErrors: bool
    :param printDebugErrors:
    
    .. versionadded:: R16.050
    
    **True** to print debug errors, otherwise **False**.
    
    :type stackInErrors: bool
    :param stackInErrors: **True** to enable stack in errors, otherwise **False**.
    :type locationInErrors: bool
    :param locationInErrors: **True** to enable location in errors, otherwise **False**.
    
    
    """
    ...

def GetGlobalNetRenderService() -> NetRenderService:
    """    
    Get the global NET render service.
    
    :rtype: c4d.modules.net.NetRenderService
    :return: The global NET render service.
    
    
    """
    ...

def VerificationStateToString(state: int) -> str:
    """    
    Format a verification *state* as a string.
    
    :type state: int
    :param state: The verification state:
    
    .. include:: /consts/VERIFICATIONBIT.rst
    :start-line: 3
    
    :rtype: str
    :return: The formatted verification state.
    
    
    """
    ...

def JobCommandToString(command: int) -> str:
    """    
    Format a job *command* as a string.
    
    :type command: int
    :param command: The job command:
    
    .. include:: /consts/JOBCOMMAND.rst
    :start-line: 3
    
    :rtype: str
    :return: The formatted job command.
    
    
    """
    ...

def JobStateToString(state: Any) -> str:
    """    
    Format a job *state* as a string.
    
    .. versionadded:: R16.021
    
    :type command: int
    :param command: The job state:
    
    .. include:: /consts/JOBSTATE.rst
    :start-line: 3
    
    :rtype: str
    :return: The formatted job state.
    
    
    """
    ...

def NetSpecialEventAdd(service: NetRenderService, remoteUuid: Any, msg: BaseContainer, forceConnect: bool) -> bool:
    """    
    Adds a custom event over NET.
    
    .. versionadded:: R16.021
    
    :type service: c4d.modules.net.NetRenderService
    :param service: The NET render service.
    :type remoteUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
    :param remoteUuid: The machine to send the message to.
    :type msg: c4d.BaseContainer
    :param msg: The message container.
    :type forceConnect: bool
    :param forceConnect: Private.
    :rtype: bool
    :return: **True** if successful, otherwise **False**.
    
    
    """
    ...

def NetGeSyncMessage(service: NetRenderService, remoteUuid: Any, msg: BaseContainer, forceConnect: bool) -> None:
    """    
    Sends a synchronous event message over NET.
    
    .. versionadded:: R16.021
    
    :type service: c4d.modules.net.NetRenderService
    :param service: The NET render service.
    :type remoteUuid: `UUID <https://docs.python.org/release/2.7/library/uuid.html#uuid.UUID>`_
    :param remoteUuid: The machine to send the message to.
    :type msg: c4d.BaseContainer
    :param msg: The message container.
    :type forceConnect: bool
    :param forceConnect: Private.
    :rtype: tuple(bool, :class:`BaseContainer <c4d.BaseContainer>`)
    :return: The successful status and result container.
    
    
    """
    ...

