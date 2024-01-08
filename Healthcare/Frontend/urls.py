from Frontend import views
from django.urls import path
urlpatterns = [
    path('expertspage/', views.expertspage, name="expertspage"),
    path('exphomepage/', views.exphomepage, name="exphomepage"),
    path('symptompage/', views.symptompage, name="symptompage"),
    path('savesymptoms/', views.savesymptoms, name="savesymptoms"),
    path('managesymptoms/', views.managesymptoms, name="managesymptoms"),
    path('deletesymptom/<int:dataid>/', views.deletesymptom, name="deletesymptom"),


    path('suggestionpage/', views.suggestionpage, name="suggestionpage"),
    path('savesuggestion/', views.savesuggestion, name="savesuggestion"),
    path('managesuggestion/', views.managesuggestion, name="managesuggestion"),
    path('deletesuggestion/<int:dataid>/', views.deletesuggestion, name="deletesuggestion"),
    path('sugesstionview/', views.sugesstionview, name="sugesstionview"),

    path('userpage/', views.userpage, name="userpage"),
    path('usehomepage/', views.usehomepage, name="usehomepage"),
    path('savereg/', views.savereg, name="savereg"),

    path('user_login/', views.user_login, name="user_login"),
    path('coun_msg', views.coun_msg, name="coun_msg"),
    path('expert_coun_msg1/<int:id>', views.expert_coun_msg1, name="expert_coun_msg1"),
    path('expert_coun_insert_chat/<str:msg>/<int:id>', views.expert_coun_insert_chat, name="expert_coun_insert_chat"),
    path('chatview', views.chatview, name="chatview"),
    path('coun_insert_chat/<str:msg>', views.coun_insert_chat, name="coun_insert_chat"),
    path('chat_with_expert/<int:id>', views.chat_with_expert, name="chat_with_expert"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('user_logout/', views.user_logout, name="user_logout"),

    path('expert_login/', views.expert_login, name="expert_login"),
    path('expertlogin/', views.expertlogin, name="expertlogin"),
    path('expert_logout/', views.expert_logout, name="expert_logout"),

    path('profileview/', views.profileview, name="profileview"),
    path('updateprofile/<int:dataid>/', views.updateprofile, name="updateprofile"),
    path('saveupdate/<int:dataid>/', views.saveupdate, name="saveupdate"),

    path('userview/', views.userview, name='userview'),
    path('expertview/', views.expertview, name='expertview'),
    path('chat_user/', views.chat_user, name="chat_user"),
    path('sendcomplain/', views.sendcomplain, name='sendcomplain'),
    path('savecomplain/', views.savecomplain, name='savecomplain'),
    path('managecomplain/', views.managecomplain, name='managecomplain'),
    path('my-view/', views.my_view, name='my_view'),
    path('viewhomeremedies/', views.viewhomeremedies, name='viewhomeremedies'),

    path('chat_bot/', views.chat_bot, name='chat_bot'),
    path('UserChatbot/', views.UserChatbot, name='UserChatbot'),

    path('diseasepredict/', views.diseasepredict, name='diseasepredict'),
    path('viewprediction/', views.viewprediction, name='viewprediction'),
]