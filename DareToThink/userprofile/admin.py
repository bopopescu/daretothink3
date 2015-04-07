from django.contrib import admin
from userprofile.models import UserProfile, Post, Comment
#from django.http import request
#from django.contrib.auth.models import User

#class UpdateUser(forms.ModelForm):
#    class Meta:
#        model = User


class UserProfileAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
    #if request.user.is_superuser:
        obj.is_staff = True
        obj.save()

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'body')

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(PostAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)