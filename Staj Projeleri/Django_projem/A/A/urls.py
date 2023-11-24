from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('yourapp/', include('yourapp.urls')),
    # Diğer URL pattern'lerinizi buraya ekleyebilirsiniz.
]
