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
from rest_framework.routers import DefaultRouter

from multi_step_form import views


router = DefaultRouter()
router.register('wizard', views.WizardFormViewSet)

# router.register('step1', views.Step1ViewSet)
# router.register('step2', views.Step2ViewSet)
# router.register('step3', views.Step3ViewSet)
# router.register('upload-image', views.UserPicturesViewSet)

app_name = 'multi_step_form'


urlpatterns = [
    path('', include(router.urls))
]
