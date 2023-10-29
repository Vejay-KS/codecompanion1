"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from codecompanionapp import views
from django.conf.urls import include

app_name = "codecompanionapp"   

router = routers.DefaultRouter()
router.register(r'codecompanions', views.CodecompanionView, 'codecompanionview')

#path('auth/', include('rest_auth.urls')),

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('home/', views.homepage, name="homepage"),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name= "logout"),
    path('codeOptimizer/', views.code_optimizer, name= "codeOptimizer"),
    path('codeDebugger/', views.code_debugger, name= "codeDebugger"),
    path('codeReviewer/', views.code_reviewer, name= "codeReviewer"),
    path('commentGenerator/', views.comment_generator, name= "commentGenerator"),
    path('documentationHelper/', views.documentation_helper, name= "documentationHelper"),
    path('learningPathRecommendations/', views.learning_path_recommendation, name= "learningPathRecommendations"),
    path('letterGenerator/', views.letter_generator, name= "letterGenerator"),
    path('resumeFilterer/', views.resume_filterer, name= "resumeFilterer"),
    path('summarizeAppraisals/', views.summarize_appraisals, name= "summarizeAppraisals"),
    path('technicalTrends/', views.technical_trends, name= "technicalTrends"),
    path('unitTestGenerator/', views.unit_test_generator, name= "unitTestGenerator"),
]