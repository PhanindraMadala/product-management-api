from behave import given
from service.models import Product

@given('the database contains the following products')
def step_impl(context):
    for row in context.table:
        product = Product(name=row['name'], category=row['category'], availability=row['availability'])
        product.save()
 
