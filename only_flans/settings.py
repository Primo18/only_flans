import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


LANGUAGE_CODE = "en-us"

LANGUAGES = [
    ("en", "English"),
    ("es", "Spanish"),
    # Agrega otros idiomas según sea necesario
]

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7=1#t$oo3%zucucu93yp4@$sz-*t6=s14u8jcdsjgl^)$teej6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "onlyflans-production.up.railway.app",
    "web-production-c1cd1.up.railway.app",
]
CSRF_TRUSTED_ORIGINS = [
    "https://onlyflans-production.up.railway.app",
    "https://web-production-c1cd1.up.railway.app",
]


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "jazzmin",
    "widget_tweaks",
    "web",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "only_flans.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Configuración de autenticación
LOGIN_REDIRECT_URL = "/welcome/"
LOGOUT_REDIRECT_URL = "/"


WSGI_APPLICATION = "only_flans.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "es-cl"

TIME_ZONE = "America/Santiago"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


JAZZMIN_SETTINGS = {
    "site_title": "Only Flans Admin",
    "site_header": "Only Flans",
    "site_logo": "/web/images/flan.png",
    "site_favicon": "/web/images/favicon.png",
    "welcome_sign": "Bienvenido a Only Flans Admin",
    "topmenu_links": [
        {"name": "Inicio", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"app": "web"},
    ],
    "usermenu_links": [
        {
            "name": "Soporte",
            "url": "https://github.com/farridav/django-jazzmin/issues",
            "new_window": True,
        },
        {"model": "auth.user"},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": ["auth", "web"],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "web.Flan": "fas fa-cake",
        "web.ContactForm": "fas fa-envelope",
    },
    "related_modal_active": True,
    "custom_css": None,
    "custom_js": None,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "language_chooser": True,  # Habilitar selector de idioma
    "show_ui_builder": True,  # Habilitar el personalizador de UI
}
