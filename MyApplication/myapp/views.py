from django.forms import model_to_dict
from django.http import JsonResponse
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
        doctor = Doctor.objects.filter(id=request.query_params.get('doctor_id')).first()
        if doctor:
            timeSlots = list(doctor.timeslots_set.filter(status=False).values())
            return JsonResponse(timeSlots, safe=False)
        else:
            return Response(data={"code": status.HTTP_404_NOT_FOUND, "data": "", "message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        response = serializer.is_valid(raise_exception=True)
        if response.status_code == status.HTTP_200_OK:
            person = serializer.save(creator=request.user)
            res = json.loads(response.data)
            res['data'] = model_to_dict(person)
            return Response(data=res, status=status.HTTP_200_OK)

        return Response(data=json.loads(response.data), status=status.HTTP_400_BAD_REQUEST)

