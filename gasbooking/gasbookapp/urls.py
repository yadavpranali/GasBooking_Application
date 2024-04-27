
from django.urls import path
from gasbookapp import views

urlpatterns = [
    path('index',views.base),
    path('home',views.home,name='home'),
    path('connection',views.connection,name='connection'),
    path('book',views.bookcylinder),
    path('bookhistory',views.bookinghistory,name='bookhistory'),
    path('connectioninfo',views.connectioninfo,name='connectioninfo'),
    path('delete_booking/<int:pk>',views.delete_booking,name='delete-booking'),
    path('delete_connection/<int:pk>',views.delete_connection,name='delete-connection'),
    path('update_connection/<rid>',views.update_connection,name='update-connection'),
    path('book/<int:pk>', views.book_cylinder_view, name='book-cylinder'),
    
]