import reflex as rx
from typing import TypedDict, Optional
from app.states.auth_state import AuthState


class AdminUser(TypedDict):
    id: int
    name: str
    email: str
    role: str
    status: str


class OrderItem(TypedDict):
    name: str
    quantity: int
    price: float


class Order(TypedDict):
    id: str
    customer: str
    email: str
    date: str
    total: float
    status: str
    items_count: int
    items_list: list[OrderItem]
    address: str


class AdminProduct(TypedDict):
    id: int
    name: str
    price: float
    image: str
    tagline: str
    description: str
    category: str
    pieces: str | None
    stock: int
    status: str


class ContentData(TypedDict):
    announcement_text: str
    announcement_active: bool
    hero_line1: str
    hero_line2: str
    hero_line3: str
    hero_subtitle: str
    hero_cta: str
    hero_bg_color: str
    cat_ropa_title: str
    cat_ropa_subtitle: str
    cat_sets_title: str
    cat_sets_subtitle: str
    cat_acc_title: str
    cat_acc_subtitle: str
    newsletter_head: str
    newsletter_desc: str
    newsletter_btn: str


class StoreSettings(TypedDict):
    name: str
    tagline: str
    email: str
    instagram: str
    tiktok: str
    free_shipping_threshold: float
    standard_shipping: float
    express_shipping: float
    notify_orders: bool
    notify_low_stock: bool
    notify_registrations: bool
    primary_color: str
    secondary_color: str
    font_family: str


class AdminState(rx.State):
    active_section: str = "dashboard"
    content_tab: str = "announcement"
    is_user_modal_open: bool = False
    editing_user_id: int | None = None
    user_form_name: str = ""
    user_form_email: str = ""
    user_form_role: str = "viewer"
    users_list: list[AdminUser] = [
        {
            "id": 1,
            "name": "Super Admin",
            "email": "admin@bymapa.com",
            "role": "super_admin",
            "status": "Active",
        },
        {
            "id": 2,
            "name": "Admin Manager",
            "email": "manager@bymapa.com",
            "role": "admin",
            "status": "Active",
        },
    ]
    content_data: ContentData = {
        "announcement_text": "El nuevo drop llegó — Descúbrelo",
        "announcement_active": True,
        "hero_line1": "Color.",
        "hero_line2": "Actitud.",
        "hero_line3": "Tú.",
        "hero_subtitle": "La moda que no pide permiso.",
        "hero_cta": "Ver el drop",
        "hero_bg_color": "#f8f8f8",
        "cat_ropa_title": "ROPA",
        "cat_ropa_subtitle": "Piezas que hablan por ti.",
        "cat_sets_title": "SETS",
        "cat_sets_subtitle": "Combinar nunca fue tan fácil.",
        "cat_acc_title": "ACCESORIOS",
        "cat_acc_subtitle": "El detalle que lo cambia todo.",
        "newsletter_head": "SUSCRÍBETE AL INNER CIRCLE",
        "newsletter_desc": "Drops exclusivos. First access. Sin spam, solo estilo.",
        "newsletter_btn": "Unirme",
    }
    settings_data: StoreSettings = {
        "name": "BY MAPA",
        "tagline": "Editorial Fashion House",
        "email": "hola@bymapa.com",
        "instagram": "@bymapa",
        "tiktok": "@bymapa_official",
        "free_shipping_threshold": 150.0,
        "standard_shipping": 15.0,
        "express_shipping": 25.0,
        "notify_orders": True,
        "notify_low_stock": True,
        "notify_registrations": False,
        "primary_color": "#E91E8C",
        "secondary_color": "#000000",
        "font_family": "Inter",
    }
    products_list: list[AdminProduct] = []
    orders_list: list[Order] = []
    product_search: str = ""
    is_product_modal_open: bool = False
    editing_product_id: int | None = None
    product_form: dict = {}
    order_filter_tab: str = "Todos"
    is_order_modal_open: bool = False
    selected_order_id: str = ""

    @rx.event
    def set_section(self, section: str):
        self.active_section = section

    @rx.event
    def set_content_tab(self, tab: str):
        self.content_tab = tab

    @rx.event
    def update_content_field(self, key: str, value: str):
        self.content_data[key] = value

    @rx.event
    def toggle_announcement(self):
        self.content_data["announcement_active"] = not self.content_data[
            "announcement_active"
        ]

    @rx.event
    def save_content(self):
        rx.toast("Contenido actualizado exitosamente", duration=3000)

    @rx.event
    def update_settings_field(self, key: str, value: str):
        self.settings_data[key] = value

    @rx.event
    def toggle_setting(self, key: str):
        self.settings_data[key] = not self.settings_data[key]

    @rx.event
    def save_settings(self):
        rx.toast("Configuración guardada correctamente", duration=3000)

    @rx.event
    def reset_settings(self):
        self.settings_data["primary_color"] = "#E91E8C"
        self.settings_data["notify_orders"] = True
        rx.toast("Valores restaurados por defecto", duration=3000)

    @rx.var
    def total_products_count(self) -> int:
        return len(self.products_list)

    @rx.var
    def total_orders_count(self) -> int:
        return len(self.orders_list)

    @rx.var
    def total_revenue(self) -> str:
        return "$0.00"

    @rx.var
    def active_users_count(self) -> int:
        return len(self.users_list)

    @rx.var
    def filtered_products(self) -> list[AdminProduct]:
        return self.products_list

    @rx.var
    def filtered_orders(self) -> list[Order]:
        return self.orders_list

    @rx.var
    def selected_order(self) -> Order | None:
        return None