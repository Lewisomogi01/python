from rest_framework import serializers
from book_api.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'number_of_pages', 'publish_date', 'quantity']
        read_only_fields = ['id']

    # Optional: Add validation for specific fields
    def validate_number_of_pages(self, value):
        if value < 0:
            raise serializers.ValidationError("Number of pages cannot be negative.")
        return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value
    
    def update(self, instance, data):
        instance.title = data.get('title',instance.title)
        instance.number_of_pages= data.get('number_of_pages',instance.number_of_pages)
        instance.publish_date = data.get('publish_date ',instance.publish_date ) 
        instance.quantity = data.get('quantity',instance.quantity)
        
        instance.save()
        return instance
        
        
        
        
        
        
        

