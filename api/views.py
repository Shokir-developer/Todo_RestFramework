from api.serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todos.models import Todo

@api_view(['GET'])
def indexApi(request):
    items = Todo.objects.all()
    serializer = TodoSerializer(items, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def add(request):
    items = Todo.objects.all()
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
    items = Todo.objects.get(id=pk)
    serializer = TodoSerializer(items, many=False)

    return Response(serializer.data)
