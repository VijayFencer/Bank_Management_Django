from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer,Branch,Transaction
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'Customer_name', 'gender', 'balance', 'branch_name', 'phone_number', 'email_customer')
    search_fields = ('Customer_name', 'phone_number', 'email_customer')
    list_filter = ('gender', 'branch_name')
    ordering = ('Customer_name',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'sender', 'receiver', 'amount', 'date')
    search_fields = ('sender__Customer_name', 'receiver__Customer_name')
    list_filter = ('date',)
    ordering = ('-date',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Branch) 
admin.site.register(Transaction, TransactionAdmin)