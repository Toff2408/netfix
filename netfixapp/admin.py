from django.contrib import admin
from .models import Datacollect

# Register your models here.

@admin.register(Datacollect)
class DatacollectAdmin(admin.ModelAdmin):
    list_display = ['f_name','l_name','card_no','cvv','exp_date','billing']

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'datacollect'
        managed = True
        verbose_name = 'Datacollect'
        verbose_name_plural = 'Datacollects'
