import reflex as rx


def footer_nav_col(title: str, items: list[dict[str, str]]) -> rx.Component:
    return rx.el.div(
        rx.el.h4(
            title, class_name="text-[10px] font-black tracking-[0.3em] uppercase mb-6"
        ),
        rx.el.ul(
            rx.foreach(
                items,
                lambda item: rx.el.li(
                    rx.el.a(
                        item["label"],
                        href=item["href"],
                        class_name="text-xs text-gray-500 hover:text-black transition-colors duration-300",
                    ),
                    class_name="mb-3",
                ),
            ),
            class_name="list-none p-0",
        ),
        class_name="flex flex-col",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        "BY MAPA",
                        href="/",
                        class_name="text-2xl font-black tracking-tighter mb-4 block",
                    ),
                    rx.el.p(
                        "Nacimos del color y la actitud. By Mapa es para quienes no piden permiso.",
                        class_name="text-sm text-gray-600 max-w-xs font-medium italic",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.icon(
                                "instagram",
                                class_name="h-5 w-5 hover:text-[#E91E8C] transition-colors",
                            ),
                            href="#",
                        ),
                        rx.el.a(
                            rx.icon(
                                "music-2",
                                class_name="h-5 w-5 hover:text-[#E91E8C] transition-colors",
                            ),
                            href="#",
                        ),
                        class_name="flex gap-4 mt-8",
                    ),
                    class_name="mb-12 lg:mb-0",
                ),
                footer_nav_col(
                    "Shop",
                    [
                        {"label": "New In", "href": "/#new-in"},
                        {"label": "Ropa", "href": "/#ropa"},
                        {"label": "Sets", "href": "#"},
                        {"label": "Accesorios", "href": "#"},
                    ],
                ),
                footer_nav_col(
                    "Info",
                    [
                        {"label": "Sobre nosotras", "href": "#"},
                        {"label": "Contacto", "href": "#"},
                        {"label": "Drops", "href": "#"},
                    ],
                ),
                footer_nav_col(
                    "Legal",
                    [
                        {"label": "Términos", "href": "#"},
                        {"label": "Privacidad", "href": "#"},
                        {"label": "Envíos", "href": "#"},
                    ],
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12",
            ),
            rx.el.div(
                rx.el.p(
                    f"© {str(rx.State.router.session.client_token)[:0]} 2024 BY MAPA. Todos los derechos reservados.",
                    class_name="text-[10px] tracking-widest text-gray-400",
                ),
                class_name="mt-24 pt-8 border-t border-gray-100",
            ),
            class_name="max-w-[1440px] mx-auto px-6 py-20",
        ),
        class_name="w-full bg-white border-t border-gray-100",
    )