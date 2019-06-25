from django.conf.urls import url, include
from django.contrib import admin
from Wallet.views import router,diposit_view ,transaction_view
from django.contrib.auth.views import login, logout
#from rest_framework.schemas import get_schema_view
#from rest_framework.documentation import include_docs_urls
#from rest_framework.urlpatterns import format_suffix_patterns
#from Wallet import views

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^xyz/', diposit_view, name='deposit'),
    url(r'^transfer/',transaction_view, name='transfer'),
]
