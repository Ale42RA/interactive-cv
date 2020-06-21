from django.contrib import admin

from .models import Me
from .models import Equipment
from .models import Skillset
from .models import WorkExp
from .models import Education
from .models import Attribute
from .models import Like



admin.site.register(Me)
admin.site.register(Equipment)
admin.site.register(Skillset)
admin.site.register(WorkExp)
admin.site.register(Education)
admin.site.register(Attribute)
admin.site.register(Like)
