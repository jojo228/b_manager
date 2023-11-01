from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, contact, password, **extra_fields):
        if not contact:
            raise ValueError("The contact must be set")
        user = self.model(contact=contact, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, contact, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        # extra_fields.setdefault('user_type', user_constants.SUPERUSER)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(contact, password, **extra_fields)
