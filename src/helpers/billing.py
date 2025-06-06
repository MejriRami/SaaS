import stripe 
from  decouple import config

DJANGO_DEBUG=config("DJANGO_DEBUG", cast=bool, default=False)
STRIPE_SECRET_KEY=config("STRIPE_SECRET_KEY", cast=str)

if "sk_test" in STRIPE_SECRET_KEY and not DJANGO_DEBUG:
    raise Exception("iNvalid stirpe key for prod ")

stripe.api_key = STRIPE_SECRET_KEY


def create_customer(name="",email="",raw=False):
    response=stripe.Customer.create(
        name=name,
        email=email,
        )
    if raw:
        return response
    stripe_id=response.id
    return stripe_id



def create_customer(name="",email="",raw=False):
    response=stripe.Customer.create(
        name=name,
        email=email,
        )
    if raw:
        return response
    stripe_id=response.id
    return stripe_id




