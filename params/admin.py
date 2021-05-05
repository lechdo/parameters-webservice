from django.contrib import admin
from .models import *

# model registration in the admin mode
admin.site.register(Tag)
admin.site.register(TestCase)
admin.site.register(Server)
admin.site.register(CheckFlowParams)
admin.site.register(CleanFlowParams)
admin.site.register(DeclareFlowParams)
admin.site.register(ExtractTableParams)
admin.site.register(LoadTableParams)
admin.site.register(RunOracleActionParams)
admin.site.register(RunScriptParams)
admin.site.register(UpdateStateIdParams)
admin.site.register(CompareParams)



