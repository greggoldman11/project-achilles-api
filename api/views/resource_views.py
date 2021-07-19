from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from ..models.resource import Resource
from ..serializers import ResourceSerializer

# Create views(endpoints)
# Create a class for all Resources
class Resources(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ResourceSerializer
    def get(self, request):
        """Index Request"""
        resources = Resource.objects.all()
        data = ResourceSerializer(resources, many=True).data
        return Response({ 'resources': data })
    def post(self, request):
        """Create Request"""
        request.data['resource']['owner'] = request.user.id
        resource = ResourceSerializer(data=request.data['resource'])
        if resource.is_valid():
            resource.save()
            return Response({ 'resource': resource.data }, status=status.HTTP_201_CREATED)
        return Response(resource.errors, status=status.HTTP_400_BAD_REQUEST)
  # Create a class for a specific Resource
class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show Request"""
        resource = get_object_or_404(Resource, pk=pk)
        data = ResourceSerializer(resource).data
        return Response({ 'resource': data })
    def delete(self, request, pk):
        """Delete Request"""
        resource = get_object_or_404(Resource, pk=pk)
        if not request.user.id == resource.owner.id:
            raise PermissionDenied('You are unauthorized')
        resource.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def partial_update(self, request, pk):
        """Update Request"""
        resource = get_object_or_404(Resource, pk=pk)
        if not request.user.id == resource.owner.id:
            raise PermissionDenied('You are unauthorized')
        request.data['resource']['owner'] = request.user.id
        data = ResourceSerializer(resource, data=request.data['resource'], partial=True)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
