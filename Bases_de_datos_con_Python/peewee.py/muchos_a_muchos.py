# Se importa la libreria peewee para la conexion a la base de datos
import peewee

# Se crea la conexion a la base de datos MySQL
database = peewee.MySQLDatabase("python_db",
                                host = "127.0.0.1",
                                port = 3306, 
                                user = "root",
                                passwd = "aqui_tu_contraseña")

# Se crea la clase Product que representa la tabla products
class Product(peewee.Model):
    title = peewee.CharField(max_length=50)
    price = peewee.DecimalField(max_digits=10, decimal_places=2)
    # Se crea la clase Meta para definir la base de datos y el nombre de la tabla
    class Meta:
        database = database
        db_table = "products"
    # Se crea el metodo __str__ para mostrar el titulo del producto
    def __str__(self):
        return self.title

# Se crea la clase Category que representa la tabla categories
class Category(peewee.Model):
    title = peewee.CharField(max_length=20)
    # Se crea la clase Meta para definir la base de datos y el nombre de la tabla
    class Meta:
        database = database
        db_table = "categories"
    # Se crea el metodo __str__ para mostrar el titulo de la categoria    
    def __str__(self):
        return self.title

# Se crea la clase ProductCategory que representa la tabla product_categories
class ProductCategory(peewee.Model):
    product = peewee.ForeignKeyField(Product, backref = "categories")
    category = peewee.ForeignKeyField(Category, backref = "products")
    # Se crea la clase Meta para definir la base de datos y el nombre de la tabla
    class Meta:
        database = database
        db_table = "product_categories"

# Se crea la funcion main  
if __name__ == "__main__":
    # Se crean las tablas en la base de datos, primero se eliminan si ya existen y luego se crean de nuevo.
    database.drop_tables([Product, Category, ProductCategory])
    database.create_tables([Product, Category, ProductCategory])

    # Se crean los productos definiendolos como una variable para luego usarlos en la tabla intermedia
    laptop = Product.create(title = "laptop", price = 4100.00)
    kit_teclado_mouse = Product.create(title = "kit_teclado_mouse", price = 350.00)
    smart_tv = Product.create(title = "smart_tv", price = 4800.00)

    # Se crean mas productos sin necesidad de definirlos como variable
    Product.create(title = "pc_gamer", price = 16000.00)
    Product.create(title = "audifonos", price = 1100.00)
    Product.create(title = "bocina", price = 1800.00)

    # Se crean las categorias definiendolas como una variable para luego usarlas en la tabla intermedia
    technology = Category.create(title = "Technology")
    home = Category.create(title = "Home")

    # Se crean las relaciones muchos a muchos en la tabla intermedia
    ProductCategory.create(product=laptop, category=technology)
    ProductCategory.create(product=kit_teclado_mouse, category=technology)
    ProductCategory.create(product=smart_tv, category=technology)
    ProductCategory.create(product=smart_tv, category=home)

    # Este codigo muestra como acceder a las relaciones muchos a muchos
    """
    for product_category in technology.products:
       print(product_category.product)
    """

    # Este codigo muestra como acceder a las relaciones muchos a muchos de otra forma
    """
    for product_category in smart_tv.categories:
        print(product_category.category)
    """

    # El siguiente codigo es lo que se conoce como un problema N+1 Query, así que, aun que funcione, no es recomendable utilizar esto.
    """
    for product in Product.select():
        for product_category in product.categories:
            print(product, "-", product_category.category) 
    """

    # En su lugar se deben usar Joins
    # Este es un INNER JOIN, que meustra solo los productos que tienen categorias asignadas
    for product in Product.select(
        Product.title, Category.title
    ).join(
        ProductCategory
    ).join(Category, 
        on = (
            ProductCategory.category_id == Category.id
        )
    ):
        print(product, "-", product.productcategory.category)

    # Este es un LEFT JOIN, que muestra todos los productos, incluyendo los que no tienen categorias asignadas
    products = Product.select(
        Product.title
    ).join(
        ProductCategory,
        peewee.JOIN.LEFT_OUTER
    ).where(
        ProductCategory.id == None
    )

    for product in products:
        print(product.title)

        