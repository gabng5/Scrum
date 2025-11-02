from flask_login import login_user, logout_user
from app.entity.user_account import UserAccount

class AuthController:
    def login(self, email, password):
        user = UserAccount.query.filter_by(email=email).first()
        if not user or not user.isActive: return None, "Account not found or suspended."
        if not user.check_password(password): return None, "Invalid credentials."
        login_user(user)
        role = (user.profile.profileName if user.profile else "").lower()
        if role == "useradmin": return "/admin/dashboard", None
        if role in ("csrrep","csr","csr representative"): return "/csr/dashboard", None
        if role in ("pin","personinneed","person-in-need"): return "/pin/dashboard", None
        if role in ("platformmanager","platform"): return "/pm/dashboard", None
        return "/", None
    def logout(self):
        logout_user(); return True
