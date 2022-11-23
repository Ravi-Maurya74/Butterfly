from django.urls import path
from api import views

urlpatterns = [
    path('identify/<int:pk>', views.IdentifyUserApi.as_view()),
    path('detail/<int:pk>', views.UserDetailApi.as_view()),
    path('create/', views.NewUserApi.as_view()),
    path('idemail/<str:user_email>', views.IdentifyUserEmailApi.as_view()),
    path('getall/', views.GetAllUsersApi.as_view()),
    path('postdetail/<int:pk>', views.PostDetailApi.as_view()),
    path('homepageposts/', views.homePagePosts),
    path('likepost/', views.likePost),
    path('dislikepost/', views.dislikePost),
    path('newpost/', views.NewPostApi.as_view()),
    path('bookmark/', views.bookmarkPost),
    path('unmark/', views.unmarkPost),
    path('addfollower/', views.followuser),
    path('removefollower/', views.unfollowuser),
    path('newreply/', views.NewReplyApi.as_view()),
    path('searchuser/', views.search_user),
    path('deletepost/<int:pk>', views.DeletePostApi.as_view()),
    path('getreplies/', views.getpostreplies),
]
