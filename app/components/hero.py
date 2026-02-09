import reflex as rx
from app.states.navigation_state import NavigationState


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(class_name="absolute inset-0 bg-[#f8f8f8]"),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Color.",
                    rx.el.br(),
                    "Actitud.",
                    rx.el.br(),
                    "Tú.",
                    class_name="text-[12vw] md:text-[8vw] font-black leading-[0.85] tracking-tighter text-black",
                ),
                rx.el.p(
                    "La moda que no pide permiso.",
                    class_name="text-xl md:text-2xl font-medium mt-8 text-gray-800 italic",
                ),
                rx.el.div(
                    rx.el.button(
                        "Ver el drop",
                        on_click=NavigationState.increment_cart,
                        class_name="mt-12 px-12 py-5 bg-black text-white text-xs uppercase tracking-[0.3em] font-bold hover:bg-[#E91E8C] hover:scale-105 transition-all duration-500 rounded-none",
                    ),
                    class_name="flex",
                ),
                class_name="relative z-10 flex flex-col justify-center h-full max-w-[1440px] mx-auto px-6",
            ),
            class_name="h-full w-full",
        ),
        rx.el.div(
            rx.el.span(
                "COLLECTION NO. 01 / VERANO 24",
                class_name="text-[10px] tracking-[0.5em] uppercase vertical-text font-bold",
            ),
            class_name="absolute right-10 bottom-24 hidden lg:block rotate-90 origin-right",
        ),
        rx.el.div(
            rx.el.div(class_name="w-[1px] h-16 bg-black animate-bounce"),
            class_name="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-4",
        ),
        class_name="h-[calc(100vh-112px)] w-full relative overflow-hidden flex items-center",
    )