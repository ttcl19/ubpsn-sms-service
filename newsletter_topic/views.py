from django.http import Http404

# Create your views here.
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
import logging

from newsletter_topic.models import NewsletterTopic, NewsletterTopicMessage
from newsletter_topic.serializers import (
    NewsletterTopicSerializer,
    NewsletterTopicMessageSerializer,
)
logger = logging.getLogger(__name__)

class NewsletterTopicViewSet(viewsets.ModelViewSet):
    queryset = NewsletterTopic.objects.all()
    serializer_class = NewsletterTopicSerializer


class NewsletterTopicMessageViewSet(viewsets.ModelViewSet):
    queryset = NewsletterTopicMessage.objects.all()
    serializer_class = NewsletterTopicMessageSerializer
    # Get users subscribed, then call service
    def perform_create(self, serializer):
        logger.info(__name__)
