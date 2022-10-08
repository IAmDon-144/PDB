from rest_framework import serializers
from .models import PBS, Zonal, SubZonal, ComplainCenter, Fider, Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"


class FiderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fider
        fields = "__all__"


class ComplainCenterSerializer(serializers.ModelSerializer):
    child = FiderSerializers(many=True, read_only=True)
    report = ReportSerializer(many=True, read_only=True)

    class Meta:
        model = ComplainCenter
        fields = ["id", "name", "type", "child", "report"]


class SubZonalSerializers(serializers.ModelSerializer):
    child = ComplainCenterSerializer(many=True, read_only=True)

    class Meta:
        model = SubZonal
        fields = ["id", "name", "type", "child"]


class ZonalSerializers(serializers.ModelSerializer):
    child = SubZonalSerializers(many=True, read_only=True)

    class Meta:
        model = Zonal
        fields = ["id", "name", "type", "child"]


class PBS_Serializer(serializers.ModelSerializer):
    child = ZonalSerializers(many=True, read_only=True)

    class Meta:
        model = PBS
        fields = ["id", "name", "type", "child"]
