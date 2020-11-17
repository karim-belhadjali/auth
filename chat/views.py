from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from authtest.models import User
from chat.models import Message, Messagerecipient


@login_required
def sendPage(request):
    if request.method == 'POST':
        recipient = User.objects.get(username=request.POST.get('recipient'))
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        creator = request.user
        message = Message.objects.create(subject=subject, creator=creator, message_body=body)
        Messagerecipient.objects.create(recipient=recipient, message=message)
        return redirect('loginPage')

    user = request.user
    recipients = User.objects.all()
    context = {
        'user': user,
        'recipients': recipients,
    }
    return render(request, 'chat/send.html', context)


def discussionPage(request):
    if request.method == 'GET':
        print('ok')
    users = []
    messagesent = Messagerecipient.objects.all()
    for m in messagesent:
        user = m.message.creator
        print(m.recipient)
        if user == request.user:
            if users.__contains__(m.recipient):
                print(m.recipient.username + ": is already there" + "  Test 1")
            else:
                users.append(m.recipient)
        else:
            if request.user == m.recipient:
                if users.__contains__(user):
                    print(user.username + ": is already there" + "  Test 2")
                else:
                    users.append(user)

    context = {
        'users': users
    }
    return render(request, 'chat/discussions.html', context)


def detailPage(request, username):
    allmessages = Messagerecipient.objects.all()
    messages = []
    user = request.user
    for m in allmessages:
        if m.recipient == user:
            msg = m.message
            if msg.creator.username == username:
                messages.append(m.message)
        else:
            if m.recipient.username == username:
                msg = m.message
                if msg.creator == user:
                    messages.append(msg)

    messages.sort(key=lambda m: m.create_date)
    context = {
        'messages': messages
    }
    return render(request, 'chat/detail.html', context)


def replyPage(request, id):
    message = Message.objects.get(pk=id)
    context = {
        'message': message
    }
    return render(request, 'chat/reply.html',context)
