from .models import *

from faker import Faker



def generate_fake_date():
    # Create categories
    fake = Faker()
    categories = [
        Category(name="Electronics"),
        Category(name="Clothing"),
        Category(name="Home Decor"),
    ]
    Category.objects.bulk_create(categories)
    
    # Create brands
    brands = [
        Brand(name="Apple"),
        Brand(name="Nike"),
        Brand(name="IKEA"),
    ]
    Brand.objects.bulk_create(brands)
    
    # Create products
    products = []
    for _ in range(10):
        product = Product(
            name=fake.word(),
            category=categories[fake.random_int(min=0, max=len(categories)-1)],
            brand=brands[fake.random_int(min=0, max=len(brands)-1)],
            stock=fake.random_int(min=0, max=100),
        )
        products.append(product)
    Product.objects.bulk_create(products)
    
    # Create firms
    firms = []
    for _ in range(5):
        firm = Firm(
            name=fake.company(),
            phone=fake.phone_number(),
            address=fake.address(),
        )
        firms.append(firm)
    Firm.objects.bulk_create(firms)
    
    # Create users
    users = User.objects.all()
    
    # Create purchases
    purchases = []
    for _ in range(10):
        purchase = Purchase(
            user=users[fake.random_int(min=0, max=len(users)-1)],
            product=products[fake.random_int(min=0, max=len(products)-1)],
            firm=firms[fake.random_int(min=0, max=len(firms)-1)],
            quantity=fake.random_int(min=1, max=10),
            price=fake.pydecimal(min_value=10, max_value=100, right_digits=2),
        )
        purchases.append(purchase)
    Purchase.objects.bulk_create(purchases)
    
    # Create sales
    sales = []
    for _ in range(10):
        sale = Sale(
            user=users[fake.random_int(min=0, max=len(users)-1)],
            product=products[fake.random_int(min=0, max=len(products)-1)],
            quantity=fake.random_int(min=1, max=10),
            price=fake.pydecimal(min_value=10, max_value=100, right_digits=2),
        )
        sales.append(sale)
    Sale.objects.bulk_create(sales)

