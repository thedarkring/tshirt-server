from django.views import View
from django.shortcuts import render

class DashboardView(View):

    def __init__(self):
        print("init dashboard")

    def get(self, request):
        context = dict()
        return render(request, 'index.html', context)