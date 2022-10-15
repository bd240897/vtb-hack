from django import forms
from django.contrib import admin
from .models import *


class ChoiceAdminForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = "__all__"
        widgets = {
            'name': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    form = ChoiceAdminForm
    list_display = ("pk", "name", )
    list_display_links = ("pk", "name",)

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "description", )
    list_display_links = ("pk", "name",)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("pk", "poll", "timestamp",)
    list_display_links = ("pk", "poll",)
    readonly_fields = ("timestamp",)