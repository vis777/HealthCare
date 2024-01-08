from Backend import views
from django.urls import path
urlpatterns = [
    path('adminpage/', views.adminpage, name="adminpage"),
    path('expertpage/', views.expertpage, name="expertpage"),
    path('saveexpert/', views.saveexpert, name="saveexpert"),
    path('manageexpert/', views.manageexpert, name="manageexpert"),
    path('editexpert/<int:dataid>/', views.editexpert, name="editexpert"),
    path('updateexpert/<int:dataid>/', views.updateexpert, name="updateexpert"),
    path('deleteexpert/<int:dataid>/', views.deleteexpert, name="deleteexpert"),

    path('diseasepage/', views.diseasepage, name="diseasepage"),
    path('savedisease/', views.savedisease, name="savedisease"),
    path('managedisease/', views.managedisease, name="managedisease"),
    path('deletedisease/<int:dataid>/', views.deletedisease, name="deletedisease"),

    path('replypage/<int:id>', views.replypage, name="replypage"),
    path('reply/', views.replypage, name="replypage"),
    path('savereply/', views.savereply, name="savereply"),

    path('complaintpage/', views.complaintpage, name="complaintpage"),
    path('blkunblk/', views.blkunblk, name="blkunblk"),
    path('toggle_block_status/<int:dataid>/', views.toggle_block_status, name='toggle_block_status'),
    path('blockexpert/<int:dataid>/', views.blockexpert, name="blockexpert"),
    path('unblockexpert/<int:dataid>/', views.unblockexpert, name="unblockexpert"),

    path('datasetpage/', views.datasetpage, name="datasetpage"),
    path('savedataset/', views.savedataset, name="savedataset"),
    path('managedataset/', views.managedataset, name="managedataset"),
    path('deletedataset/<int:dataid>/', views.deletedataset, name="deletedataset"),

    path('homeremedypage/', views.homeremedypage, name="homeremedypage"),
    path('savehomeremedies/', views.savehomeremedies, name="savehomeremedies"),
    path('managehomeremedies/', views.managehomeremedies, name="managehomeremedies"),
    path('deletehomeremedies/<int:dataid>/', views.deletehomeremedies, name="deletehomeremedies"),

    path('admin_login/', views.admin_login, name="admin_login"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),

]