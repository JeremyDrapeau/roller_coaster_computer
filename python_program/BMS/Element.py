class Element :
    """
    Class that represents the basic elements of an element. Used to give an id and
    a name to the element.
    """
    
    id : int
    """ Unique identifier for this element """
    name : str
    """ Name for this element """
    
    def __init__(self, id : int, name : str) -> None:
        """
        Initialise the element by giving it a unique identifier and a name.
        
        :param id: This element's unique identifier
        :type id: int
        :param name: This element's name
        :type name: str
        """
        self.id = id
        self.name = name