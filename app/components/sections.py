import reflex as rx
from app.states.product_state import ProductState, Product


def product_card(product: Product) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=product["image"],
                class_name="w-full aspect-[3/4] object-cover transition-transform duration-700 group-hover:scale-105",
            ),
            rx.cond(
                product["pieces"],
                rx.el.span(
                    product["pieces"],
                    class_name="absolute top-4 left-4 bg-black text-white text-[8px] font-black tracking-widest px-2 py-1 z-10",
                ),
            ),
            rx.el.div(
                rx.el.a(
                    rx.el.button(
                        "Ver el look",
                        class_name="px-6 py-3 bg-white text-black text-[10px] uppercase tracking-widest font-bold opacity-0 group-hover:opacity-100 transition-opacity duration-300",
                    ),
                    href=f"/producto/{product['id']}",
                ),
                class_name="absolute inset-0 flex items-center justify-center bg-black/10 opacity-0 group-hover:opacity-100 transition-all duration-300",
            ),
            class_name="relative overflow-hidden",
        ),
        rx.el.div(
            rx.el.h3(
                product["name"],
                class_name="text-sm font-semibold uppercase tracking-tight text-gray-900",
            ),
            rx.el.p(product["price"], class_name="text-sm text-gray-500 font-medium"),
            class_name="mt-4 flex justify-between items-start",
        ),
        class_name="group cursor-pointer",
    )


def the_drop_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "EL DROP",
                    class_name="text-[12vw] font-black leading-none tracking-tighter text-black opacity-5 absolute -top-12 -left-4 select-none",
                ),
                rx.el.h2(
                    "JUST LANDED",
                    class_name="text-5xl md:text-7xl font-black tracking-tighter text-black relative z-10",
                ),
                rx.el.p(
                    "Piezas que no esperan. / Solo para quienes actúan.",
                    class_name="text-lg md:text-xl text-gray-600 mt-4 font-medium italic",
                ),
                class_name="mb-16 relative",
            ),
            rx.el.div(
                rx.foreach(ProductState.products, product_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
            class_name="max-w-[1440px] mx-auto px-6 py-24",
        ),
        id="new-in",
        class_name="w-full bg-white overflow-hidden",
    )


def marquee_break() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "COLOR • ACTITUD • ENERGÍA • AUDAZ • ",
                    class_name="text-4xl md:text-6xl font-black text-white px-4",
                ),
                rx.el.span(
                    "COLOR • ACTITUD • ENERGÍA • AUDAZ • ",
                    class_name="text-4xl md:text-6xl font-black text-white px-4",
                ),
                rx.el.span(
                    "COLOR • ACTITUD • ENERGÍA • AUDAZ • ",
                    class_name="text-4xl md:text-6xl font-black text-white px-4",
                ),
                class_name="whitespace-nowrap animate-marquee flex items-center h-full",
            ),
            class_name="w-full h-32 md:h-48 bg-[#E91E8C] flex items-center overflow-hidden",
        ),
        class_name="w-full",
    )


def trend_edit_card(
    title: str, subtitle: str, cta: str, bg_color: str, image_src: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name=f"absolute inset-0 {bg_color} opacity-20 group-hover:opacity-40 transition-opacity duration-700"
        ),
        rx.image(
            src=image_src,
            class_name="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-1000",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    title,
                    class_name="text-4xl md:text-6xl font-black text-white mb-2 tracking-tighter",
                ),
                rx.el.p(
                    subtitle,
                    class_name="text-white/90 text-sm md:text-lg mb-6 max-w-xs font-medium",
                ),
                rx.el.button(
                    cta,
                    class_name="px-8 py-3 bg-white text-black text-xs font-bold uppercase tracking-widest hover:bg-black hover:text-white transition-all duration-300",
                ),
                class_name="relative z-10",
            ),
            class_name="absolute inset-0 p-8 md:p-12 flex flex-col justify-end bg-gradient-to-t from-black/80 via-black/20 to-transparent",
        ),
        class_name="relative aspect-square md:aspect-video overflow-hidden group cursor-pointer",
    )


def trend_edit_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "TREND EDIT",
                class_name="text-2xl font-black tracking-widest mb-12 text-center",
            ),
            rx.el.div(
                trend_edit_card(
                    "ELECTRIC NIGHTS",
                    "Para las noches que se convierten en historias.",
                    "Explorar",
                    "bg-purple-900",
                    "/fashion_photography_high.png",
                ),
                trend_edit_card(
                    "GOLDEN HOUR",
                    "Cuando la luz te favorece, todo lo demás también.",
                    "Descubrir",
                    "bg-orange-500",
                    "/fashion_editorial_photography.png",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-4",
            ),
            class_name="max-w-[1440px] mx-auto px-6 py-24",
        ),
        id="ropa",
        class_name="w-full bg-[#f8f8f8]",
    )


def newsletter_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "SUSCRÍBETE AL INNER CIRCLE",
                    class_name="text-3xl md:text-4xl font-black tracking-tighter mb-4",
                ),
                rx.el.p(
                    "Drops exclusivos. First access. Sin spam, solo estilo.",
                    class_name="text-gray-600 mb-10 font-medium",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.input(
                            placeholder="TU EMAIL AQUÍ",
                            name="email",
                            type="email",
                            required=True,
                            class_name="flex-1 bg-transparent border-b-2 border-black py-4 px-2 focus:outline-none focus:border-[#E91E8C] transition-colors uppercase text-sm font-bold tracking-widest",
                        ),
                        rx.el.button(
                            "Unirme",
                            type="submit",
                            class_name="px-10 py-4 bg-black text-white font-bold uppercase text-xs tracking-[0.3em] hover:bg-[#E91E8C] transition-all",
                        ),
                        class_name="flex flex-col md:flex-row gap-6 w-full max-w-2xl mx-auto",
                    ),
                    on_submit=ProductState.handle_newsletter_submit,
                ),
                class_name="text-center",
            ),
            class_name="max-w-[1440px] mx-auto px-6 py-32 border-t border-gray-100",
        ),
        class_name="w-full bg-white",
    )