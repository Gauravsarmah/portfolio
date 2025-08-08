from django.shortcuts import render
from .models import Skill, Project , BlogPost , skill_header
from django.core.mail import send_mail , EmailMessage
from django.conf import settings

def home(request):
    skills = skill_header.objects.all()
    projects = Project.objects.all()[:3]
    latest_posts = BlogPost.objects.all().order_by('-created_at')[:3]
    return render(request, 'portfolio/home.html', {
        'skills': skills,
        'projects': projects,
        'latest_posts': latest_posts
    })

def about(request):
    skheader = skill_header.objects.all()

    return render(request, 'portfolio/about.html', {'skheader': skheader})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Build email
        email_message = EmailMessage(
            subject=f"Portfolio Contact from {name}",
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]  # So you can click "Reply" in your inbox
        )
        email_message.send()

        return render(request, 'portfolio/contact.html', {'success': True})

    return render(request, 'portfolio/contact.html')


def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'portfolio/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, 'portfolio/blog_detail.html', {'post': post})