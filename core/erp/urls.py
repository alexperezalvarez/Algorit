from django.urls import path
from core.erp.views import myfierstview, mysecondview

app_name = 'erp'

urlpatterns = [
  path('uno/', myfierstview, name='uno'),
  path('dos/', mysecondview, name='dos'),
]