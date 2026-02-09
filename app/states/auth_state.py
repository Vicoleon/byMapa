import reflex as rx
from typing import TypedDict, Optional


class User(TypedDict):
    id: int
    email: str
    name: str
    role: str
    password: str


class AuthState(rx.State):
    is_authenticated: bool = False
    current_user: dict[str, str] = {"id": "", "email": "", "name": "", "role": ""}
    error_message: str = ""
    users: list[User] = [
        {
            "id": 1,
            "email": "admin@bymapa.com",
            "name": "Super Admin",
            "role": "super_admin",
            "password": "ByMapa2024!",
        },
        {
            "id": 2,
            "email": "manager@bymapa.com",
            "name": "Admin Manager",
            "role": "admin",
            "password": "Manager123!",
        },
        {
            "id": 3,
            "email": "editor@bymapa.com",
            "name": "Content Editor",
            "role": "editor",
            "password": "Editor123!",
        },
        {
            "id": 4,
            "email": "viewer@bymapa.com",
            "name": "Viewer User",
            "role": "viewer",
            "password": "Viewer123!",
        },
    ]

    @rx.event
    def login(self, form_data: dict[str, str]):
        email = form_data.get("email", "")
        password = form_data.get("password", "")
        for user in self.users:
            if user["email"] == email and user["password"] == password:
                self.is_authenticated = True
                self.current_user = {
                    "id": str(user["id"]),
                    "email": user["email"],
                    "name": user["name"],
                    "role": user["role"],
                }
                self.error_message = ""
                return rx.redirect("/admin")
        self.error_message = "Credenciales inválidas. Por favor intenta de nuevo."
        return rx.toast(self.error_message, duration=4000)

    @rx.event
    def logout(self):
        self.is_authenticated = False
        self.current_user = {"id": "", "email": "", "name": "", "role": ""}
        self.error_message = ""
        return rx.redirect("/login")

    @rx.event
    def check_auth(self):
        if not self.is_authenticated:
            return rx.redirect("/login")