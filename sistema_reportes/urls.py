from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import handler404,url
from django.conf.urls.static import static

from apps.registration.urls import registrationpatterns
from apps.investigadores.urls import investigadorespatterns
from apps.biblioteca.urls import bibliotecapatterns
from apps.administradores.urls import administradorespatterns
from apps.metricas.urls import metricaspatterns
from apps.reporteSNI.urls import reporteSNIpatterns



urlpatterns = [
    path('',include('apps.core.urls')),
    path('',include(investigadorespatterns)),
    path('',include(bibliotecapatterns)),
    path('',include(administradorespatterns)),
    path('',include(metricaspatterns)),
    path('',include(reporteSNIpatterns)),
    path('admin/', admin.site.urls),

    # Paths de Auth
    path('accounts/',include('django.contrib.auth.urls')),
    path('',include(registrationpatterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.core.views.error'