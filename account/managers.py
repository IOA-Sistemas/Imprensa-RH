from django.contrib.auth.base_user import BaseUserManager

class UsersManager(BaseUserManager):
    
    def _create_user(self, cpf, email, password, **extra_fields):
        if not cpf:
            raise ValueError('The given cpf is not valid')
        cpf = self.model.normalize_username(cpf)
        user = self.model(cpf=cpf, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, cpf, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        # extra_fields.setdefault('is_default', False)
        return self._create_user(cpf, email, password, **extra_fields)
    
    def create_superuser(self, cpf, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_default', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(cpf, email, password, **extra_fields),
    