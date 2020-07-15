from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import NewComment, NewPost, UpdateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse,reverse_lazy



def index(request):
    comments = Comment.objects.all()
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        paginator.page(paginator.num_page)
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': posts,
        'comments': comments,
        'page': page,
    }

    return render(request, 'blog/index.html', context)


def about(request):
    context = {
        'title': 'من أنا',
    }
    return render(request, 'blog/about.html', context)



def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # comments = post.comments.filter(active=True)
    comments = post.comments.all()

    # check before saving data
    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()
    context = {
        'title': post,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
      
    }
    return render(request, 'blog/detail.html', context)


@login_required(login_url='login')
def new_post(request):
    if request.method == 'POST':
        user = User.objects.first()
        new_post_form = NewPost(request.POST,request.FILES)
        post = new_post_form.save(commit=False)
        post.author_id = request.user.id
        post.save()
        
        messages.success(
            request, f'تمت اضافة تدوينة جديدة بنجاح')
        return redirect('index')

    else:
        new_post_form = NewPost()
      
    
    context = {
        'title': 'اضافة تدوينة جديدة',
        'new_post_form': new_post_form,
      
        

    }
    return render(request, 'blog/new_post.html', context)


@login_required(login_url='login')
def update_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        
        form = UpdateForm(request.POST or None, instance=post)
        if form.is_valid:
            form.save()
            messages.success(
                request, f'تم تعديل التدوينة  بنجاح')
            return redirect('index')
    else:
        form = UpdateForm(request.POST or None, instance=post)
    context = {
        'title': 'تعديل تدوينة',
        'form': form, 
    }
    return render(request, 'blog/update_post.html', context)


@login_required(login_url='login')
def delete_post(request, id):
    post=Post.objects.get(id=id)
    if request.method=='POST':
        post.delete()
        messages.success(
            request, f'تم حذف التدوينة  بنجاح')
        return redirect('index')
    context={
        'title':'حذف تدوينة',
    }
    return render(request, 'blog/confirm_delete_post.html', context)
