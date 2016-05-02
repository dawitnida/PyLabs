from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.context_processors import csrf
from datetime import datetime

from myblog.models import Post
from myblog.forms import PostForm


cnt_visit = 0
cnt_edit = 0
cnt_create = 0
cnt_delete = 0
session_dict = {}

# Reset the sessions and also the counter
def reset_sessions(request, cnt_sessions = 0):
    global session_dict
    queryset = request.session.flush()
    s_time = str(datetime.now().strftime( "%b. %d,%Y, %I:%M %p"))
    return queryset, s_time, cnt_sessions


# Store session as dictionary for different session keys, returns unpacked session items
def get_sessions():
    session_dict = {'visited' : cnt_visit,
                    'edited': cnt_edit,
                    'created': cnt_create,
                    'deleted' : cnt_delete,
                    }
    return session_dict.items()


# Get the start time of the session
def session_start_date(request):
    s_time = str(datetime.now().strftime( "%b. %d,%Y, %I:%M %p"))
    count =  max(get_sessions(), key=lambda x: x[1])
    print count
    if count[1] == 1:
        request.session['visit'] = s_time
        return s_time


# Count corresponding sessions depending on the user action and return counter<type(int)>
def count_session(request, page, counter):
    if page in request.session:
        counter += 1
    else:
        counter = 1
    return counter


def show_post(request):
    """
    Create a view for showing the latest 6 post from the blog
    data is fetched from the model using fetchAllPosts() method
    """
    queryset = Post.fetchAllPosts()
    ss_start = session_start_date(request)
    if queryset:
        msg = "All blog posts"
        context = {'posts': queryset,
                   'message': msg,
                   'sessionStartTime' : ss_start,
                   'sessionStat' : get_sessions(),
                   }

        # Create HTTP response , pass data from one view to another
    else:
        msg = "Empty blog...add new posts!"
        context = {'posts': '', 'message': msg}

    res = render_to_response('../../Pythonidae/templates/index.html',
                              context,
                              context_instance=RequestContext(request))
    return res

def detail_post(request, postid):
    """
    Display details of the nth post where n = postId from the user url
    """
    global cnt_visit

    request.session['detail'] = True
    cnt_visit = count_session(request, 'detail', cnt_visit)
    ss_start = session_start_date(request)

    fetch = Post.getPostByID(postid)
    if fetch:
       msg = "Detail view post %d: " % (int(postid))
       context = {'post': fetch,
                  'message': msg,
                  'sessionStartTime' : ss_start,
                  'sessionStat' : get_sessions(),
                  }
       res = render_to_response('singlepost.html',
                                context,
                                context_instance=RequestContext(request))
       return res
    return HttpResponseRedirect('/myblog/')


def add_post(request):
    """
    Add a new post to the blog and it will be saved into the model,
    then the last added element will be fetched to show the details
    """
    global cnt_create

    if request.method == 'POST' and request.POST.get('save'):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            message =  "New post %d added!"
            request.session['create'] = True
            cnt_create = count_session(request, 'create', cnt_create)
            return HttpResponseRedirect('/myblog/')
    elif request.method == 'POST' and request.POST.get('cancel'):
        message = "Adding new post cancelled!"
        return HttpResponseRedirect('/myblog/')
    else:
        form = PostForm()
    ss_start = session_start_date(request)
    context = {'sessionStartTime' : ss_start,
               'sessionStat' : get_sessions(),
               }
    context.update(csrf(request))
    context['form'] = form
    res = render_to_response('addblog.html',
                             context,
                             context_instance=RequestContext(request))
    return res


def edit_post(request, postid):
    """
    Fetch the nth post from the blog, validate the input data and update the model,
    """
    global cnt_edit

    queryset = Post.getPostByID(postid)
    ss_start = session_start_date(request)

    if queryset:
        queryset = Post.getPostByID(postid)
        context = {'post': queryset,
                   'sessionStartTime' : ss_start,
                   'sessionStat' : get_sessions(),
                   }
    else:
        queryset = Post.objects.get(id=postid)

    if request.method == 'POST' and request.POST.get('update'):
        # Create a form to edit an existing Post, but use
        # POST data to populate the form!
        p_instance = Post.objects.get(pk=postid)
        update_form = PostForm(request.POST, instance=p_instance)
        if update_form.is_valid():
            update_form.save()

            request.session["edit"] = True
            cnt_edit = count_session(request, 'edit', cnt_edit)
            ss_start = session_start_date(request)

            message = "Post %d: updated! " %(int(postid))
            context = {'post': queryset, 'message': message}
            return HttpResponseRedirect('/myblog/'+ postid)
    elif request.method == 'POST' and request.POST.get('cancel'):
        message = "Updating post cancelled!"
        return HttpResponseRedirect('/myblog/')
    else:
        message = "Updating post interrupted!"

    res = render_to_response('editblog.html',
                              context,
                              context_instance=RequestContext(request))
    return res


def delete_post(request, postid):
    """
    Delete the nth post where n = postId entered from the user url
    """
    global cnt_delete
    context = {}

    if Post.exists(postid):
        try:
            fetch = Post.getPostByID(postid)
            if fetch:
                message = 'Post %d Deleted!' %(int(postid))
                fetch.delete()

                request.session['delete'] = True
                cnt_delete = count_session(request, 'delete', cnt_delete)
        except ValueError:
            raise Http404()

        return HttpResponseRedirect('/myblog/')
    else:
        msg = 'Nothing to delete!'
        ss_start = session_start_date(request)
        context = {}
        context.update(csrf(request))
        context = {'message': msg,
                   'sessionStartTime' : ss_start,
                   'sessionStat' : get_sessions(),
                   }

    res = render_to_response('../../Pythonidae/templates/index.html',
                             context,
                             context_instance=RequestContext(request))
    return res
