from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from Mvpapp.models import Family, Orphan, OrphanEducation, Subsidy, family_subsidy
from Mvpapp.serializers import FamilySerializer, OrphanSerializer, OrphanEducationSerializer, SubsidySerializer, FamilySubsidySerializer
from datetime import datetime
# Create your views here.
# pylint: disable=maybe-no-member


@csrf_exempt
def familyApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            families = Family.objects.all() 
            families_serializer = FamilySerializer(families, many=True)
            #print([families_serializer.data[i].get('cin') for i in range(0, len(families_serializer.data))])
            return JsonResponse(families_serializer.data, safe=False)
        else:
            fam = Family.objects.get(id=id)
            fam_serializer = FamilySerializer(fam)
            return JsonResponse(fam_serializer.data, safe=False)

    elif request.method == 'POST':
        family_data = JSONParser().parse(request)
        family_serializer = FamilySerializer(data=family_data)
        if family_serializer.is_valid():
            family_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        #print(family_serializer.errors)
        d = {}
        for i in family_serializer.errors.keys():
            d[i] = family_serializer.errors[i]
        return JsonResponse([str(k + ": " + v[0] + "\n") for k, v in d.items()], safe=False)
    elif request.method == 'PUT':
        family_data = JSONParser().parse(request)
        # print(family_data['id'])
        family = Family.objects.get(id=family_data['id'])
        family_serializer = FamilySerializer(family, data=family_data)
        if family_serializer.is_valid():
            family_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        d = {}
        for i in family_serializer.errors.keys():
            d[i] = family_serializer.errors[i]
        return JsonResponse([str(k + ": " + v[0] + "\n") for k, v in d.items()], safe=False)
    elif request.method == 'DELETE':
        family = Family.objects.get(id=id)
        family.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def orphanApi(request, id=0):
    if request.method == 'GET':
        orphans = Orphan.objects.all()
        orphans_serializer = OrphanSerializer(orphans, many=True)
        return JsonResponse(orphans_serializer.data, safe=False)

    elif request.method == 'POST':
        orphan_data = JSONParser().parse(request)
        orphan_serializer = OrphanSerializer(data=orphan_data)
        if orphan_serializer.is_valid():
            orphan_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        print(orphan_serializer.errors)
        d = {}
        for i in orphan_serializer.errors.keys():
            d[i] = orphan_serializer.errors[i]
        return JsonResponse([str(k + ": " + v[0] + "\n") for k, v in d.items()], safe=False)
    elif request.method == 'PUT':
        orphan_data = JSONParser().parse(request)
        # print(orphan_data['id'])
        orphan = Orphan.objects.get(id=orphan_data['id'])
        orphan_serializer = OrphanSerializer(orphan, data=orphan_data)
        if orphan_serializer.is_valid():
            orphan_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        d = {}
        for i in orphan_serializer.errors.keys():
            d[i] = orphan_serializer.errors[i]
        return JsonResponse([str(k + ": " + v[0] + "\n") for k, v in d.items()], safe=False)
    elif request.method == 'DELETE':
        orphan = Orphan.objects.get(id=id)
        orphan.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def subsidyApi(request, id=0):
    if request.method == 'GET':
        subsidies = Subsidy.objects.all()
        subsidies_serializer = SubsidySerializer(subsidies, many=True)
        print(subsidies)
        return JsonResponse(subsidies_serializer.data, safe=False)

    elif request.method == 'POST':
        subsidy_data = JSONParser().parse(request)
        subsidy_serializer = SubsidySerializer(data=subsidy_data)
        if subsidy_serializer.is_valid():
            subsidy_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        print(subsidy_serializer.errors)
        d = {}
        for i in subsidy_serializer.errors.keys():
            d[i] = subsidy_serializer.errors[i]
        return JsonResponse([str(k + ": " + v[0] + "\n") for k, v in d.items()], safe=False)
    elif request.method == 'PUT':
        subsidy_data = JSONParser().parse(request)
        print(subsidy_data)
        subsidy = Subsidy.objects.get(id=subsidy_data['id'])
        subsidy_serializer = SubsidySerializer(subsidy, data=subsidy_data)
        if subsidy_serializer.is_valid():
            subsidy_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        print(subsidy_serializer.errors)
        d = {}
        for i in subsidy_serializer.errors.keys():
            d[i] = subsidy_serializer.errors[i]
        return JsonResponse([str(k + ": " + v[0] + "\n") for k, v in d.items()], safe=False)
    elif request.method == 'DELETE':
        subsidy = Subsidy.objects.get(id=id)
        subsidy.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def orphaneducationApi(request, id=0):
    if request.method == 'GET':
        orphanseducation = OrphanEducation.objects.all()
        orphanseducation_serializer = OrphanEducationSerializer(
            orphanseducation, many=True)
        return JsonResponse(orphanseducation_serializer.data, safe=False)

    elif request.method == 'POST':
        orphaneducation_data = JSONParser().parse(request)
        orphaneducation_serializer = OrphanEducationSerializer(
            data=orphaneducation_data)
        if orphaneducation_serializer.is_valid():

            orphaneducation_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        # print(orphaneducation_serializer.errors)
        d = {}
        for i in orphaneducation_serializer.errors.keys():
            d[i] = orphaneducation_serializer.errors[i]
        return JsonResponse([str(k + ": " + v[0] + "\n") for k, v in d.items()], safe=False)
    elif request.method == 'PUT':
        orphaneducation_data = JSONParser().parse(request)
        orphaneducation = OrphanEducation.objects.get(
            id=orphaneducation_data['id'])
        orphaneducation_serializer = OrphanEducationSerializer(
            orphaneducation, data=orphaneducation_data)
        if orphaneducation_serializer.is_valid():
            orphaneducation_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        d = {}
        for i in orphaneducation_serializer.errors.keys():
            d[i] = orphaneducation_serializer.errors[i]
        return JsonResponse([str(k + ": " + v[0] + "\n") for k, v in d.items()], safe=False)
    elif request.method == 'DELETE':
        orphaneducation = OrphanEducation.objects.get(id=id)
        orphaneducation.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def familysubsidyApi(request, id=0):
    if request.method == 'GET':
        familysubsidies = family_subsidy.objects.all()
        familysubsidies_serializer = FamilySubsidySerializer(
            familysubsidies, many=True)
        return JsonResponse(familysubsidies_serializer.data, safe=False)

    elif request.method == 'POST':
        familysubsidy_data = JSONParser().parse(request)
        familysubsidy_serializer = FamilySubsidySerializer(
            data=familysubsidy_data)
        if familysubsidy_serializer.is_valid():

            familysubsidy_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        print(familysubsidy_serializer.errors)
        d = {}
        for i in familysubsidy_serializer.errors.keys():
            d[i] = familysubsidy_serializer.errors[i]
        return JsonResponse([str(k + ": " + v[0] + "\n") for k, v in d.items()], safe=False)
    elif request.method == 'PUT':
        familysubsidy_data = JSONParser().parse(request)
        familysubsidy = family_subsidy.objects.get(id=familysubsidy_data['id'])
        familysubsidy_serializer = FamilySubsidySerializer(
            familysubsidy, data=familysubsidy_data)
        if familysubsidy_serializer.is_valid():
            familysubsidy_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        d = {}
        for i in familysubsidy_serializer.errors.keys():
            d[i] = familysubsidy_serializer.errors[i]
        return JsonResponse([str(k + ": " + v[0] + "\n") for k, v in d.items()], safe=False)
    elif request.method == 'DELETE':
        familysubsidy = family_subsidy.objects.get(id=id)
        familysubsidy.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
