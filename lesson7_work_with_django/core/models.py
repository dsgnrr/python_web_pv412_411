from . import utils

class Product:
    id: int
    slug: str
    name: str
    description: str
    
    def __init__(self, id, slug, name, description):
        self.id = id
        self.slug = slug
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"""
    <h3>{self.name}</h3>
    <h4>slug: {self.slug}</h4>
    <h4>id: {self.id}</h4>
    <p>{self.description}</p>
    """
    
products = [
    Product(utils.get_current_timestamp(), 'first-product', 'First Product', 'description product 1'),
    Product(utils.get_current_timestamp(), 'second-product', 'Second Product', 'description product 2'),
    Product(utils.get_current_timestamp(), 'third-product', 'Third Product', 'description product 3'),
    Product(utils.get_current_timestamp(), 'fourth-product', 'Fourth Product', 'description product 4'),
]
