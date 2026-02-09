import reflex as rx
from app.components.navigation import announcement_bar, navbar
from app.components.hero import hero_section
from app.components.sections import (
    the_drop_section,
    marquee_break,
    trend_edit_section,
    newsletter_section,
)
from app.components.footer import footer
from app.states.product_state import ProductState
from app.states.navigation_state import NavigationState
from app.states.auth_state import AuthState
from app.states.admin_state import AdminState
from app.components.admin_components import (
    admin_sidebar,
    dashboard_view,
    users_view,
    products_view,
    orders_management_view,
    content_management_view,
    settings_view,
)
from app.components.category_layout import category_page_layout


def index() -> rx.Component:
    return rx.el.main(
        announcement_bar(),
        navbar(),
        hero_section(),
        the_drop_section(),
        marquee_break(),
        trend_edit_section(),
        newsletter_section(),
        footer(),
        class_name="font-['Inter'] selection:bg-[#E91E8C] selection:text-white",
    )


def ropa_page() -> rx.Component:
    return category_page_layout(
        title="ROPA",
        subtitle="Diseños que desafían lo convencional. / Editorial ready.",
        filters=["Todo", "Vestidos", "Tops", "Pantalones", "Faldas"],
        products_var=ProductState.filtered_ropa,
    )


def sets_page() -> rx.Component:
    return category_page_layout(
        title="SETS",
        subtitle="Coordinación sin esfuerzo. Impacto máximo.",
        filters=["Todo"],
        products_var=ProductState.filtered_sets,
    )


def accesorios_page() -> rx.Component:
    return category_page_layout(
        title="ACCESORIOS",
        subtitle="El punto final de cualquier declaración de estilo.",
        filters=["Todo", "Bolsos", "Joyería", "Gafas"],
        products_var=ProductState.filtered_accesorios,
    )


def login_page() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("arrow-left", class_name="h-4 w-4 mr-2"),
                    "VOLVER AL SHOP",
                    href="/",
                    class_name="text-[10px] font-black tracking-widest text-gray-400 hover:text-black transition-colors mb-12 flex items-center",
                ),
                rx.el.div(
                    rx.el.h1(
                        "ACCESO INTERNO",
                        class_name="text-4xl font-black tracking-tighter mb-2",
                    ),
                    rx.el.p(
                        "Solo personal autorizado.",
                        class_name="text-gray-500 font-medium mb-8",
                    ),
                    rx.el.form(
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "EMAIL",
                                    class_name="text-[10px] font-black block mb-2",
                                ),
                                rx.el.input(
                                    name="email",
                                    type="email",
                                    placeholder="admin@bymapa.com",
                                    class_name="w-full border-b-2 border-black py-3 focus:outline-none focus:border-[#E91E8C] transition-colors text-sm font-bold",
                                ),
                                class_name="mb-6",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "CONTRASEÑA",
                                    class_name="text-[10px] font-black block mb-2",
                                ),
                                rx.el.input(
                                    name="password",
                                    type="password",
                                    placeholder="********",
                                    class_name="w-full border-b-2 border-black py-3 focus:outline-none focus:border-[#E91E8C] transition-colors text-sm font-bold",
                                ),
                                class_name="mb-10",
                            ),
                            rx.el.button(
                                "INICIAR SESIÓN",
                                type="submit",
                                class_name="w-full py-4 bg-black text-white font-black tracking-[0.3em] hover:bg-[#E91E8C] transition-all",
                            ),
                        ),
                        on_submit=AuthState.login,
                    ),
                ),
                class_name="max-w-md w-full bg-white p-12",
            ),
            class_name="min-h-screen w-full flex items-center justify-center bg-[#f8f8f8]",
        ),
        class_name="font-['Inter']",
    )


def admin_dashboard() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            admin_sidebar(),
            rx.el.main(
                rx.match(
                    AdminState.active_section,
                    ("dashboard", dashboard_view()),
                    ("users", users_view()),
                    ("products", products_view()),
                    ("orders", orders_management_view()),
                    ("content", content_management_view()),
                    ("settings", settings_view()),
                    dashboard_view(),
                ),
                class_name="flex-1 p-12 h-screen overflow-y-auto bg-[#f8f8f8] font-['Inter']",
            ),
            class_name="flex h-screen w-full",
        )
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap",
            rel="stylesheet",
        ),
        rx.el.style("""
            .animate-marquee {
                display: flex;
                animation: marquee 20s linear infinite;
            }
            @keyframes marquee {
                0% { transform: translateX(0); }
                100% { transform: translateX(-50%); }
            }
        """),
    ],
)
app.add_page(index, route="/")
app.add_page(ropa_page, route="/ropa", on_load=lambda: ProductState.set_filter("Todo"))
app.add_page(sets_page, route="/sets", on_load=lambda: ProductState.set_filter("Todo"))
app.add_page(
    accesorios_page,
    route="/accesorios",
    on_load=lambda: ProductState.set_filter("Todo"),
)
app.add_page(login_page, route="/login")
app.add_page(admin_dashboard, route="/admin", on_load=AuthState.check_auth)