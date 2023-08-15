import nested_admin
from django.contrib import admin

from Question.models import Option, Question, Category, FinalResult, Questionnaire, ContactUs


# class QuestionAdmin(admin.ModelAdmin):
#    list_display = ['question_text', 'writer', 'total_score']

#    def total_score(self, obj):
#        return sum(option.score for option in obj.options.all())

#    total_score.short_description = 'Total Score'

# admin.site.register(Question, QuestionAdmin)


class OptionInline(nested_admin.NestedTabularInline):
    model = Option
    extra = 1
    classes = ['collapse']


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [OptionInline]
    extra = 1
    classes = ['collapse']
    #fieldsets = [
        #('Category Name', {'fields': ['category']},),
        #('Question Text', {'fields': ['question_text'], 'classes': ['collapse']})

    #]


class CategoryAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]
    fieldsets = [
        ('Survey Name', {'fields': ['writer']}),
        ('Questionnaire Name', {'fields': ['questionnaire']}),
        ('Category Name', {'fields': ['category_name', 'importance', 'first_text', 'second_text', 'third_text', 'fourth_text'], 'classes': ['collapse']},)
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(FinalResult)
admin.site.register(Questionnaire)
admin.site.register(ContactUs)
