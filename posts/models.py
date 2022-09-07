from django.db import models  
from django.contrib.auth.models import User
import os
#from markdownx.models import MarkdownxField
#from markdownx.utils import markdown



# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) 
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'  

    def get_absolute_url(self):
        return f'/posts/{self.pk}/'
    '''
        def get_file_ext(self):  
        return self.get_file_name().split('.')[-1]

    def get_file_name(self):  
        return os.path.basename(self.file_upload.name)  

    def get_content_markdown(self):
        return markdown(self.content)

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return 'https://doitdjango.com/avatar/id/379/9ff1a6a6bc11ac6f/svg/{self.author.email}'
    '''





