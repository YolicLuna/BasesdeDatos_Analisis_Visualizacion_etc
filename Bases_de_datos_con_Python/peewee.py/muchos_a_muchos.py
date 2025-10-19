import peewee
#Se importa la libreria peewee para la conexion a la base de datos

database = peewee.MySQLDatabase("python_db",
                                host = "127.0.0.1",
                                port = 3306, 
                                user = "root",
                                passwd = "aqui_tu_contraseña")

class Product(peewee.Model):
    title = peewee.CharField(max_length=50)
    price = peewee.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        database = database
        db_table = "products"
        
    def __str__(self):
        return self.title
    
class Category(peewee.Model):
    title = peewee.CharField(max_length=20)

    class Meta:
        database = database
        db_table = "categories"
        
    def __str__(self):
        return self.title

class ProductCategory(peewee.Model):
    product = peewee.ForeignKeyField(Product, backref = "categories")
    category = peewee.ForeignKeyField(Category, backref = "products")

    class Meta:
        database = database
        db_table = "product_categories"
        
if __name__ == "__main__":
    
    database.drop_tables([Product, Category, ProductCategory])
    database.create_tables([Product, Category, ProductCategory])

    laptop = Product.create(title = "laptop", price = 4100.00)
    kit_teclado_mouse = Product.create(title = "kit_teclado_mouse", price = 350.00)
    smart_tv = Product.create(title = "smart_tv", price = 4800.00)

    Product.create(title = "pc_gamer", price = 16000.00)
    Product.create(title = "audifonos", price = 1100.00)
    Product.create(title = "bocina", price = 1800.00)

    technology = Category.create(title = "Technology")
    home = Category.create(title = "Home")

    ProductCategory.create(product=laptop, category=technology)
    ProductCategory.create(product=kit_teclado_mouse, category=technology)
    ProductCategory.create(product=smart_tv, category=technology)

    ProductCategory.create(product=smart_tv, category=home)

#    for product_category in technology.products:
#       print(product_category.product)

#    for product_category in smart_tv.categories:
#        print(product_category.category)


# Mostrar en consola todos los productos con sus categorias

# El siguiente codigo es lo que se conoce como un problema N+1 Query, así que, aun que funcione, no es recomendable utilizar esto.
    """
    for product in Product.select():
        for product_category in product.categories:
            print(product, "-", product_category.category) """

# En su lugar se deben usar Joins

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

# Listar en consola todos los productos que no posean una categoria
#LEFT JOIN

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