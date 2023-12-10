# MAIN APP URLS

from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),

  path('finches/', views.finches_index, name='index'),
  path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
  path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
  path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
  path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
  path('finches/<int:finch_id>/add_flight/', views.add_flight, name='add_flight'),

  path('finches/<int:finch_id>/assoc_cage/<int:cage_id>/', views.assoc_cage, name='assoc_cage'),
  path('finches/<int:finch_id>/disassoc_cage/<int:cage_id>/', views.disassoc_cage, name='disassoc_cage'),

  path('cages/', views.CageList.as_view(), name='cages_index'),
  path('cages/<int:pk>/', views.CageDetail.as_view(), name='cages_detail'),
  path('cages/create/', views.CageCreate.as_view(), name='cages_create'),
  path('cages/<int:pk>/update/', views.CageUpdate.as_view(), name='cages_update'),
  path('cages/<int:pk>/delete/', views.CageDelete.as_view(), name='cages_delete'),
]