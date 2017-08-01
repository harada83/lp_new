# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post
# Register your models here.

# class PostInline(admin.StackedInline):
# 	model = Post
# 	extra = 2
# 	fk_name = 'author'


class PostAdmin(admin.ModelAdmin):
	fields = ['author','title', 'text', 'post_image',] 
	# inlines = [PostInline,]
	# list_fiter = ['post_date']

admin.site.register(Post, PostAdmin)