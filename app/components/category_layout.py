import reflex as rx
from app.states.product_state import ProductState, Product
from app.components.sections import product_card
from app.components.navigation import navbar, announcement_bar
from app.components.footer import footer


def category_filter_btn(label: str) -> rx.Component:
    is_active = ProductState.category_filter == label
    return rx.el.button(
        label,
        on_click=lambda: ProductState.set_filter(label),
        class_name=rx.cond(
            is_active,
            "px-6 py-2 bg-black text-white text-[10px] font-black uppercase tracking-widest transition-all",
            "px-6 py-2 bg-white text-gray-400 border border-gray-100 text-[10px] font-black uppercase tracking-widest hover:text-black transition-all",
        ),
    )


def category_header(title: str, subtitle: str, filters: list[str]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                title,
                class_name="text-6xl md:text-8xl font-black tracking-tighter mb-4",
            ),
            rx.el.p(
                subtitle,
                class_name="text-lg md:text-xl text-gray-500 font-medium italic",
            ),
            class_name="mb-16",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Filtrar por:",
                    class_name="text-[10px] font-black tracking-widest text-gray-400 uppercase mr-4 self-center",
                ),
                rx.foreach(filters, category_filter_btn),
                class_name="flex flex-wrap gap-2",
            ),
            class_name="border-y border-gray-100 py-6 mb-12 flex justify-between items-center",
        ),
        class_name="max-w-[1440px] mx-auto px-6 pt-24",
    )


def category_page_layout(
    title: str, subtitle: str, filters: list[str], products_var: rx.Var
) -> rx.Component:
    return rx.el.main(
        announcement_bar(),
        navbar(),
        category_header(title, subtitle, filters),
        rx.el.section(
            rx.el.div(
                rx.cond(
                    products_var.length() > 0,
                    rx.el.div(
                        rx.foreach(products_var, product_card),
                        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-x-8 gap-y-16",
                    ),
                    rx.el.div(
                        rx.icon(
                            "shopping-bag", class_name="h-12 w-12 text-gray-200 mb-4"
                        ),
                        rx.el.p(
                            "No se encontraron productos en esta categoría.",
                            class_name="text-gray-400 font-medium",
                        ),
                        class_name="flex flex-col items-center justify-center py-32 text-center",
                    ),
                ),
                class_name="max-w-[1440px] mx-auto px-6 pb-32",
            )
        ),
        footer(),
        class_name="font-['Inter'] selection:bg-[#E91E8C] selection:text-white",
    )