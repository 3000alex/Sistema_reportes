from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import handler404,url
from django.conf.urls.static import static

from registration.urls import registrationpatterns
from investigadores.urls import investigadorespatterns
from biblioteca.urls import bibliotecapatterns
from administradores.urls import administradorespatterns
from metricas.urls import metricaspatterns

handler404 = 'core.views.error'

urlpatterns = [
    path('',include('core.urls')),
    path('reportes/',include(investigadorespatterns)),
    path('reportes/',include(bibliotecapatterns)),
    path('reportes/',include(administradorespatterns)),
    path('reportes/',include(metricaspatterns)),
    path('admin/', admin.site.urls),

    # Paths de Auth
    path('accounts/',include('django.contrib.auth.urls')),
    path('',include(registrationpatterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
