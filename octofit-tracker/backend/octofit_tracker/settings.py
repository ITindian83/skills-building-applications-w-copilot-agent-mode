# Django settings for octofit_tracker project

# ...existing settings...

# MongoDB configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
    }
}

# Allow all hosts
ALLOWED_HOSTS = ['*']

# Enable CORS
INSTALLED_APPS += ['corsheaders']
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE
CORS_ALLOW_ALL_ORIGINS = True
