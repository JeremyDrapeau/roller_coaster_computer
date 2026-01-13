# datetime is used to timestamp messages
from datetime import datetime


class Message :
    """
    The message class represents a message in the computer's memory. It can be used to log
    information on information rettrieved from sensors by the computer. Messages have multiple
    use cases, has they are also the class used for warnings and errors.
    """

    id : int
    """Unique message identifier"""
    
    importance : int
    """Importance level (0=low importance, 99=high importance)"""
    
    string : str
    """The actual message as a string"""

    timestamp : datetime
    """Date and time of message creation"""
 
    def __init__(self, id, importance, string) -> None:
        """
        Create a message. The "timestamp" variable is automaticaly setted to the current
        computer's time.
        
        :param id: The message's unique identifier.
        :param importance: The message's importance (0=low importance, 99=high importance).
        :param string: The message's message as a string.
        """
        self.id = id
        self.importance = importance
        self.string = string

        # timestamp is automaticaly set (based on this computer's current time) so there's no
        # need to provide a source of time
        self.timestamp = datetime.now()

    def get_id(self) -> int :
        """
        Getter of the "id" variable of this message.

        :return: This message's unique identifier
        :rtype: int
        """
        return self.id

    def get_importance(self) -> int :
        """
        Getter of the "importance" variable of this message.

        :return: This message's importance level (0=low importance, 99=high importance)
        :rtype: int
        """
        return self.importance

    def get_string(self) -> str :
        """
        Getter of the "string" variable of this message.

        :return: This message's actual message as a string
        :rtype: str
        """
        return self.string
    
    def get_timestamp(self) -> datetime :
        """
        Getter of the "timestamp" variable of this message.

        :return: This message's date and time of it's creation
        :rtype: datetime
        """
        return self.timestamp