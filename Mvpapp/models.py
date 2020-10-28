from django.db import models

# Create your models here.
gender = (
    ("male", "male"),
    ("female", "female"),
)
class Family(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)
    cin = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20, choices=gender, default="male")
    birthdate = models.DateField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    health_insurance = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    income = models.IntegerField()
    home_status = models.CharField(max_length=20)
    home_owner = models.CharField(max_length=40)
    health_status = models.CharField(max_length=100) 
    deceased_parent_name = models.CharField(max_length=50)
    cause_of_death = models.CharField(max_length=100)
    sponsor_name = models.CharField(max_length=40, null=True)
    family_status = models.CharField(max_length=50)


class Orphan(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)
    family_id = models.ForeignKey(Family, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20, choices=gender, default="male")
    birthdate = models.DateField()
    hobbies = models.CharField(max_length=200, null=True, blank=True)
    education_status = models.CharField(max_length=20)
    health_status = models.CharField(max_length=200)



class Subsidy(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)
    sub_type = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    price_unit = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=gender, null=True, blank=True)
    age_min = models.CharField(max_length=3, null=True, blank=True)
    age_max = models.CharField(max_length=3, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    amount = models.IntegerField()
    unit = models.CharField(max_length=20, null=True, blank=True)


class OrphanEducation(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)
    PRESCHOOL = 'PRE'
    ONE = '1'
    TWO = '2'
    Three = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    ELEVEN = '11'
    TWELVE = '12'
    THIRTEEN = '13'
    UNIVERSITY = 'UNI'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (PRESCHOOL, 'Preschool'),
        (ONE, 'First'),
        (TWO, 'Second'),
        (Three, 'Third'),
        (FOUR, 'Fourth'),
        (FIVE, 'Fifth'),
        (SIX, 'SIXth'),
        (SEVEN, 'Seventh'),
        (EIGHT, 'Eighth'),
        (NINE, 'Ninth'),
        (TEN, 'Tenth'),
        (ELEVEN, 'Eleventh'),
        (TWELVE, 'Twelfth'),
        (THIRTEEN, 'Thirteenth'),
        (UNIVERSITY, 'University'),
        (GRADUATE, 'Graduate')
    ]
    orphan_id = models.ForeignKey(Orphan, on_delete=models.CASCADE, related_name="orphan_education", null=True)
    school = models.CharField(max_length=20)
    grade_year = models.CharField(
        max_length=3, choices=YEAR_IN_SCHOOL_CHOICES, null=False)
    success = models.BooleanField(null=True, blank=True)
    score_1 = models.CharField(max_length=20, null=True, blank=True)
    score_2 = models.CharField(max_length=20, null=True, blank=True)
    score_3 = models.CharField(max_length=20, null=True, blank=True)
    score_final = models.CharField(max_length=20, null=True, blank=True)
    updated = models.CharField(max_length=10, null=True, blank=True)
    academic_year = models.CharField(max_length=5)
    class Meta:
        unique_together = ("orphan_id", "academic_year")




class family_subsidy(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)
    family_id = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="familySubsidy", null=True)
    subsidy_id = models.ForeignKey(Subsidy, on_delete=models.CASCADE, related_name="subsidiesForFamilies", null=True)
    sub_amount = models.IntegerField(default=0)
    
