from Message import Message
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

    def __init__(self, id : int, name : str) -> list[Message] :
        """
        Create a new channel with an unique identifier and a name.
        
        :param id: Channel's unique identifier
        :param name: Channel's name
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

    def add_message(self, importance, string) -> None :
        if len(self.messages) == 0 :
            self.messages.append(Message(0, importance, string))
        else :
            self.messages.append(Message(self.messages[len(self.messages) - 1].id + 1, importance, string))
        return None