from django import forms
from .models import Post

class CustomPost(Post):
    title = forms.CharField(max_length=75, required=True)
    body = forms.CharField(required=True)
    slug = forms.SlugField(max_length=50, required=True)
    date = forms.DateTimeField(required=True)
    banner = forms.ImageField(required=False)
    
    class Meta:
        model = Post
        fields = ('title','body','slug','date','banner')
        
    def save(self, commit=True):
        post = super().save(commit=False)
        post.title = self.cleaned_data["title"]
        post.body = self.cleaned_data["body"]
        post.slug = self.cleaned_data["slug"]
        post.date = self.cleaned_data["date"]
        post.banner = self.cleaned_data["banner"]
        if commit:
            post.save()
        return post