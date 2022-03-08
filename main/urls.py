from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings

from main.views import AdmissionViewSet,\
    ClinicianAssignedPatientsViewSet,\
    ClinicianStatAPIView,\
    PatientViewSet, PrescriptionViewSet,\
    ReceptionistPatientView, ReceptionistStatAPIView,\
    ReferralViewSet, UserViewSet, WardViewSet,\
    ClinicianInfoViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'users', UserViewSet)
router.register(r'referrals', ReferralViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'wards', WardViewSet)
router.register(r'admissions', AdmissionViewSet),
router.register(r'clinicians',
                ClinicianInfoViewSet,
                'clinician')
router.register(r'receptionist-patients',
                ReceptionistPatientView,
                'registered-patient')
router.register(r'assigned-patients',
                ClinicianAssignedPatientsViewSet,
                basename='assigned-patient')

schema_view = get_schema_view(
    openapi.Info(
        title='LiveUp API',
        default_version='v1',
        description='RESTFUL API for LiveUp',
        contact=openapi.Contact(email=settings.FROM_EMAIL),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = [
    path('browsable-api-auth/', include('rest_framework.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('', include(router.urls)),
    path('receptionists/stats/', ReceptionistStatAPIView.as_view()),
    path('medics/stats/', ClinicianStatAPIView.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
]
