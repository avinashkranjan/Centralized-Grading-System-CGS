from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

# urlpatterns = [
#     path('',assignment_home, name='assignment_page'),
#     path('add/',assignment_add, name='assignment_add'),
# ]


urlpatterns = [
    path('', home, name='home'),
    
    path('teachers/', include(([
        path('', assignment_home, name='assignment_page'),
        path('assignment/add/', assignment_add, name='assignment_add'),
        path('assignment/<int:pk>/', assignment_update, name='assignment_update'),
        path('assignment/<int:pk>/delete/', assignment_delete, name='assignment_delete'),
        path('assignment/<int:pk>/submitted/', submitted_assignment, name='assignment_submitted'),
    ],'assignment'), namespace='teachers')),

    path('students/', include(([
        path('', student_assignment_home, name='assignment_page'),
        path('<int:pk>/submit', student_assignment_upload, name='assignment_upload'),
    ],'assignment'), namespace='students'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)