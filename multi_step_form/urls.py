
from django.urls import path, include
from rest_framework import routers

from multi_step_form import views
# from .views import ValidatePhoneSendOTP

router = routers.DefaultRouter()
router.register('wizard', views.WizardFormViewSet, base_name='wizard')
router.register('wizardlist/natural',
                views.WizardFormNaturalListView, base_name='wizardlistnatural')

router.register('wizardlist/juridica',
                views.WizardFormJuridicaListView, base_name='wizardlistjuridica')

# router.register('user-image', views.UserPicturesViewSet)
app_name = 'multi_step_form'


urlpatterns = [
    path('', include(router.urls)),
    # path('file/', views.FileView.as_view()),
    # path('filedetail/<int:pk>/', views.FileDetail.as_view()),
    # path('filelist/', views.FileViewlist.as_view()),
    path("wizard-natural/detail/<pk>/", views.wizardnatural_detail),
    path("wizard-juridica/detail/<pk>/", views.wizardjuridica_detail),

    path("verify/<phone>/", views.getPhoneNumberRegistered.as_view(), name="OTP Gen"),
    path('email-check/', views.EmailCheck.as_view()),
    path('partner/', views.PartnerView.as_view({'post': 'create'})),
    path('partnerlist/', views.PartnerMainWizardListAPIView.as_view()),

]
