from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class PersonView(APIView):
    def get_serializer_context(self):
        context = {'request': self.request}
        return context

    def get(self, request):
        person = Person.objects.filter(id=request.query_params.get('roll_number')).first()
        # res['data'] = model_to_dict(person)
        return Response(data=model_to_dict(person), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        response = serializer.is_valid(raise_exception=True)
        if response.status_code == 200:
            person = serializer.save(creator=request.user)
            res = json.loads(response.data)
            res['data'] = model_to_dict(person)
            return Response(data=res, status=status.HTTP_200_OK)

        return Response(data=json.loads(response.data), status=status.HTTP_400_BAD_REQUEST)
