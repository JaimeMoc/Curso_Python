from django.http import JsonResponse
from datetime import datetime

def get_datetime(request):
   now = datetime.now()
   response = {"datetime" : now}
   return JsonResponse(response)