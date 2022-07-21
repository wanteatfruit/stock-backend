from django.contrib import admin

# Register your models here.
from .models import A
from .models import B
from .models import C
 

admin.site.register(A)
admin.site.register(B)
admin.site.register(C)