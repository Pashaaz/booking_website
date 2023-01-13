from rest_framework import serializers

from viewpoints.models import (
    HotelComment,
    CompanyComment,
    HotelRating,
    CompanyRating,
)


class HotelCommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = HotelComment
        fields = ('id', 'parent', 'comment_body', 'hotel', 'user', 'status')

        extra_kwargs = {
            'parent': {'required': False},
            'status': {'read_only': True},
        }


class CompanyCommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = CompanyComment
        fields = ('id', 'parent', 'comment_body', 'company', 'user', 'status')

        extra_kwargs = {
            'parent': {'required': False},
            'status': {'read_only': True},
        }


class HotelRatingSerializers(serializers.ModelSerializer):

    class Meta:
        model = HotelRating
        fields = ('id', 'rate', 'hotel', 'user')


class CompanyRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyRating
        fields = ('id', 'rate', 'company', 'user')
