from django.contrib import admin
from matrix.models import Tactic, Platform, DataSource, Technique, Note, SigmaRule, LogSource


#admin.site.register(Tactic)
admin.site.register(Platform)
admin.site.register(DataSource)
#admin.site.register(Technique)
#admin.site.register(Note)
#admin.site.register(SigmaRule)
admin.site.register(LogSource) 

# Define Technique admin class
class TechniqueAdmin(admin.ModelAdmin):
    list_display = ('technique_id','technique_name','created','modified')

# Register the Technique admin class with the associated model
admin.site.register(Technique, TechniqueAdmin)

# Define Tactic admin class
class TacticAdmin(admin.ModelAdmin):
    list_display = ('tactic_id','tactic_name','tactic_description','tactic_url')

# Register the Tactic admin class with the associated model
admin.site.register(Tactic, TacticAdmin)

# Define Sigma admin class
class SigmaRuleAdmin(admin.ModelAdmin):
    list_display = ('rule_name',
                    'rule_file',
                    'date',
		    'detection_created')

# Register the SigmaRule admin class with the associated model
admin.site.register(SigmaRule, SigmaRuleAdmin)

# Define Note admin class
class NoteAdmin(admin.ModelAdmin):
    list_display = ('technique','date','note')

# Register the Note admin class with the associated model
admin.site.register(Note, NoteAdmin)

