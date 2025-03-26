import factory
from service.models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("word")
    category = factory.Faker("word")
    price = factory.Faker("random_int", min=10, max=1000)
    availability = factory.Faker("boolean")
 
