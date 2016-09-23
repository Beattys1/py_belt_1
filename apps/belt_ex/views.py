from django.shortcuts import render, HttpResponse, redirect
from .models import User, Relationship
from django.contrib import messages
from django.db.models import Q

def index(request):
    # if "current_user" in request.session:
    #     return redirect('/friend_show')
    return render(request, 'belt_ex/index.html')

def register(request):
    name = request.POST['name']
    alias = request.POST['alias']
    email = request.POST['email']
    password = request.POST['password']
    passconf = request.POST['passconf']
    dob = request.POST['dob']
    errors, user = User.userManager.register(name, alias, email, password, passconf, dob)
    if errors:
        for i in range(0, len(errors)):
            messages.warning(request, errors[i])
        return redirect('/')
    if user:
        messages.success(request, 'Wow! You did it! You really registered!')
        return redirect('/')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        error, user = User.userManager.login(request.POST['email'], request.POST['password'])
        if error:
            for i in range(0 , len(error)):
                messages.warning(request, error[i])
            return redirect('/')
        if user:
            request.session['current_user'] = user.id
            return redirect('/friend_show')
    else:
        return redirect('/')

def logout(request):
    del request.session['current_user']
    return redirect('/')

def friend_show(request):
    if 'current_user' in request.session:
        user = User.objects.get(id=request.session['current_user'])
        friends = Relationship.objects.filter(user_id = user)
        all_users_but_me = User.objects.exclude(id=user.id)
        all_my_friends = Relationship.objects.filter(friend_id = user)
        print friends
        print "*************"
        print all_my_friends
        not_friends = all_users_but_me.exclude(user_relate__in=all_my_friends)
        # not_friends = User.objects.filter(relationship__isnull=True).filter(~Q(id=id))
        # for friend in not_friends:
        #     print friend.alias
        #     print friends
        if not friends:
            messages.warning(request, "you have no friends... sorry ")
        context = {
            'profile': user.alias,
            'friend':friends,
            'not_friends':not_friends,
        }
        return render(request, 'belt_ex/friends.html', context)
    else:
        return redirect('/')

def user(request, id):
    if 'current_user' in request.session:
        user = User.objects.get(id = id)
        context = {"user" : user}
        return render(request, 'belt_ex/user.html',context)
    else:
        return redirect('/')

def delete(request, id):
    Relationship.objects.filter(user_id = User.objects.get(id=request.session['current_user']), friend_id = User.objects.get(id=id)).delete()
    Relationship.objects.filter(friend_id = User.objects.get(id=request.session['current_user']), user_id = User.objects.get(id=id)).delete()


    return redirect('/friend_show')

def add_friend(request, id):
    Relationship.objects.create(user_id = User.objects.get(id=request.session['current_user']), friend_id=User.objects.get(id=id))
    Relationship.objects.create(user_id=User.objects.get(id=id), friend_id = User.objects.get(id=request.session['current_user']))
    return redirect('/friend_show')
