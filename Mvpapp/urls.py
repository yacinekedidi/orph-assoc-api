from django.conf.urls import url
from Mvpapp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^family/$', views.familyApi),
    url(r'^family/([0-9]+)$', views.familyApi),
    url(r'^orphan/$', views.orphanApi),
    url(r'^orphan/([0-9]+)$', views.orphanApi),
    url(r'^subsidy/$', views.subsidyApi),
    url(r'^subsidy/([0-9]+)$', views.subsidyApi),
    url(r'^orphaneducation/$', views.orphaneducationApi),
    url(r'^orphaneducation/([0-9]+)$', views.orphaneducationApi),
    url(r'^familysubsidy/$', views.familysubsidyApi),
    url(r'^familysubsidy/([0-9]+)$', views.familysubsidyApi)


    # url(r'^employee/$',views.employeeApi),
    # url(r'^employee/([0-9]+)$',views.employeeApi),

]
