from django_cassandra_engine.rest import serializers
from blog.models import Post


class PostSerializer(serializers.DjangoCassandraModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'description', 'content'
        ]
        read_only_fields = ['id']
