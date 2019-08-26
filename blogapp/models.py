from django.db import models

class Blog(Model.models):
    title = CharField(max_length =100)
    
    text = CharField(max_length = 100)
    
    created_at = 