from django.urls import path
from .import views
from .views import SearchResultsView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.login, name="login"),
    path('home',views.home,name='home'),
    path('logout', views.logout, name="logout"),
    path('add_ip', views.add_ip, name="add_ip"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("update/<Iplist_id>", views.update, name="update"),
    path('edit_ip', views.edit_ip, name="edit_ip"),
    path('delete/<Iplist_id>', views.delete, name="delete"),
    path('delete_ip', views.delete_ip, name="delete_ip"),
    path("search/update/<Iplist_id>", views.update, name="update"),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),name='password_change_done'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),name='password_change'),
    path('password_reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),name='password_reset_complete'),
    
]
