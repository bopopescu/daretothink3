from django.shortcuts import render
from userprofile.models import Post, Motion, Comment
from django.forms import ModelForm, Textarea, TextInput
from tinymce.widgets import TinyMCE
from django import forms
#from tinymce import models as tinymce_models
from tinymce.models import HTMLField

class PostForm(ModelForm):
    #body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    body = HTMLField()

    class Meta:
        model = Post
        fields = ['title', 'body',]
        #widgets = {
        #    'body': SummernoteInplaceWidget(),
        #}

    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/textareas.js',)



class MotionForm(ModelForm):
    class Meta:
        model = Motion
        fields = ['title', 'post',]
        widgets = {
            'title': Textarea(attrs={'cols': 70, 'rows': 1}),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body','motion','post',]
        widgets = {
            'body': Textarea(attrs={'cols': 70, 'rows': 3}),
        }

def userprofile_blog(request):
    all_posts = Post.objects.all().order_by('-date')
    all_motions = Motion.objects.all().order_by('-date')
    all_comments = Comment.objects.all().order_by('-date')


    postform = PostForm(request.POST)
    motionform = MotionForm(request.POST)
    commentform = CommentForm(request.POST)
    template_data = {'postform' : postform, 'motionform' : motionform, 'commentform': commentform, 'posts' : all_posts, 'motions' : all_motions, 'comments' : all_comments,}

    if request.method == 'POST':
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            if commentform.cleaned_data['body']:
                comment.post = commentform.cleaned_data['post']
                comment.motion = commentform.cleaned_data['motion']
                comment.body = commentform.cleaned_data['body']
                comment.author = request.user

                if 'yes' in request.POST:
                    comment.yes = comment.yes + 1
                elif 'maybe' in request.POST:
                #elif commentform.cleaned_data['maybe']:
                    comment.maybe = comment.maybe + 1
                elif 'no' in request.POST:
                    comment.no = comment.no + 1

                comment.save()
        elif motionform.is_valid():
            motion = motionform.save(commit=False)
            if motionform.cleaned_data['title']:
                motion.post = motionform.cleaned_data['post']
                motion.title = motionform.cleaned_data['title']
                motion.author = request.user
                motion.save()
    else:
        motionform = MotionForm()
        commentform = CommentForm()

    return render(request, 'userprofile_blog.html', template_data)




def userprofile_newblog(request):
    all_posts = Post.objects.all().order_by('-date')
    all_motions = Motion.objects.all().order_by('-date')
    all_comments = Comment.objects.all().order_by('-date')

    postform = PostForm(request.POST)
    motionform = MotionForm(request.POST)
    commentform = CommentForm(request.POST)
    template_data = {'postform' : postform, 'motionform' : motionform, 'commentform': commentform, 'posts' : all_posts, 'motions' : all_motions, 'comments' : all_comments,}

    if request.method == 'POST':
        if postform.is_valid():
            post = postform.save(commit=False)
            post.title = postform.cleaned_data['title']
            post.body = postform.cleaned_data['body']
            post.author = request.user
            post.save()
            return render(request, 'userprofile_blog.html', template_data)
    else:
        postform = PostForm()
        return render(request, 'userprofile_newblog.html', template_data)

