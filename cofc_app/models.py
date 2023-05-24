from django.conf import settings
from django.db import models

class CharacterInput(models.Model):
    age = models.PositiveIntegerField(verbose_name='年齢',blank=False)
    gender = models.CharField(verbose_name="性別",max_length=20,choices=(("男","男"),("女","女")))
    job = models.CharField(verbose_name="職業",max_length=30,blank = False)
    others = models.TextField(verbose_name="その他の特徴",blank=True)
    def __str__(self):
	    return self.job