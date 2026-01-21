from MMS.Message import Message

class Channel :
    """
    Channel is used to group messages of a same subject. It contains all the messages
    related to this channel's subject and permit the user to view all messages and find
    a specific one if needed.
    """

    id : int
    """ Unique identifier of the channel """

    name : str
    """ Name of the channel """
    
    messages = list()
    """ List of all messages related to this channel """

    def __init__(self, id : int, name : str) -> None :
        """
        Create a new channel with an unique identifier and a name.
        
        :param id: This channel's unique identifier
        :type id: int
        :param name: This channel's name
        :type name: str
        """
        
        self.id = id
        self.name = name
    
    def get_last_message(self) -> Message :
        """
        If this channel's messages list is empty, return nothing.
        If not empty, return the last message added to the list.
        
        :return: The last message added to this channel
        :rtype: Message
        """
        nb = len(self.messages)
        if nb > 0 :
            return self.messages[nb - 1]
        else :
            return None
    
    def get_all_messages(self) -> list[Message] :
        """
        If this channel's list of messages is empty, return None.
        If not empty, return all messages as a list.
        
        :return: All messages in this channel
        :rtype: list[Message]
        """
        if len(self.messages) > 0 :
            return self.messages
        else :
            return None

    def add_message(self, importance : int, string : str) -> None :
        """
        Add a message to this channel, by providing the importance level and the actual message.
        
        :param importance: The new message's importance level
        :type importance: int
        :param string: The new message's actual message
        :type string: str
        """
        if len(self.messages) == 0 :
            self.messages.append(Message(0, importance, string))
        else :
            self.messages.append(Message(self.messages[len(self.messages) - 1].id + 1, importance, string))
        return None