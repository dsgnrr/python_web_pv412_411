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
    Product(0, 'first-product', 'First Product', 'description product 1'),
    Product(1, 'second-product', 'Second Product', 'description product 2'),
    Product(2, 'third-product', 'Third Product', 'description product 3'),
    Product(3, 'fourth-product', 'Fourth Product', 'description product 4'),
]
