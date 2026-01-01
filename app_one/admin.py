from django.contrib import admin

from .models import  Class,Parent,Marks,Attendance,Student,CustomUser,Profile,Subject,Teacher,Staff,Fees

# Register your models here.




# Register your models here.
admin.site.register(Staff)
admin.site.register(CustomUser)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Marks)
admin.site.register(Attendance)
admin.site.register(Student)
admin.site.register(Profile)

from django.db.models import Sum
@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'student_class',
        'total_fees',
        'paid_amount',
        'balance_amount',
        'status',
        'payment_date',
    )
    list_filter = ('status', 'student_class')
    search_fields = ('student__name',)

    change_list_template = 'fees_change_list.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            queryset = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        totals = queryset.aggregate(
            total_sum=Sum('total_fees'),
            paid_sum=Sum('paid_amount'),
            balance_sum=Sum('balance_amount')
        )

        response.context_data['totals'] = totals
        return response

