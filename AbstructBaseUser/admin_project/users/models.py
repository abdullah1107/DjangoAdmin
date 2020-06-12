from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class MyAccountManager(BaseUserManager):
	def _create_user(self, email,password,**extra_fields):
		if not email:
			raise ValueError('User Must have an email Address')
		user = self.model(
			   email = self.normalize_email(email),
			   **extra_fields,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)
	
	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)
		#extra_fields.setdefault('is_staff', True)
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
	username      = None
	email         = models.EmailField(verbose_name = "email", max_length = 35, unique =True)
	name          = models.CharField(max_length = 12, null=True, unique=False)
	mobile_number = models.CharField(max_length= 15, unique=True, null=False)
	is_active     = models.BooleanField(default=True)
	is_staff      = models.BooleanField(default= True)
	is_superadmin  = models.BooleanField(default=False)

	REQUIRED_FIELDS = ['mobile_number']
	USERNAME_FIELD  = 'email'

	objects = MyAccountManager()

	def __str__(self):
		return self.email
	
	# def has_module_perms(self,app_label):
	# 	return True

	# def has_perm(self, perm, obj = None):
	# 	return self.is_admin

		
	# def create_superuser(self, email, password,**extra_fields):
	# 	user = self._create_user(email=email, password=password,  **extra_fields)
	# 	user.is_admin     = True
	# 	user.is_staff     = True
	# 	user.is_superuser = True
	# 	user.save(using=self._db)
	# 	return user	
