from .models import Profile

def user_subscriptions(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            return {'user_subscriptions': profile.subscribers.all()}
        except Profile.DoesNotExist:
            return {'user_subscriptions': []}
    return {}
