import reflex as rx
from app.states.admin_state import AdminState
from app.states.auth_state import AuthState


def sidebar_item(label: str, icon_name: str, section_id: str) -> rx.Component:
    is_active = AdminState.active_section == section_id
    return rx.el.button(
        rx.icon(
            icon_name,
            class_name=rx.cond(
                is_active,
                "h-5 w-5 text-white",
                "h-5 w-5 text-gray-400 group-hover:text-white",
            ),
        ),
        rx.el.span(label),
        on_click=lambda: AdminState.set_section(section_id),
        class_name=rx.cond(
            is_active,
            "flex items-center gap-3 w-full px-4 py-3 bg-[#E91E8C] text-white text-sm font-bold tracking-wide rounded-lg transition-all shadow-md",
            "flex items-center gap-3 w-full px-4 py-3 text-gray-400 hover:bg-gray-800 hover:text-white text-sm font-medium transition-all rounded-lg group",
        ),
    )


def admin_sidebar() -> rx.Component:
    user_role = AuthState.current_user["role"]
    return rx.el.aside(
        rx.el.div(
            rx.el.h1(
                "BY MAPA",
                class_name="text-xl font-black tracking-tighter text-white mb-1",
            ),
            rx.el.p(
                "ADMIN CONSOLE",
                class_name="text-[10px] font-bold tracking-[0.3em] text-[#E91E8C]",
            ),
            class_name="px-6 py-8 border-b border-gray-800",
        ),
        rx.el.nav(
            rx.el.div(
                rx.el.p(
                    "MENU",
                    class_name="text-[10px] font-black text-gray-500 tracking-widest mb-4 px-4",
                ),
                sidebar_item("Dashboard", "layout-dashboard", "dashboard"),
                sidebar_item("Productos", "shopping-bag", "products"),
                sidebar_item("Pedidos", "package", "orders"),
                sidebar_item("Usuarios", "users", "users"),
                sidebar_item("Contenido", "file-text", "content"),
                sidebar_item("Configuración", "settings", "settings"),
                class_name="flex flex-col gap-2",
            ),
            class_name="p-4 flex-1 overflow-y-auto",
        ),
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed={AuthState.current_user['name']}",
                    class_name="h-10 w-10 rounded-full bg-gray-700",
                ),
                rx.el.div(
                    rx.el.p(
                        AuthState.current_user["name"],
                        class_name="text-sm font-bold text-white leading-none mb-1",
                    ),
                    rx.el.p(
                        AuthState.current_user["role"],
                        class_name="text-[10px] font-medium text-gray-400 uppercase",
                    ),
                    class_name="flex flex-col",
                ),
                class_name="flex items-center gap-3",
            ),
            rx.el.button(
                rx.icon(
                    "log-out",
                    class_name="h-5 w-5 text-gray-400 hover:text-red-500 transition-colors",
                ),
                on_click=AuthState.logout,
            ),
            class_name="p-6 border-t border-gray-800 flex items-center justify-between",
        ),
        class_name="w-64 bg-[#111111] h-screen flex flex-col flex-shrink-0",
    )


def content_input(label: str, key: str, type: str = "text") -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name="text-[10px] font-black text-gray-400 uppercase tracking-widest mb-2 block",
        ),
        rx.el.input(
            on_change=lambda v: AdminState.update_content_field(key, v),
            class_name="w-full p-3 bg-white border border-gray-100 rounded-xl text-sm focus:outline-none focus:border-black transition-all",
            default_value=AdminState.content_data[key],
        ),
        class_name="mb-6",
    )


def settings_input(label: str, key: str, placeholder: str = "") -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="text-xs font-bold text-gray-600 mb-2 block"),
        rx.el.input(
            placeholder=placeholder,
            on_change=lambda v: AdminState.update_settings_field(key, v),
            class_name="w-full p-3 bg-gray-50 border border-gray-200 rounded-xl text-sm focus:bg-white focus:border-black transition-all",
            default_value=AdminState.settings_data[key].to_string(),
        ),
        class_name="mb-4",
    )


def content_management_view() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "GESTIÓN DE CONTENIDO",
            class_name="text-3xl font-black tracking-tighter mb-8",
        ),
        rx.el.div(
            rx.foreach(
                [
                    ("announcement", "Barra Anuncio"),
                    ("hero", "Hero Section"),
                    ("categories", "Categorías"),
                    ("newsletter", "Newsletter"),
                ],
                lambda tab: rx.el.button(
                    tab[1],
                    on_click=lambda: AdminState.set_content_tab(tab[0]),
                    class_name=rx.cond(
                        AdminState.content_tab == tab[0],
                        "px-8 py-3 bg-black text-white text-[10px] font-black uppercase tracking-widest rounded-full shadow-lg transition-all",
                        "px-8 py-3 bg-white text-gray-400 text-[10px] font-black uppercase tracking-widest hover:text-black transition-all",
                    ),
                ),
            ),
            class_name="flex gap-4 mb-12 border-b border-gray-100 pb-6",
        ),
        rx.match(
            AdminState.content_tab,
            (
                "announcement",
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            content_input("Texto de Anuncio", "announcement_text"),
                            rx.el.div(
                                rx.el.span(
                                    "Mostrar Barra de Anuncio",
                                    class_name="text-sm font-bold",
                                ),
                                rx.el.button(
                                    rx.el.div(
                                        class_name=rx.cond(
                                            AdminState.content_data[
                                                "announcement_active"
                                            ],
                                            "h-4 w-4 bg-white rounded-full translate-x-6 transition-all",
                                            "h-4 w-4 bg-white rounded-full translate-x-0 transition-all",
                                        )
                                    ),
                                    on_click=AdminState.toggle_announcement,
                                    class_name=rx.cond(
                                        AdminState.content_data["announcement_active"],
                                        "w-12 h-6 bg-green-500 rounded-full p-1",
                                        "w-12 h-6 bg-gray-300 rounded-full p-1",
                                    ),
                                ),
                                class_name="flex items-center justify-between p-6 bg-gray-50 rounded-2xl mb-8",
                            ),
                            rx.el.button(
                                "GUARDAR CAMBIOS",
                                on_click=AdminState.save_content,
                                class_name="w-full py-4 bg-black text-white font-black text-xs tracking-widest rounded-xl hover:bg-[#E91E8C] transition-all",
                            ),
                            class_name="w-full md:w-1/2",
                        ),
                        rx.el.div(
                            rx.el.p(
                                "PREVIEW",
                                class_name="text-[10px] font-black text-gray-400 mb-4",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.p(
                                        AdminState.content_data["announcement_text"],
                                        class_name="text-[10px] text-white tracking-widest uppercase",
                                    ),
                                    class_name=rx.cond(
                                        AdminState.content_data["announcement_active"],
                                        "w-full bg-black py-2 flex items-center justify-center",
                                        "hidden",
                                    ),
                                ),
                                class_name="w-full h-32 bg-white border border-dashed border-gray-300 rounded-2xl flex flex-col items-center justify-center p-4",
                            ),
                            class_name="w-full md:w-1/2",
                        ),
                        class_name="flex flex-col md:flex-row gap-12",
                    )
                ),
            ),
            (
                "hero",
                rx.el.div(
                    rx.el.div(
                        content_input("Línea 1", "hero_line1"),
                        content_input("Línea 2", "hero_line2"),
                        content_input("Línea 3", "hero_line3"),
                        content_input("Subtítulo", "hero_subtitle"),
                        content_input("Botón CTA", "hero_cta"),
                        content_input("Color de Fondo", "hero_bg_color"),
                        rx.el.button(
                            "ACTUALIZAR HERO",
                            on_click=AdminState.save_content,
                            class_name="w-full py-4 bg-black text-white font-black text-xs tracking-widest rounded-xl",
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-2 gap-x-8",
                    )
                ),
            ),
            (
                "categories",
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.h3(
                                "PÁGINA ROPA", class_name="font-black text-sm mb-4"
                            ),
                            content_input("Título", "cat_ropa_title"),
                            content_input("Subtítulo", "cat_ropa_subtitle"),
                            class_name="p-6 bg-white border border-gray-100 rounded-2xl",
                        ),
                        rx.el.div(
                            rx.el.h3(
                                "PÁGINA SETS", class_name="font-black text-sm mb-4"
                            ),
                            content_input("Título", "cat_sets_title"),
                            content_input("Subtítulo", "cat_sets_subtitle"),
                            class_name="p-6 bg-white border border-gray-100 rounded-2xl",
                        ),
                        rx.el.div(
                            rx.el.h3(
                                "PÁGINA ACCESORIOS",
                                class_name="font-black text-sm mb-4",
                            ),
                            content_input("Título", "cat_acc_title"),
                            content_input("Subtítulo", "cat_acc_subtitle"),
                            class_name="p-6 bg-white border border-gray-100 rounded-2xl",
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-3 gap-6",
                    ),
                    rx.el.button(
                        "GUARDAR TODO",
                        on_click=AdminState.save_content,
                        class_name="mt-8 px-12 py-4 bg-black text-white font-black text-xs tracking-widest rounded-xl",
                    ),
                ),
            ),
            (
                "newsletter",
                rx.el.div(
                    rx.el.div(
                        content_input("Encabezado", "newsletter_head"),
                        content_input("Descripción", "newsletter_desc"),
                        content_input("Texto Botón", "newsletter_btn"),
                        rx.el.div(
                            rx.el.p(
                                "SUSCRIPTORES ACTUALES",
                                class_name="text-[10px] font-black text-gray-400 mb-1",
                            ),
                            rx.el.p(
                                "1,248", class_name="text-3xl font-black text-[#E91E8C]"
                            ),
                            class_name="mt-4 p-6 bg-pink-50 rounded-2xl",
                        ),
                        class_name="max-w-xl",
                    ),
                    rx.el.button(
                        "GUARDAR",
                        on_click=AdminState.save_content,
                        class_name="mt-8 px-12 py-4 bg-black text-white font-black text-xs tracking-widest rounded-xl",
                    ),
                ),
            ),
            rx.el.div("Selecciona una sección para editar"),
        ),
        class_name="animate-in fade-in slide-in-from-bottom-4 duration-700",
    )


def settings_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "CONFIGURACIÓN", class_name="text-3xl font-black tracking-tighter"
            ),
            rx.el.div(
                rx.el.button(
                    "RESTAURAR",
                    on_click=AdminState.reset_settings,
                    class_name="px-6 py-2 text-xs font-bold text-gray-400 hover:text-black",
                ),
                rx.el.button(
                    "GUARDAR CAMBIOS",
                    on_click=AdminState.save_settings,
                    class_name="px-8 py-3 bg-black text-white text-[10px] font-black rounded-xl hover:bg-[#E91E8C] transition-all",
                ),
                class_name="flex gap-4",
            ),
            class_name="flex justify-between items-center mb-12",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "INFORMACIÓN DE LA TIENDA", class_name="text-sm font-black mb-6"
                ),
                settings_input("Nombre de la Tienda", "name"),
                settings_input("Tagline", "tagline"),
                settings_input("Email de Contacto", "email"),
                rx.el.div(
                    settings_input("Instagram URL", "instagram"),
                    settings_input("TikTok URL", "tiktok"),
                    class_name="grid grid-cols-2 gap-4",
                ),
                class_name="p-8 bg-white rounded-3xl border border-gray-100 shadow-sm",
            ),
            rx.el.div(
                rx.el.h3("MATRIZ DE PERMISOS", class_name="text-sm font-black mb-6"),
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    "Rol",
                                    class_name="text-left p-4 text-[10px] text-gray-400",
                                ),
                                rx.el.th(
                                    "Prod.", class_name="p-4 text-[10px] text-gray-400"
                                ),
                                rx.el.th(
                                    "Ord.", class_name="p-4 text-[10px] text-gray-400"
                                ),
                                rx.el.th(
                                    "Users", class_name="p-4 text-[10px] text-gray-400"
                                ),
                                rx.el.th(
                                    "Cont.", class_name="p-4 text-[10px] text-gray-400"
                                ),
                            )
                        ),
                        rx.el.tbody(
                            rx.el.tr(
                                rx.el.td(
                                    "Super Admin", class_name="p-4 text-xs font-bold"
                                ),
                                rx.el.td(
                                    rx.icon(
                                        "check",
                                        class_name="mx-auto h-4 w-4 text-green-500",
                                    ),
                                    class_name="p-4",
                                ),
                                rx.el.td(
                                    rx.icon(
                                        "check",
                                        class_name="mx-auto h-4 w-4 text-green-500",
                                    ),
                                    class_name="p-4",
                                ),
                                rx.el.td(
                                    rx.icon(
                                        "check",
                                        class_name="mx-auto h-4 w-4 text-green-500",
                                    ),
                                    class_name="p-4",
                                ),
                                rx.el.td(
                                    rx.icon(
                                        "check",
                                        class_name="mx-auto h-4 w-4 text-green-500",
                                    ),
                                    class_name="p-4",
                                ),
                            ),
                            rx.el.tr(
                                rx.el.td("Editor", class_name="p-4 text-xs font-bold"),
                                rx.el.td(
                                    rx.icon(
                                        "check",
                                        class_name="mx-auto h-4 w-4 text-green-500",
                                    ),
                                    class_name="p-4",
                                ),
                                rx.el.td(
                                    rx.icon(
                                        "x", class_name="mx-auto h-4 w-4 text-red-300"
                                    ),
                                    class_name="p-4",
                                ),
                                rx.el.td(
                                    rx.icon(
                                        "x", class_name="mx-auto h-4 w-4 text-red-300"
                                    ),
                                    class_name="p-4",
                                ),
                                rx.el.td(
                                    rx.icon(
                                        "check",
                                        class_name="mx-auto h-4 w-4 text-green-500",
                                    ),
                                    class_name="p-4",
                                ),
                            ),
                            rx.el.tr(
                                rx.el.td("Viewer", class_name="p-4 text-xs font-bold"),
                                rx.el.td(
                                    rx.icon(
                                        "x", class_name="mx-auto h-4 w-4 text-red-300"
                                    ),
                                    class_name="p-4",
                                ),
                                rx.el.td(
                                    rx.icon(
                                        "check",
                                        class_name="mx-auto h-4 w-4 text-green-500",
                                    ),
                                    class_name="p-4",
                                ),
                                rx.el.td(
                                    rx.icon(
                                        "x", class_name="mx-auto h-4 w-4 text-red-300"
                                    ),
                                    class_name="p-4",
                                ),
                                rx.el.td(
                                    rx.icon(
                                        "x", class_name="mx-auto h-4 w-4 text-red-300"
                                    ),
                                    class_name="p-4",
                                ),
                            ),
                        ),
                        class_name="w-full text-center border-t border-gray-50",
                    ),
                    class_name="overflow-hidden rounded-2xl border border-gray-100",
                ),
                class_name="p-8 bg-white rounded-3xl border border-gray-100 shadow-sm",
            ),
            rx.el.div(
                rx.el.h3("ENVÍOS", class_name="text-sm font-black mb-6"),
                settings_input("Umbral Envío Gratis ($)", "free_shipping_threshold"),
                settings_input("Costo Estándar ($)", "standard_shipping"),
                settings_input("Costo Express ($)", "express_shipping"),
                class_name="p-8 bg-white rounded-3xl border border-gray-100 shadow-sm",
            ),
            rx.el.div(
                rx.el.h3("NOTIFICACIONES", class_name="text-sm font-black mb-6"),
                rx.el.div(
                    rx.el.p("Nuevos Pedidos", class_name="text-xs font-bold"),
                    rx.el.button(
                        rx.el.div(
                            class_name=rx.cond(
                                AdminState.settings_data["notify_orders"],
                                "h-4 w-4 bg-white rounded-full translate-x-4 transition-all",
                                "h-4 w-4 bg-white rounded-full translate-x-0 transition-all",
                            )
                        ),
                        on_click=lambda: AdminState.toggle_setting("notify_orders"),
                        class_name=rx.cond(
                            AdminState.settings_data["notify_orders"],
                            "w-10 h-6 bg-green-500 rounded-full p-1",
                            "w-10 h-6 bg-gray-300 rounded-full p-1",
                        ),
                    ),
                    class_name="flex justify-between items-center mb-4",
                ),
                rx.el.div(
                    rx.el.p("Alerta Stock Bajo", class_name="text-xs font-bold"),
                    rx.el.button(
                        rx.el.div(
                            class_name=rx.cond(
                                AdminState.settings_data["notify_low_stock"],
                                "h-4 w-4 bg-white rounded-full translate-x-4 transition-all",
                                "h-4 w-4 bg-white rounded-full translate-x-0 transition-all",
                            )
                        ),
                        on_click=lambda: AdminState.toggle_setting("notify_low_stock"),
                        class_name=rx.cond(
                            AdminState.settings_data["notify_low_stock"],
                            "w-10 h-6 bg-green-500 rounded-full p-1",
                            "w-10 h-6 bg-gray-300 rounded-full p-1",
                        ),
                    ),
                    class_name="flex justify-between items-center",
                ),
                class_name="p-8 bg-white rounded-3xl border border-gray-100 shadow-sm",
            ),
            rx.el.div(
                rx.el.h3("APARIENCIA", class_name="text-sm font-black mb-6"),
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "Color Primario",
                            class_name="text-[10px] font-bold text-gray-400",
                        ),
                        rx.el.div(
                            rx.el.input(
                                type="color",
                                on_change=lambda v: AdminState.update_settings_field(
                                    "primary_color", v
                                ),
                                class_name="h-10 w-10 border-none cursor-pointer",
                                default_value=AdminState.settings_data["primary_color"],
                            ),
                            rx.el.p(
                                AdminState.settings_data["primary_color"],
                                class_name="text-xs font-mono font-bold",
                            ),
                            class_name="flex items-center gap-4 mt-2",
                        ),
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Tipografía",
                            class_name="text-[10px] font-bold text-gray-400",
                        ),
                        rx.el.select(
                            rx.el.option("Inter", value="Inter"),
                            rx.el.option("Roboto", value="Roboto"),
                            rx.el.option("Montserrat", value="Montserrat"),
                            value=AdminState.settings_data["font_family"],
                            on_change=lambda v: AdminState.update_settings_field(
                                "font_family", v
                            ),
                            class_name="w-full p-2 bg-gray-50 rounded-lg text-xs mt-2 appearance-none font-bold",
                        ),
                    ),
                    class_name="space-y-6",
                ),
                class_name="p-8 bg-white rounded-3xl border border-gray-100 shadow-sm",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
        ),
        class_name="animate-in fade-in slide-in-from-bottom-4 duration-700",
    )


def dashboard_view() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "RESUMEN GENERAL", class_name="text-xl font-black tracking-tighter mb-8"
        ),
        rx.el.div(
            stat_card(
                "Pedidos",
                AdminState.total_orders_count.to_string(),
                "+12%",
                "shopping-cart",
                "text-blue-500",
            ),
            stat_card(
                "Ingresos",
                AdminState.total_revenue,
                "+8%",
                "dollar-sign",
                "text-green-500",
            ),
            stat_card(
                "Usuarios",
                AdminState.active_users_count.to_string(),
                "+1",
                "users",
                "text-purple-500",
            ),
            stat_card(
                "Productos",
                AdminState.total_products_count.to_string(),
                "0",
                "package",
                "text-pink-500",
            ),
            class_name="grid grid-cols-1 md:grid-cols-4 gap-6 mb-12",
        ),
        rx.el.div(
            rx.el.h3(
                "ACTIVIDAD RECIENTE",
                class_name="text-sm font-black tracking-widest uppercase mb-6",
            ),
            rx.el.div(
                rx.el.p(
                    "No hay pedidos registrados aún.",
                    class_name="text-gray-400 text-sm italic",
                ),
                class_name="bg-white p-12 rounded-3xl border border-gray-100 text-center shadow-sm",
            ),
        ),
    )


def stat_card(
    title: str, value: str, trend: str, icon: str, color: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, class_name=f"h-6 w-6 {color}"),
                class_name="h-12 w-12 rounded-xl bg-gray-50 flex items-center justify-center",
            ),
            rx.el.span(
                trend,
                class_name="text-xs font-bold text-green-600 bg-green-50 px-2 py-1 rounded-full",
            ),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.el.h3(value, class_name="text-2xl font-black mb-1"),
        rx.el.p(title, class_name="text-xs font-bold text-gray-500 uppercase"),
        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm",
    )


def placeholder_view(title: str, message: str) -> rx.Component:
    return rx.el.div(
        rx.icon("construction", class_name="h-12 w-12 text-gray-200 mb-4"),
        rx.el.h2(title, class_name="text-xl font-black mb-2"),
        rx.el.p(message, class_name="text-gray-400 text-sm font-medium"),
        class_name="flex flex-col items-center justify-center h-[60vh] text-center",
    )


def users_view() -> rx.Component:
    return placeholder_view("Usuarios", "Gestión de personal administrativo.")


def products_view() -> rx.Component:
    return placeholder_view("Productos", "Gestión del catálogo editorial.")


def orders_management_view() -> rx.Component:
    return placeholder_view("Pedidos", "Seguimiento de ventas y envíos.")