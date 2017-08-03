# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post
# Register your models here.

# class PostInline(admin.StackedInline):
# 	model = Post
# 	extra = 0
# 	fk_name = 'author'


class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author','published_date']
	list_display_links = ['id', 'title']
	#exclude = ["text"]
	#fields = ['author','title', 'text', 'post_image',] 
	#inlines = [PostInline]
	# list_fiter = ['post_date']
	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)