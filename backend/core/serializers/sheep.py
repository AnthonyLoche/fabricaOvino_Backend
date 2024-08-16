from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from backend.core.models import Sheep

from .category import CategorySerializer


class SheepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheep
        fields = ["id", "earringNumber", "breed", "category", "lots", "birthday", "sex", "teethQuantity", "lactating"]
        depth = 1


class SheepCreateNewbornSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheep
        fields = ["id", "earringNumber", "breed", "category", "lots", "birthday", "sex", "teethQuantity", "lactating"]
        depth = 1

class SheepDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    breed = serializers.CharField(source="breed.name", read_only=True)
    lots = serializers.CharField(source="lots.name", read_only=True)
    sex = serializers.SerializerMethodField()

    class Meta:
        model = Sheep
        fields = [
            "id",
            "earringNumber",
            "breed",
            "category",
            "lots",
            "births",
            "birthday",
            "sex",
            "teethQuantity",
            "pregnant",
            "lactating",
            "shearing",
        ]
        depth = 1

    def get_sex(self, obj) -> str:
        return _(obj.get_sex_display())