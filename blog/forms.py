from django import forms
from .models import Comment,Post 


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class NewPost(forms.ModelForm):
    title = forms.CharField(label=' العنوان', max_length=100)
    content= forms.CharField(label ='التدوينة' ,widget=forms.Textarea(attrs={'row':'10','size': '40'}))
    class Meta:
        model = Post 
        fields = ('title', 'content','image')
        
        
class UpdateForm(forms.ModelForm):
    title = forms.CharField(label=' العنوان', max_length=100)
    content= forms.CharField(label ='التدوينة' ,widget=forms.Textarea(attrs={'row':'10','size': '40'}))
    class Meta:
        model = Post
        fields = ('title', 'content',)
      
      
      

