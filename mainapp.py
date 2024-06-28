from fastapi import FastAPI

app = FastAPI()

price_list = {"beer": 5,
              "soda": 1,
              "lotto": 5,
              "gel": 4,
              "eggs": 6,
              }


@app.get("/")
def get_home():
    return 'WLCOME TO HOME'


@app.get("/products/{product}")
def get_product(product: str):
    return get_price(product)


def get_price(product: str):
    price = f" Price of the product named -> {product} = {price_list[product]}"
    return price
