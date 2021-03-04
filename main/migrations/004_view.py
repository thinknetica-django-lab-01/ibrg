
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210304_2253'),
    ]

    sql = """
      CREATE OR REPLACE VIEW user_advert AS
      SELECT obj.id as id, u.id as user_id, u.username, obj.advert_title as title, obj.description as description, obj.advert_category AS tags
      FROM main_advert as obj
      INNER JOIN auth_user AS u on u.id = obj.advert_owner_id
    """

    operations = [
        migrations.RunSQL("""DROP VIEW IF EXISTS user_advert """),
        migrations.RunSQL(sql)
    ]
