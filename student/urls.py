from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='std-index'),
    path('quiz', views.quiz, name='std-quiz'),
    path('play-quiz/<int:pk>', views.playQuiz, name='std-play-quiz'),
    path('submit-quiz/<int:pk>', views.submitQuiz, name='std-submit-quiz'),
    path('classroom-discussion', views.classRoomDiscussion, name='std-classroom-discussion'),
    # Updated: flipped discussion now includes event_id for access control
    path('flipped-classroom-discussion/<int:event_id>/', views.flippedClassRoomDiscussion, name='std-flipped-classroom-discussion'),
    # New endpoints for asking and replying
    path('flipped-discussion/ask/<int:event_id>/', views.askFlippedQuestion, name='std-flipped-ask'),
    path('flipped-discussion/reply/<int:discussion_id>/', views.replyFlippedQuestion, name='std-flipped-reply'),
    path('attendance', views.attendance, name='std-attendance'),
    path('extra-cirricular', views.extraCirricular, name='std-extra-cirricular'),
    path('event', views.event, name='std-event'),
    path('event-apply/<int:pk>', views.eventApply, name='std-event-apply'),
    path('feedback', views.feedback, name='std-feedback'),
    path('quiz/retest/<int:pk>/', views.retestQuiz, name='std-quiz-retest')
]