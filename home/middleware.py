from datetime import timedelta
from django.utils import timezone
from .models import Profile

class OnlineStatusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user_profile = Profile.objects.get(user=request.user)
            user_profile.last_activity = timezone.now()
            user_profile.is_online = True
            user_profile.save()
        
        response = self.get_response(request)
        
        # Onlayn foydalanuvchilarni tekshirish va last_activity ni yangilash
        online_threshold = timezone.now() - timedelta(minutes=15)  # 15 daqiqa ichida so'ng faol bo'lib chiqishni aniqlang
        online_users = Profile.objects.filter(last_activity__gte=online_threshold)
        for user_profile in online_users:
            user_profile.is_online = True
            user_profile.save()
        
        return response
