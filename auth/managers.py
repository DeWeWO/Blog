from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, discipline, user_group, password, **extra_fields):
        if not email:
            raise ValueError("Email kiritilishi kerak!")
        if not username:
            raise ValueError("Foydalanuvchi nomi kiritilishi kerak!")
        if not first_name:
            raise ValueError("Ism kiritilishi kerak!")
        if not last_name:
            raise ValueError("Familiya kiritilishi kerak!")
        if not discipline:
            raise ValueError("Yo'nalish kiritilishi kerak!")
        if not user_group:
            raise ValueError("Guruh kiritilishi kerak!")
        
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            discipline=discipline,
            user_group=user_group,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, first_name, last_name, discipline, user_group, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            discipline=discipline,
            user_group=user_group,
            password=password,
            **extra_fields
        )