from myblog.models import Post
from myblog.forms import PostForm, RegistrationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from myblog.serializers import PostSerializer
from rest_framework.decorators import api_view


def create_user(request):
    # Get the request context
    context_instance=RequestContext(request)
    if request.method == 'POST' and request.POST.get('create'):
        reg_form = RegistrationForm(request.POST or None)
        if reg_form.is_valid():
            username = request.POST.get('username', '')
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            new_user = reg_form.save()
            new_user = authenticate(username = new_user.username, password = password1)
            if new_user is not None and  new_user.is_active:
                login(request, new_user)
                messages.success(request, "Registration Successful")
                return HttpResponseRedirect('/myblog/')
            else:
                messages.success(request, "Registration Successful, Login Again!")
                return HttpResponseRedirect('/login/')
        else:
            reg_form =RegistrationForm()
            context = {'form': reg_form, 'message': "Form data invalid."}
            context.update(csrf(request))
            return render_to_response('creatuser.html', context, context_instance)

    else:
        reg_form =RegistrationForm()

    context = {'form': reg_form}
    context.update(csrf(request))
    return render_to_response('creatuser.html',
                             context,
                             context_instance)


def login_user(request):
    if request.method == 'POST' and request.POST.get('login'):
        uname = request.POST.get('username', '')
        pword = request.POST.get('password', '')
        user = authenticate(username = uname, password = pword)
        if user is not None and  user.is_active:
            login(request, user)
            message = 'welcome to the blog!'
            return HttpResponseRedirect('/myblog/')
        else:
            messages.info(request,"Invalid username or  password.")
            return HttpResponseRedirect('/login/')

    context = {}
    context.update(csrf(request))
    return render_to_response('login.html',
                     context,context_instance = RequestContext(request))


def logout_user(request):
    logout(request)
    messages.info(request,"You are logged out.")
    return HttpResponseRedirect('/myblog/')


def show_post(request):
    """
    Create a view for showing the latest 6 post from the blog
    data is fetched from the model using fetchAllPosts() method
    """
    queryset = Post.fetchAllPosts()
    if queryset:
        msg = "All blog posts"
        context = {'posts': queryset,
                   'message': msg,
                   }

        # Create HTTP response , pass data from one view to another
    else:
        msg = "Empty blog...add new posts!"
        context = {'posts': '', 'message': msg}

    return render_to_response('index.html',
                              context,
                              context_instance=RequestContext(request))

def detail_post(request, postid):
    try:
        fetch = Post.objects.get(id=postid)
        if fetch is not None:
           msg = "Detail view post %d: " % (int(postid))
           context = {'post': fetch,
                      'message': msg,
                      }
           return render_to_response('singlepost.html',
                                context,
                                context_instance=RequestContext(request))
    except Post.DoesNotExist:
        msg = "No blog post found."
        context = {'message': msg,}
        return render_to_response('index.html',context,
                                context_instance=RequestContext(request))

@login_required(login_url='/login/')
def add_post(request):
    """
    Add a new post to the blog and it will be saved into the model,
    then the last added element will be fetched to show the details
    """
    if request.method == 'POST' and request.POST.get('save'):
        form = PostForm(request.POST)
        if form.is_valid():
            new_blogpost = form.save(commit=False)
            new_blogpost.author = request.user
            form.save()
            message =  "New post %d added!"
            return HttpResponseRedirect('/myblog/')
    elif request.method == 'POST' and request.POST.get('cancel'):
        message = "Adding new post cancelled!"
        return HttpResponseRedirect('/myblog/')
    else:
        form = PostForm()

    context = {}
    context.update(csrf(request))
    context['form'] = form
    return render_to_response('addblog.html',
                             context,
                             context_instance=RequestContext(request))


@login_required(login_url='/login/')
def edit_post(request, postid):
    """
    Fetch the nth post from the blog, validate the input data and update the model,
    """
    try:
        queryset = Post.objects.get(id=postid)
        context = {'post': queryset,}
        if request.method == 'POST' and request.POST.get('update'):
            # Create a form to edit an existing Post, but use
            # POST data to populate the form!
            p_instance = Post.objects.get(pk=postid)
            if p_instance.author == request.user:
                update_form = PostForm(request.POST, instance=p_instance)
                if update_form.is_valid():
                    update_form.save()
                    msg = "Post %d: updated! " %(int(postid))
                    context = {'post': queryset, 'message': msg}
                    return HttpResponseRedirect('/myblog/'+ postid)
            else:
                msg = "You can only edit your blog posts."
                context = {'message': msg}
                return render_to_response('index.html',
                              {'message': msg},
                              context_instance=RequestContext(request))

        elif request.method == 'POST' and request.POST.get('cancel'):
            msg = "Updating post cancelled!"
            return HttpResponseRedirect('/myblog/')
        else:
            msg = "Updating post interrupted!"
            return render_to_response('editblog.html',
                              context,
                              context_instance=RequestContext(request))
    except Post.DoesNotExist:
        msg = "No blog post found for edit."
        context = {'message': msg,}
        return render_to_response('index.html',context,
                                context_instance=RequestContext(request))

@login_required(login_url='/login/')
def delete_post(request, postid):
    """
    Delete the nth post where n = postId entered from the user url
    """
    context = {}
    if Post.exists(postid):
        queryset = Post.getPostByID(postid)
        if queryset:
            if queryset.author == request.user:
                message = 'Post %d Deleted!' %(int(postid))
                queryset.delete()
                return HttpResponseRedirect('/myblog/')
            else:
                return render_to_response('index.html',
                              {'message':  "You can only delete your blog posts."},
                              context_instance=RequestContext(request))
    else:
        context = {}
        context.update(csrf(request))
        context = {'message': "Nothing to delete!"}

    return render_to_response('index.html',
                             context,
                             context_instance=RequestContext(request))


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'PUT'])
@csrf_exempt
def apiblog(request):
    if request.method == 'GET':
        blog = Post.objects.all()
        serializer = PostSerializer(blog, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        test_data =  {
        "title": "True Story",
        "content": "Implement a RESTful web service",
        "timestamp": "2016-10-25T13:20:20.473Z",
        "author": 4
        }
        serializer = PostSerializer(data=data)
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = 201)
        return JSONResponse(serializer.errors, status = 400)

