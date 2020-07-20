from django.shortcuts import render
from rest_framework.decorators import APIView
from .models import Details
from .serializers import DetailSerializer
from rest_framework.response import Response
# Create your views here.



def homepage(request):
	return render(request,'customapi/homepage.html')




class DetailsListView(APIView):

	def get(self, request):
		details = Details.objects.all()
		serializer = DetailSerializer(details, many=True)
		serializer.data
		return Response(serializer.data)

