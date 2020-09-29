from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin2/', admin.site.urls),
    path('stocks/', include('stocks.urls')),
    path('', include('pages.urls'))
]