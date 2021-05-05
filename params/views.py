from django.shortcuts import render, get_object_or_404
from params.models import *


def testcase_list(request):
    testcase_list = TestCase.objects.all().order_by("instance")
    context = {
        'PAGE_TITLE': "TestCases",
        'testlist': testcase_list,
    }
    return render(request, 'params/testcase_list.html', context)


def testcase_detail(request, test_id):
    testcase = get_object_or_404(TestCase, id=test_id)
    tags = testcase.tags.all()
    chekflow_params = CheckFlowParams.objects.filter(test_case=testcase)
    compare_params = CompareParams.objects.filter(test_case=testcase)
    context = {
        'PAGE_TITLE': testcase.name,
        'testcase': testcase,
        'tags': tags,
        'checkflowparams': chekflow_params,
        'compare_params': compare_params,
    }
    return render(request, 'params/testcase_detail.html', context)


def runscript_list(request):
    params = RunScriptParams.objects.order_by('key').all()
    context = {
        'PAGE_TITLE': "Paramètres RUN SCRIPT",
        'params': params,
    }
    return render(request, 'params/runscript_list.html', context)


def runscript_detail(request, key):
    params = get_object_or_404(RunScriptParams, key=key)
    context = {
        'PAGE_TITLE': "RUN SCRIPT : {}".format(params.key),
        'params': params,
    }
    return render(request, 'params/runscript_detail.html', context)
