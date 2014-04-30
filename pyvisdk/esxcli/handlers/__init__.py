
def import_handler(name):
    from pyvisdk.utils import camel_to_under
    from pyvisdk.brownie_importing import import_string
    return import_string('{}.ha_cli_handler_{}.{}'.format(__name__, camel_to_under(name), name))
