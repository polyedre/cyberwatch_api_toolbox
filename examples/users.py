"""Example: Get all users and their attributes"""

import os
from configparser import ConfigParser
from cbw_api_toolbox.cbw_api import CBWApi

CONF = ConfigParser()
CONF.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'api.conf'))
CLIENT = CBWApi(CONF.get('cyberwatch', 'url'), CONF.get('cyberwatch', 'api_key'), CONF.get('cyberwatch', 'secret_key'))

FILTER = {
    "auth_provider": "" #used to filter users with "auth_provider" (local_password or ldap)
}

CLIENT.users(FILTER)
