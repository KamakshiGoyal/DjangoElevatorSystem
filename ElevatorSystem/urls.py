"""
URL configuration for ElevatorSystem project.

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

from ElevatorSystem.viewsets import (ElevatorRequestViewSet,
                                     ElevatorSystemViewSet, ElevatorViewSet)

router = routers.DefaultRouter()
router.register(r'elevatorsystems', ElevatorSystemViewSet, basename = 'elevatorsystem')
urlpatterns = router.urls

urlpatterns = [  
    path('elevatorsystem/', ElevatorSystemViewSet.as_view({'get': 'elevator_system'})),
    path('elevatorsystem/requestelevator/', ElevatorRequestViewSet.as_view({'post': 'create_request'})),
    path('elevatorsystem/elevator/<int:elevator_id>/',
         ElevatorViewSet.as_view({'get': 'get_status'})),
    path('elevatorsystem/elevator/update/<int:elevator_id>/',
         ElevatorViewSet.as_view({'post': 'update_status'})),     
    path('elevatorsystem/elevator/allrequests/<int:elevator_id>/',
         ElevatorViewSet.as_view({'get': 'get_requests'})),
    path('admin/', admin.site.urls)
]

