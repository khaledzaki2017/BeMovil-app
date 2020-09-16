# from django.urls import path

# #from multi_step_form.views import FormStep1, FormStep2, FormStep3
# from multi_step_form.views import Form_list
# from multi_step_form import views
# from rest_framework.routers import DefaultRouter

# app_name = 'multi_step_form'

# urlpatterns = [
#     path('api/', views.Form_list),

#     # path('', FormStep1.as_view(), name='step_1'),
#     # path('step-2', FormStep2.as_view(), name='step_2'),
#     # path('step-3', FormStep3.as_view(), name='step_3'),
# ]
from django.urls import path, include
from rest_framework import routers

from multi_step_form import views
from .views import ValidatePhoneSendOTP

router = routers.DefaultRouter()
router.register('wizard', views.WizardFormViewSet, base_name='wizard')

router.register('WizardList', views.WizardFormListView, base_name='WizardList')
# router.register('step2', views.Step2ViewSet)
# router.register('step3', views.Step3ViewSet)
router.register('user-image', views.UserPicturesViewSet)
app_name = 'multi_step_form'


urlpatterns = [
    path('', include(router.urls)),
    path('file/', views.FileView.as_view()),
    path('filedetail/<int:pk>/', views.FileDetail.as_view()),
    path('filelist/', views.FileViewlist.as_view()),

    path('validate_phone/', ValidatePhoneSendOTP.as_view()),
    path('email-check/', views.EmailCheck.as_view(), name='email-check'),



]
