from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tours.views import MainView, DepartureView, TourView

urlpatterns = [
                  path('', MainView.as_view(), name='tours'),
                  path('departure/<str:city>/', DepartureView.as_view(), name='departure'),
                  path('tour/<int:id>', TourView.as_view(), name='tour'),

                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
