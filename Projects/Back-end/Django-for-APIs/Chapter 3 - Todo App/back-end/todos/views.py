from rest_framework import generics 
from .models import Todo
from .serializers import TodoSerializer 

# Display all todos
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Display a single model instance
class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# In traditional Django views are used to customize what data to send to the templates. In Django REST Framework views do the same thing but for our serialized data.
