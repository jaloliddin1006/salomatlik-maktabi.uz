from django.db import models
from ckeditor.fields import RichTextField
from apps.common.models import BaseModel
from apps.formula.utils import get_function_variables


CODE_DEFOULT = """def solution(a):
    # Write your formula here
    result = a ** 2
    return result
"""

FORMULA_DEFAULT = "<p>a<sup>2</sup></p>"


class Formula(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name='Formula Name')
    image = models.ImageField(upload_to='formula/')
    variables = models.JSONField(null=True, blank=True, verbose_name='Used Variables')
    formula = RichTextField(default=FORMULA_DEFAULT, verbose_name='Math Formula')
    code = models.TextField(default=CODE_DEFOULT, verbose_name='Python Code')
    formula_img = models.ImageField(upload_to='formula/', null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.code:
            variables = get_function_variables(self.code)
            self.variables = variables
        super().save(*args, **kwargs)
