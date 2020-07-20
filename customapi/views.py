from django.shortcuts import render
from rest_framework.decorators import APIView
from .models import Details
from .serializers import DetailSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



def homepage(request):
	return render(request,'customapi/homepage.html')




class DetailsListView(APIView):

	def get(self, request):
		details = Details.objects.all()
		serializer = DetailSerializer(details, many=True)
		serializer.data
		return Response(serializer.data)

	def post(self, request):
		serializer = DetailSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED )
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class DetailView(APIView):

	def get(self, request, id):
		detail = Details.objects.get(id = id)
		serializer = DetailSerializer(detail, many=False)
		serializer.data
		return Response(serializer.data)


