from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('project-page/', ProjectPageView, name='project_page'),
    path('login/', UserLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    path('signup/', signup, name='signup'),
    path('section/', sectionView, name='section'),
    path('profile/', ProfileView, name='profile'),
    path('comment/<int:com_id>/', CommentView, name='comment'),
    path('project/<int:pcjt_id>/', ProjectView, name='project'),
    path('editprofile/<int:id_user>/', EditProfileView, name='edit_profile'),
    path('edit-project/<int:edit_id>/', EditProjectView, name='edit_project'),
    path('delete-project/<int:delete_id>/', DeleteProjectView, name='delete_project'),
]

