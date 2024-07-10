from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

@register_snippet
class Template(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()

    panels = [
        FieldPanel("title"),
        FieldPanel("content"),
    ]

    def __str__(self):
        return self.title