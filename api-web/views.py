from rest_framework.response import Response
from rest_framework.decorators import api_view
from entity.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def editItem(request, item_id):
    try:
        # Retrieve the item instance from the database
        item_instance = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)

    serializer = ItemSerializer(item_instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteItem(request, item_id):
    try:
        item_instance = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)

    item_instance.delete()
    return Response({"message": "Item deleted successfully"})
