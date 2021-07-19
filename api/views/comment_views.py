from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from ..models.comment import Comment
from ..serializers import CommentSerializer

class Comments(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CommentSerializer
    def get(self, request):
        """Index Request"""
        comments = Comment.objects.all()
        data = CommentSerializer(comments, many=True).data
        return Response({ 'comments': data })
    def post(self, request):
        """Create Request"""
        request.data['comments']['owner'] = request.user.id
        comment = CommentSerializer(data=request.data['comments'])
        if comment.is_valid():
            comment.save()
            return Response({ 'comments': comment.data }, status=status.HTTP_201_CREATED)
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show Request"""
        comment = get_object_or_404(Comment, pk=pk)
        data = CommentSerializer(comment).data
        return Response({ 'comments': data })
    def delete(self, request, pk):
        """Delete Request"""
        comment = get_object_or_404(Comment, pk=pk)
        if not request.user.id == comment.owner.id:
            raise PermissionDenied('You are unauthorized')
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def partial_update(self, request, pk):
        """Update Request"""
        comment = get_object_or_404(Comment, pk=pk)
        if not request.user.id == comment.owner.id:
            raise PermissionDenied('You are unauthorized')
        request.data['comment']['owner'] = request.user.id
        data = CommentSerializer(comment, data=request.data['comment'], partial=True)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
