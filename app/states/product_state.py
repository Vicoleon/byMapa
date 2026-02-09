import reflex as rx
from typing import TypedDict


class Product(TypedDict):
    id: int
    name: str
    price: str
    image: str
    tagline: str
    description: str
    category: str
    pieces: str | None


class ProductState(rx.State):
    products: list[Product] = [
        {
            "id": 1,
            "name": "EL VESTIDO STATEMENT",
            "price": "$89.00",
            "image": "/fashion_editorial_photography.png",
            "tagline": "Fucsia eléctrico para no pasar desapercibida.",
            "description": "El color que enciende cualquier momento.",
            "category": "Vestidos",
            "pieces": None,
        },
        {
            "id": 2,
            "name": "POWER BLAZER",
            "price": "$120.00",
            "image": "/fashion_photography_high.png",
            "tagline": "Estructura y confianza.",
            "description": "Pieza esencial editorial.",
            "category": "Tops",
            "pieces": None,
        },
        {
            "id": 3,
            "name": "SUNSET SET",
            "price": "$75.00",
            "image": "/fashion_editorial_photography.png",
            "tagline": "Atardecer en tu piel.",
            "description": "Dos piezas coordinadas.",
            "category": "Sets",
            "pieces": "2 PIEZAS",
        },
        {
            "id": 4,
            "name": "PANTALÓN FLOW",
            "price": "$65.00",
            "image": "/fashion_photography_high.png",
            "tagline": "Movimiento puro.",
            "description": "Actitud en cada paso.",
            "category": "Pantalones",
            "pieces": None,
        },
        {
            "id": 5,
            "name": "TOP ATREVIDO",
            "price": "$45.00",
            "image": "/fashion_editorial_photography.png",
            "tagline": "Corte asimétrico.",
            "description": "Diseño audaz.",
            "category": "Tops",
            "pieces": None,
        },
        {
            "id": 6,
            "name": "FALDA VIBE",
            "price": "$55.00",
            "image": "/fashion_photography_high.png",
            "tagline": "Efecto satinado.",
            "description": "Perfecta para el día.",
            "category": "Faldas",
            "pieces": None,
        },
        {
            "id": 7,
            "name": "CAMISA ACTITUD",
            "price": "$70.00",
            "image": "/fashion_editorial_photography.png",
            "tagline": "Oversized fit.",
            "description": "Clásico moderno.",
            "category": "Tops",
            "pieces": None,
        },
        {
            "id": 8,
            "name": "BOLSO STATEMENT",
            "price": "$45.00",
            "image": "/accessories_photography_fashion.png",
            "tagline": "Detalle único.",
            "description": "Cuero vegano.",
            "category": "Bolsos",
            "pieces": None,
        },
        {
            "id": 9,
            "name": "ARETES DRAMA",
            "price": "$25.00",
            "image": "/accessories_photography_fashion.png",
            "tagline": "XL impact.",
            "description": "Acabado dorado.",
            "category": "Joyería",
            "pieces": None,
        },
        {
            "id": 10,
            "name": "GAFAS ATTITUDE",
            "price": "$55.00",
            "image": "/accessories_photography_fashion.png",
            "tagline": "Retro vibes.",
            "description": "Protección UV.",
            "category": "Gafas",
            "pieces": None,
        },
        {
            "id": 11,
            "name": "SET GOLDEN HOUR",
            "price": "$150.00",
            "image": "/fashion_editorial_photography.png",
            "tagline": "Lujo relajado.",
            "description": "Seda italiana.",
            "category": "Sets",
            "pieces": "3 PIEZAS",
        },
        {
            "id": 12,
            "name": "SET ELECTRIC",
            "price": "$110.00",
            "image": "/fashion_photography_high.png",
            "tagline": "Noches infinitas.",
            "description": "Energía pura.",
            "category": "Sets",
            "pieces": "2 PIEZAS",
        },
    ]
    newsletter_email: str = ""
    selected_size: str = ""
    details_open: bool = False
    category_filter: str = "Todo"

    @rx.var
    def current_product(self) -> Product:
        product_id = self.router.url.query_parameters.get("id", "1")
        for p in self.products:
            if str(p["id"]) == product_id:
                return p
        return self.products[0]

    @rx.var
    def filtered_ropa(self) -> list[Product]:
        ropa_cats = ["Vestidos", "Tops", "Pantalones", "Faldas"]
        if self.category_filter == "Todo":
            return [p for p in self.products if p["category"] in ropa_cats]
        return [p for p in self.products if p["category"] == self.category_filter]

    @rx.var
    def filtered_sets(self) -> list[Product]:
        return [p for p in self.products if p["category"] == "Sets"]

    @rx.var
    def filtered_accesorios(self) -> list[Product]:
        acc_cats = ["Bolsos", "Joyería", "Gafas"]
        if self.category_filter == "Todo":
            return [p for p in self.products if p["category"] in acc_cats]
        return [p for p in self.products if p["category"] == self.category_filter]

    @rx.event
    def set_filter(self, category: str):
        self.category_filter = category

    @rx.event
    def select_size(self, size: str):
        self.selected_size = size

    @rx.event
    def toggle_details(self):
        self.details_open = not self.details_open

    @rx.event
    def handle_newsletter_submit(self, form_data: dict):
        self.newsletter_email = form_data.get("email", "")
        return rx.toast(
            f"Bienvenida al Inner Circle, {self.newsletter_email}!", duration=3000
        )