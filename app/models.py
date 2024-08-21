from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    oib = models.CharField(max_length=11, null=False, blank=False)
    address = models.CharField(max_length=128, null=False, blank=False)
    city = models.CharField(max_length=64, null=False, blank=False)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=12, null=True, blank=True)
    avatar_url = models.CharField(max_length=128, 
                                  default="https://www.shutterstock.com/image-vector/default-avatar-profile-icon-social-600nw-1677509740.jpg")

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'oib', 'address', 'city']

    def __str__(self):
        return self.email
    
class AnimalType(models.Model):
    CAT = "CAT"
    DOG = "DOG"
    TYPE_CHOICES = [
        (CAT, "Cat"),
        (DOG, "Dog"),

    ]
    lifespan=models.CharField(max_length=128)
    type=models.CharField(max_length=64,choices=TYPE_CHOICES)
    breed=models.CharField(max_length=64)
    def __str__(self) -> str:
        return f"{self.breed}"

class Animal(models.Model):
    name = models.CharField(max_length=128)
    age= models.SmallIntegerField(default=5)
    description = models.CharField(max_length=1024)
    is_adopted = models.BooleanField(default=False)
    type= models.ForeignKey(AnimalType,on_delete=models.CASCADE)
    height=models.CharField(max_length=64)
    weight=models.CharField(max_length=64)
    avatar_url=models.CharField(max_length=128, null=True)
    gender=models.CharField(max_length=12,null=True,blank=True)
    def __str__(self) -> str:
        return f"{self.name}-{self.type.breed}"
    
class AdoptingRequest(models.Model):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (APPROVED, "Approved"),
        (DECLINED, "Declined"),
    ]
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    animal_id=models.ForeignKey(Animal,on_delete=models.CASCADE)
    created_at=	models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    description= models.CharField(max_length=3000,null=True,blank=True)
