from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	school = models.CharField(max_length=200, blank=True)
	school_proof = models.CharField(max_length=500, blank=True, verbose_name="proof of status")

	#defines the user types
	DEVELOPER = 'DEV'
	ADMINISTRATOR = 'ADM'
	CONTENT = 'CNT'
	TEACHER = 'TCH'
	ACCT_TYPE_CHOICES = (
		(ADMINISTRATOR, 'Admin'),
		(CONTENT, 'Content'),
		(TEACHER, 'Teacher')
	)
	acct_type = models.CharField(max_length=3, choices=ACCT_TYPE_CHOICES, default=TEACHER)
	approved = models.BooleanField(default=False)
	def __unicode__(self):
		return self.user.username

class Chapter(models.Model):
	num = models.IntegerField(unique=True, verbose_name="chapter number")
	name = models.CharField(max_length=512,default="")
	duration = models.CharField(max_length=512,default="",blank=True)
	description = models.TextField(default="",blank=True)
	def __unicode__(self):
		return str(self.num) + ': ' + self.name

class Module(models.Model):
	num = models.IntegerField(verbose_name="module number")
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
	name = models.CharField(max_length=512,default="")
	slug = models.SlugField(default="",blank=True)
	duration = models.CharField(max_length=512,default="",blank=True)
	description = models.TextField(default="",blank=True)
	def __unicode__(self):
		return str(self.chapter.num) + '-' + str(self.num) + ': ' + self.name

class ResourceType(models.Model):
	name = models.CharField(max_length=512)
	column = models.IntegerField()
	row = models.IntegerField()
	def __unicode__(self):
		return str(self.name)

class Resource(models.Model):
	rtype = models.ForeignKey(ResourceType, on_delete=models.PROTECT, verbose_name="resource type")
	module = models.ForeignKey(Module, on_delete=models.CASCADE)
	name = models.CharField(max_length=512,default="")
	content = models.CharField(max_length=512,default="",blank=True, verbose_name="description")
	link = models.CharField(max_length=512,default="",blank=True)
	def __unicode__(self):
		return self.name

# Visibility classes, to deal with the visibility on particular teacher pages

class ChapterVisibility(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
	visible = models.BooleanField(default=True)
	def __unicode__(self):
		return str(self.user) + "." + str(self.chapter)
	class Meta:
		verbose_name_plural = "chapter visibilities"

class ModuleVisibility(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	module = models.ForeignKey(Module, on_delete=models.CASCADE)
	visible = models.BooleanField(default=True)
	def __unicode__(self):
		return str(self.user) + "." + str(self.module)
	class Meta:
		verbose_name_plural = "module visibilities"

class ResourceVisibility(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
	visible = models.BooleanField(default=True)
	def __unicode__(self):
		return str(self.user) + "." + str(self.resource)
	class Meta:
		verbose_name_plural = "resource visibilities"

