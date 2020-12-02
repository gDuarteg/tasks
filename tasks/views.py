from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tasks.serializer import TaskSerializer
from tasks.models import Task
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(["GET"])
def get_all_tasks(request):
    data = TaskSerializer(Task.objects.all(), many=True)
    return JsonResponse(data.data, safe=False)

@api_view(["GET"])
def get_task(request):
    try:
        title = JSONParser().parse(request)['title']
        data = TaskSerializer(Task.objects.filter(title=title), many=True)
        return JsonResponse(data.data, safe=False)
    except Task.DoesNotExist:
        return HttpResponse("ERRO: Task Not Exist")

@api_view(["POST"])
def create_task(request):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)

@api_view(["DELETE"])
def delete_task(request):
    try:
        title = JSONParser().parse(request)['title']
        Task.objects.filter(title=title).delete()
    except Task.DoesNotExist:
        return HttpResponse("Task nao encontrada")
    return HttpResponse("Task deletada")

@api_view(["DELETE"])
def delete_all_tasks(request):
    Task.objects.all().delete()
    return HttpResponse("Tasks deletadas")
