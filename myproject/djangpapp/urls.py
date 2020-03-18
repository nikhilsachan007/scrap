from django.contrib import admin  
from django.urls import path  
from django.contrib.auth import views as auth_views
from myapp import views  
urlpatterns = [  
     path('admin/', admin.site.urls),
     path('login/',auth_views.LoginView.as_view(template_name='registration/login.html')),
     path('',auth_views.LoginView.as_view(template_name='registration/login.html')) ,
     path('view/',views.view),
     path('delete/<int:id>',views.delete),
     path('edit/<int:id>',views.edit),
     path('update/<int:id>',views.update),
     path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html')),
     path('urlstd/',views.urlstd),
     path('std/',views.std) 
]  