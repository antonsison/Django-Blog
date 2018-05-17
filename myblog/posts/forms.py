from django import forms

from .models import Post
from .models import Tag

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"image",
			"tags",
			"draft",
			"publish",
		]