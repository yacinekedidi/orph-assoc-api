from rest_framework import serializers
from Mvpapp.models import Family, Orphan, Subsidy, family_subsidy, OrphanEducation



class FamilySubsidySerializer(serializers.ModelSerializer):
    class Meta:
        model = family_subsidy
        fields = ('id',
                  'created_at',
                  'updated_at',
                  'show',
                  'subsidy_id',
                  'family_id',
                  'sub_amount')


class FamilySerializer(serializers.ModelSerializer):
    familySubsidy = FamilySubsidySerializer(many=True, read_only=True) 
    class Meta:
        model = Family
        fields = ('id',
                  'created_at',
                  'updated_at',
                  'show',
                  'cin',
                  'first_name',
                  'last_name',
                  'sex',
                  'birthdate',
                  'address',
                  'phone',
                  'health_insurance',
                  'job',
                  'income',
                  'home_status',
                  'home_owner',
                  'health_status',
                  'deceased_parent_name',
                  'cause_of_death',
                  'sponsor_name',
                  'family_status',
                  'familySubsidy')


class SubsidySerializer(serializers.ModelSerializer):
    subsidiesForFamilies = FamilySubsidySerializer(many=True, read_only=True)
    class Meta:
        model = Subsidy
        fields = ('id',
                  'created_at',
                  'updated_at',
                  'show',
                  'sub_type',
                  'title',
                  'description',
                  'price_unit',
                  'gender',
                  'age_min',
                  'age_max',
                  'status',
                  'amount',
                  'unit',
                  'subsidiesForFamilies')




class OrphanEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrphanEducation
        fields = ('id',
                  'created_at',
                  'updated_at',
                  'show',
                  'orphan_id',
                  'school',
                  'grade_year',
                  'success',
                  'score_1',
                  'score_2',
                  'score_3',
                  'score_final',
                  'updated',
                  'academic_year')

class OrphanSerializer(serializers.ModelSerializer):
    orphan_education = OrphanEducationSerializer(many=True, read_only=True)
    class Meta:
        model = Orphan
        fields = ('id',
                  'created_at',
                  'updated_at',
                  'show',
                  'family_id',
                  'first_name',
                  'last_name',
                  'sex',
                  'birthdate',
                  'hobbies',
                  'education_status',
                  'health_status',
                  'orphan_education')