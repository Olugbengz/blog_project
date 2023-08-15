from django.db import migrations
from blog_api.user.models import CustomUser



class Migration(migrations.Migration):
	def seed_data(apps, schema_editor):
		user = CustomUser(name='olugbenga',
			email='olugbengz@mail.com',
			is_staff=True,
			is_superuser=True,
			)
		user.set_password('olugbengz@1')
		user.save()
	
	operations = [
		migrations.RunPython(seed_data),
	]

	dependencies = [
	    
	]