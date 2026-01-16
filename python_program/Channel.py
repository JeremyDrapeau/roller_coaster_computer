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
        """
        Add a message to this channel. After adding the message, it can be
        accessed via function that retrieves messages from this channel.
        
        :param importance: The level of importance of this message
        :param string: The message's actual message (Can describe error,
        alert, etc...)
        """
        if len(self.messages) == 0 :
            self.messages.append(Message(0, importance, string))
        else :
            self.messages.append(Message(self.messages[len(self.messages) - 1].id + 1, importance, string))
        return None
    
    def get_message_with_importance(self, importance) -> list[Message] :
        """
        Returns all the messages with the importance specified in the parameter
        from this channel.

        :param importance: Importance level of messages to search for
        :return: List of all messages found in this channel with the importance
        level specified in the parameter of the function.
        :rtype: list[Message]
        """
        msg_list = list()
        for i in self.messages :
            if i.importance == importance :
                msg_list.append(i)
        return msg_list
    
    def get_message_importance_range(self, min, max) -> list[Message] :
        """
        Returns all the messages in this channel within the importance range
        specified in the method's parameter.

        :param min: Minimum importance to search for
        :param max: Maximum importance to search for
        :return: List of all messages found in this channel with the importance
        level range specified in the parameters of the function.
        :rtype: list[Message]
        """
        msg_list = list()
        for i in self.messages :
            if i.importance >= min and i.importance <= max :
                msg_list.append(i)
        return msg_list