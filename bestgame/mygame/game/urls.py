from django.conf.urls import url,include

urlpatterns = [
    url(r'^$', 'game.views.signin'),
    url(r'^login_user/', 'game.views.userchoise'),
    url(r'^choise/(?P<character_name>[\w-]+)','game.views.choose'),
    
    ]