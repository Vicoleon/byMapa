import reflex as rx
from app.states.navigation_state import NavigationState


def announcement_bar() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            "El nuevo drop llegó — Descúbrelo",
            class_name="text-[10px] tracking-[0.2em] uppercase font-medium",
        ),
        class_name="w-full bg-black text-white py-2 flex items-center justify-center sticky top-0 z-[60]",
    )


def nav_item(item: dict[str, str]) -> rx.Component:
    return rx.el.a(
        item["label"],
        href=item["href"],
        on_click=lambda: NavigationState.set_current_section(item["label"]),
        class_name="text-xs uppercase tracking-widest font-semibold hover:text-[#E91E8C] transition-colors duration-300 relative group",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.button(
                rx.icon("menu", class_name="h-5 w-5"),
                on_click=NavigationState.toggle_mobile_menu,
                class_name="md:hidden",
            ),
            rx.el.div(
                rx.foreach(NavigationState.nav_items, nav_item),
                class_name="hidden md:flex items-center gap-8",
            ),
            rx.el.div(
                rx.el.a(
                    "BY MAPA",
                    href="/",
                    class_name="text-2xl font-black tracking-tighter",
                ),
                class_name="absolute left-1/2 -translate-x-1/2",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("search", class_name="h-5 w-5"),
                    class_name="hover:text-[#FF6B35] transition-colors",
                ),
                rx.el.button(
                    rx.el.div(
                        rx.icon("shopping-bag", class_name="h-5 w-5"),
                        rx.cond(
                            NavigationState.cart_count > 0,
                            rx.el.span(
                                NavigationState.cart_count,
                                class_name="absolute -top-1 -right-1 bg-[#E91E8C] text-white text-[8px] h-4 w-4 rounded-full flex items-center justify-center font-bold",
                            ),
                        ),
                        class_name="relative",
                    ),
                    class_name="hover:text-[#E91E8C] transition-colors",
                ),
                rx.el.a(
                    rx.icon("user", class_name="h-5 w-5"),
                    href="/login",
                    class_name="hover:text-black transition-colors",
                ),
                class_name="flex items-center gap-6",
            ),
            class_name="max-w-[1440px] mx-auto px-6 h-20 flex items-center justify-between relative",
        ),
        rx.cond(
            NavigationState.mobile_menu_open,
            rx.el.div(
                rx.el.div(
                    rx.el.button(
                        rx.icon("x", class_name="h-8 w-8"),
                        on_click=NavigationState.toggle_mobile_menu,
                        class_name="absolute top-6 right-6",
                    ),
                    rx.el.div(
                        rx.foreach(
                            NavigationState.nav_items,
                            lambda item: rx.el.a(
                                item["label"],
                                href=item["href"],
                                on_click=NavigationState.toggle_mobile_menu,
                                class_name="text-4xl font-bold uppercase tracking-tighter hover:text-[#E91E8C]",
                            ),
                        ),
                        class_name="flex flex-col gap-8 items-start p-12 mt-20",
                    ),
                    class_name="w-full h-full bg-white animate-in slide-in-from-top duration-300",
                ),
                class_name="fixed inset-0 z-[100] bg-white",
            ),
        ),
        class_name="w-full bg-white/80 backdrop-blur-md border-b border-gray-100 sticky top-[32px] z-50",
    )