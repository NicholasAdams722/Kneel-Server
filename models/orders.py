class Order():
    """Class that defines the properties for a metal object"""

    # Write the __init__ method here
    def __init__(self, id, metal_Id, size_Id, style_Id, timestamp):
        self.id = id
        self.metal_Id = metal_Id
        self.size_Id = size_Id
        self.style_Id = style_Id
        self.timestamp = timestamp
