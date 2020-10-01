
from django.urls import path, include
from rest_framework import routers

from multi_step_form import views
# from .views import ValidatePhoneSendOTP

router = routers.DefaultRouter()
router.register('wizard', views.WizardFormViewSet, base_name='wizard')

router.register('wizardlist', views.WizardFormListView, base_name='wizardlist')

router.register('user-image', views.UserPicturesViewSet)
app_name = 'multi_step_form'


urlpatterns = [
    path('', include(router.urls)),
    path('file/', views.FileView.as_view()),
    path('filedetail/<int:pk>/', views.FileDetail.as_view()),
    path('filelist/', views.FileViewlist.as_view()),

    path("verify/<phone>/", views.getPhoneNumberRegistered.as_view(), name="OTP Gen"),
    path('email-check/', views.EmailCheck.as_view()),
    path('partner/', views.PartnerView.as_view()),
    path('partnerlist/', views.PartnerMainWizardListAPIView.as_view()),

]
