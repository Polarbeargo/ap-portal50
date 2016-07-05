from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from curriculum.models import UserProfile, Chapter, Module, Resource, ChapterVisibility, ModuleVisibility, ResourceVisibility, ResourceType
from django.contrib.auth.models import User, Group
from quizbank.models import Tag, Question, QuestionType
# Register your models here.


# sets up the admin site with custom headers
class AP50Admin(AdminSite):
	site_title = ugettext_lazy('CS50 AP Admin')
	site_header = ugettext_lazy('CS50 AP Admin')
	index_title = ugettext_lazy('Site administration')

# defines an inline admin section, so modules can be added on the chapter view
class ModuleInline(admin.StackedInline):
	model = Module
	extra = 2

class UserProfileInline(admin.StackedInline):
	model = UserProfile

class ResourceInline(admin.TabularInline):
	model = Resource
	extra = 5

# defines admin panels
class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		('Basics', {'fields':['username', 'first_name', 'last_name', 'email', 'password']}),
		('Permissions', {'fields':['is_staff', 'groups', 'user_permissions']}),
	]
	inlines = [UserProfileInline]
	ordering = ['id']
	list_display = ('username', 'first_name', 'last_name', 'approval_status')
	# approval status is an attribute of the UserProfile, so need a definition to view it
	def approval_status(self, x):
		return x.userprofile.approved
	approval_status.short_description = 'Approved'
	list_filter= ['userprofile__approved', 'is_staff']

class ChapterAdmin(admin.ModelAdmin):
	# module editor appears inside the chapter editor
	inlines = [ModuleInline]
	list_display = ('name', 'num', 'module_count')
	def module_count(self, x):
		return len(Module.objects.filter(chapter=x))
	ordering = ['num']

class ModuleAdmin(admin.ModelAdmin):
	inlines = [ResourceInline]
	list_display = ('name', 'chapter', 'module_num')
	def module_num(self,x):
		return x.num
	ordering = ['chapter__num', 'num']

class ResourceAdmin(admin.ModelAdmin):
	list_display = ('name', 'module', 'rtype')
	ordering = ['module__chapter__num', 'module__num', 'rtype']

class ResourceTypeAdmin(admin.ModelAdmin):
	list_display = ('name', 'column', 'row')
	ordering = ['column', 'row']

admin_site = AP50Admin()

admin_site.register(User, UserAdmin)
admin_site.register(Group)

# admin_site.register(UserProfile)
admin_site.register(Chapter, ChapterAdmin)
admin_site.register(Module, ModuleAdmin)
admin_site.register(Resource, ResourceAdmin)
admin_site.register(ResourceType, ResourceTypeAdmin)

# Getting rid of visibilities from admin site
# admin_site.register(ChapterVisibility)
# admin_site.register(ModuleVisibility)
# admin_site.register(ResourceVisibility)


# QuizBank Admin Registrations
class TagAdmin(admin.ModelAdmin):
	ordering=['name']

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		('General', {'fields':['title', 'question', 'q_image', 'answer', 'a_image']}),
		('Metadata', {'fields':['tags', 'qtype', 'released', 'points', 'difficulty', 'authorship_year']}),
		('Source (optional)', {'fields':['original_exam', 'original_question']})
	]
	list_display = ('title', 'qtype', 'difficulty', 'original_exam', 'original_question')
	ordering = ['-original_exam', 'original_question']
	filter_horizontal = ('tags',) # this creates the search for tag, and allows moving left and right
	# may need to change the ordering once non-exam questions start getting added, leaving this in comments in case
	# list_display = ('title', 'qtype', 'difficulty', 'authorship_year', 'released')
	# ordering = ['-authorship_year', 'title']

class QuestionTypeAdmin(admin.ModelAdmin):
	list_display = ('name', 'position')
	ordering = ['position', 'name']

admin_site.register(Tag, TagAdmin)
admin_site.register(Question, QuestionAdmin)
admin_site.register(QuestionType, QuestionTypeAdmin)