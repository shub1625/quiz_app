from django.urls import path
from .views import QuizListView,quiz_detail_view,quiz_data_view,quiz_save_view

app_name = 'quizes'
urlpatterns = [
    path('', QuizListView.as_view(),name='quiz_list'),
    path('<int:pk>/', quiz_detail_view,name='quiz-detail'),
    path('<int:pk>/data', quiz_data_view,name='quiz-data'),
    path('<int:pk>/save', quiz_save_view,name='quiz-save'),

]
