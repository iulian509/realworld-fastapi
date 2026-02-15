# Jetbase Configuration
# Update the sqlalchemy_url with your database connection string.

from realworld.core.config import settings

sqlalchemy_url = str(settings.database_url)
