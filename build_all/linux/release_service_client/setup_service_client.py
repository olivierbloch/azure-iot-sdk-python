from setuptools import setup, Distribution
import sys

class PlatformError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

_long_description=()

try:
    if sys.version_info < (2, 7):
        raise PlatformError("Require Python 2.7 or greater")
    if sys.version_info >= (3, 0) and sys.version_info < (3, 4):
        raise PlatformError("Require Python 3.4 or greater")
except PlatformError as e:
    sys.exit(e.value)

try:
    from iothub_service_client import iothub_service_client
    _version = iothub_service_client.__version__
except Exception as e:
    sys.exit(e)

setup(
    name='azure_iothub_service_client',
    version=_version+'.0', # using version of actual c client release
    description='IoT Hub Service Client Library',
    license='Apache Software License',
    url='https://github.com/Azure/azure-iot-sdk-python/tree/master/python/service',
    author='aziotclb',
    author_email='aziotclb@microsoft.com',
    long_description='IoT Hub Service Client Library for Python 2.7 and 3.6 - iothub_service_client.so',
    packages=['iothub_service_client'],
    classifiers=[
        'Environment :: Linux',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'],
    package_data={
        'iothub_service_client': ['__init__.py','iothub_service_client.so'],
    },
    distclass=BinaryDistribution
) 
