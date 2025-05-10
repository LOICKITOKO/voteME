from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Nominee, Vote
from .serializers import CategorySerializer, VoteSerializer
from rest_framework import status
from django.http import JsonResponse

@api_view(['GET'])
def all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_detail(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        return JsonResponse({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['POST'])
def vote(request):
    nominee_id = request.data.get('nominee_id')
    ip_address = request.META.get('REMOTE_ADDR')

    try:
        nominee = Nominee.objects.get(id=nominee_id)
    except Nominee.DoesNotExist:
        return JsonResponse({"error": "Nominee not found"}, status=status.HTTP_404_NOT_FOUND)

    # Empêcher les votes multiples par la même adresse IP
    if Vote.objects.filter(nominee=nominee, ip_address=ip_address).exists():
        return JsonResponse({"error": "You have already voted for this nominee."}, status=status.HTTP_400_BAD_REQUEST)

    # Créer un vote
    Vote.objects.create(nominee=nominee, ip_address=ip_address)

    return JsonResponse({"message": "Your vote has been registered!"}, status=status.HTTP_201_CREATED)
