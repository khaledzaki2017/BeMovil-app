# # from rest_framework.routers import DefaultRouter
# # from pdf_results import views
# # from django.urls import path, include


# # router = DefaultRouter()
# # router.register('file', views.PDFfilesLoadPDF, basename="pdf-read")
# # router.register('files', views.PDFfilesView, basename="pdf-list")
# # # router.register('file', views.render_pdf_view, basename='test-view')
# # app_name = 'pdf_results'


# # urlpatterns = [
# #     path('', include(router.urls))
# # ]
# from django.urls import path

# from .views import FileView, FileDetail, FileViewlist

# # from rest_framework.routers import DefaultRouter

# app_name = 'pdf_results'


# # router = DefaultRouter()
# # router.register('upload-file', FileLoadPDF)

# urlpatterns = [
#     path('upload_file/', FileView.as_view()),
#     path('list_file/', FileViewlist.as_view()),
#     path('detail_file/<int:pk>/', FileDetail.as_view(), name='file-detail'),
#     # path('load_pdf/<int:pk>/', FileLoadPDF.as_view({'get': 'retrieve'})),
#     # path('', include(router.urls))


# ]
