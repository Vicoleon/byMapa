import reflex as rx


class NavigationState(rx.State):
    cart_count: int = 0
    mobile_menu_open: bool = False
    current_section: str = "home"
    nav_items: list[dict[str, str]] = [
        {"label": "New In", "href": "/#new-in"},
        {"label": "Ropa", "href": "/ropa"},
        {"label": "Sets", "href": "/sets"},
        {"label": "Accesorios", "href": "/accesorios"},
    ]

    @rx.event
    def toggle_mobile_menu(self):
        self.mobile_menu_open = not self.mobile_menu_open

    @rx.event
    def increment_cart(self):
        self.cart_count += 1

    @rx.event
    def set_current_section(self, section: str):
        self.current_section = section
        self.mobile_menu_open = False