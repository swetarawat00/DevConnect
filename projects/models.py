from django.db import models
import uuid
# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=550)
    demo_link=models.CharField(max_length=100,null=True,blank=True)
    source_link=models.CharField(max_length=100,null=True,blank=True)
    tags=models.ManyToManyField('Tag')
    vote_total=models.IntegerField(default=0,null=True,blank=True)
    vote_ratio=models.IntegerField(default=0,null=True,blank=True)

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return(self.title)
    
class Review(models.Model):
    VOTE_TYPE=(
        ('Up Vote','Thumbs Up'),
        ('Down Vote','Thumbs Down')
    )
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    body=models.TextField(max_length=500,null=True,blank=True)
    value=models.CharField(max_length=20,choices=VOTE_TYPE)
    
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return(self.value)

class Tag(models.Model):
    name=models.CharField(max_length=200)

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return(self.name)  