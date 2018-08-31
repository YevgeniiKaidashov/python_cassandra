import uuid

from cassandra.cqlengine import columns
from django_cassandra_engine import models


class Post(models.DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid1)

    title = columns.Text(max_length=255, required=True)
    description = columns.Text(max_length=255, default='')
    content = columns.Text(default='')
