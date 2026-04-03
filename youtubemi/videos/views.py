from django.shortcuts import render, get_object_or_404,redirect
from .models import Video,VideoComment
from .forms import VideoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .forms import CustomUserCreationForm

def video_list(request):
    videos = Video.objects.all().order_by('-uploaded_at')
    return render(request, 'videos/video_list.html', {'videos': videos})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.views += 1
    video.save()

    videos = Video.objects.exclude(pk=pk)[:5]

    # Avtorning profili
    author_profile, created = Profile.objects.get_or_create(user=video.author)

    return render(request, 'videos/video_detail.html', {
        'video': video,
        'videos': videos,
        'author_profile': author_profile,
    })


@login_required
def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user  
            video.save()
            return redirect('videos:video_list')
    else:
        form = VideoForm()
    return render(request, 'videos/video_form.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('videos:login')  # yoki bosh sahifa
    else:
        form = CustomUserCreationForm()
    return render(request, 'videos/signup.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')



def like_video(request, pk):
    video = Video.objects.get(pk=pk)
    video.likes += 1
    video.save()
    return JsonResponse({'likes': video.likes})

def dislike_video(request, pk):
    video = Video.objects.get(pk=pk)
    video.dislikes += 1
    video.save()
    return JsonResponse({'dislikes': video.dislikes})



@login_required
def add_comment(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            VideoComment.objects.create(video=video, user=request.user, content=content)
    return redirect('videos:video_detail', pk=pk)


@login_required
def subscribed_videos(request):
    subscribed_authors = Profile.objects.filter(profile_subscribers=request.user).values_list('user', flat=True)
    videos = Video.objects.filter(author__in=subscribed_authors)
    return render(request, 'videos/subscribed_videos.html', {'videos': videos})


# views.py
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Profile, Video

@login_required
def toggle_subscribe(request, author_id):
    author_profile = get_object_or_404(Profile, user__id=author_id)
    if request.user in author_profile.subscribers.all():
        author_profile.subscribers.remove(request.user)
        subscribed = False
    else:
        author_profile.subscribers.add(request.user)
        subscribed = True
    return JsonResponse({
        'subscribed': subscribed,
        'subscriber_count': author_profile.subscribers.count()
    })




from django.contrib.auth.models import User
from .models import Subscription
@login_required
def subscribe_author(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    if author != request.user:
        Subscription.objects.get_or_create(subscriber=request.user, author=author)
    return redirect(request.META.get('HTTP_REFERER', '/'))

from .models import Video, CustomUser
def author_videos(request, author_id):
    author = get_object_or_404(CustomUser, pk=author_id)
    videos = Video.objects.filter(author=author).order_by('-uploaded_at')
    return render(request, 'videos/author_videos.html', {
        'author': author,
        'videos': videos
    })