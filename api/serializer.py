from . import models
from rest_framework import serializers
from django.db.models import Sum

class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Sponsor
        fields=('full_name',
                'phone_number',
                'organization_name',
                'amount',
                'type',)

        extra_kwargs={
            "id":{"read_only":True}
        }

    def validate(self, attrs):
        type=attrs.get("type")
        org_name=attrs.get("organization_name")
        if type == "physical"  and org_name :
                raise serializers.ValidationError(detail={"message": "jismoniy shaxs uchun organization nomiga ega  emas"})
        if type == "legal" and  not  org_name :
            raise serializers.ValidationError(detail={"error": "yuridik shaxs uchun organization nomi kiritish shart "})

        return attrs

class SponsorDatailSerializer(serializers.ModelSerializer):
    sponsor_amount=serializers.SerializerMethodField()
    def get_sponsor_amount(self,obj):
        a= obj.student_sponsors.aggregate(Sum('amount'))

        return a['amount__sum'] if a["amount__sum"] else 0

    class Meta:
        model=models.Sponsor
        fields=("id",
            "full_name",
                "phone_number",
                "amount",
                "created_at",
                "status",
                "sponsor_amount")


class SponsorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Sponsor
        fields="__all__"



class SponsorStudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.StudentSponsor
        fields="__all__"


    def create(self,validated_data):
        amount=validated_data.get("amount")
        student=validated_data.get("student")
        sponsor=validated_data.get("sponsor")

       # talabaga ajratiladigan pul miqdori oshib ketmasligi kerak
        total_amount=sum(models.StudentSponsor.objects.filter(student=student).values_list("amount",flat=True))

        if total_amount+amount>student.contract:
            raise serializers.ValidationError(detail={
                "error":f"Siz eng ko`pi bilan {student.contract-total_amount} qo`sha olasiz"
            })
        if total_amount+amount<sponsor.amount:
            raise serializers.ValidationError(detail={
                "error":f"Sponsor {sponsor.amount-student.contract}  ziyod pul qushmoqdasiz"
            })
        if amount>sponsor.amount:
            raise serializers.ValidationError(detail={
                "error":f"Sponsor{sponsor.amount} berilgan so`mma sizda shuncha pul yetarli emas"
            })


        return super().create(validated_data)



class StudentSerializer(serializers.ModelSerializer):
    student_amount=serializers.SerializerMethodField(method_name="total_student_amount")
    def total_student_amount(self,obj):
        result =sum(models.StudentSponsor.objects.filter(student=obj).values_list('amount',flat=True))

        return result




    class Meta:
        model=models.Student
        fields=("id",
                "full_name",
                "contract",
                "degree",
                "university",
                "student_amount",)


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields=("full_name",
                "contract",
                "degree",
               "university",
                )
        extra_kwargs = {
            "id": {"read_only": True}
        }


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields="__all__"


class StundentSponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.StudentSponsor
        fields=("full_name",
                "amount",)





