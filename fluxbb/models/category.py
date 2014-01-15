from django.db import models
from fluxbb import FLUXBB_PREFIX


class Category(models.Model):
    """
    FluxBB Category

    Model Fields:
        id (int): Auto incrementing primary key for the model
        cat_name (str): Name of the category
        disp_position (int): Positon of the category in relation to the others
    """
    id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=80, default="New Category")
    disp_position = models.IntegerField(max_length=10, default=0)

    class Meta:
        app_label = 'fluxbb'
        db_table = FLUXBB_PREFIX + 'categories'
