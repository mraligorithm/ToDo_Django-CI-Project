from base import *
import os


# Installed App
INSTALLED_APPS += ('django_nose',)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR', '.')  # '.' /reporst
NOSE_ARGS = [
'--verbosity=2', # Verbose ouput
'--nologcapture', # dont out put log capture
'--with-coverage', # activate coverage report
'--cover-package=toDo', # coverage reports will apply to these packages
'--with-spec', # spec style tests
'--spec-color', #
'--with-xunit',
'--xunit-file=%s/unittests.xml' % TEST_OUTPUT_DIR, # /reports/utitledtests.xml
'--cover-xml', # produce XML coverage info
'--cover-xml-file=%s/coverage.xml' % TEST_OUTPUT_DIR, # /reports/utitledtests.xml
]

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'todobackend1'),
        'USER': os.environ.get('MYSQL_USER', 'toDo'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'password'),
        'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
        'PORT': os.environ.get('MYSQL_PORT', '3306'),
    }
}
