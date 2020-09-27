from django.contrib import admin
from .models import Philosopher, Idea, School, Book

classes = [Idea, School]

class PhilosopherAdmin(admin.ModelAdmin):
	search_fields = ('title',)
	list_per_page = 20

class BookAdmin(admin.ModelAdmin):
	search_fields = ('name',)
	list_per_page = 20

admin.site.register(Philosopher, PhilosopherAdmin)
admin.site.register(Book, BookAdmin)

for c in classes:
	admin.site.register(c)