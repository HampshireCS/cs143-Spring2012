import os

def pathparts(p):
    # replace strings with proper
    if isinstance(p, str):
        p = p.replace('\\', '/').split('/')

    return p
    

class Resource(object):
    def __new__(cls, name, *a):
        mgr = ResourceManager()
        mgr.get_path()

        # make sure to build the class path up right
        r = cls.load(path)
        return 3

    @staticmethod
    def load(path):
        pass


class ResourceManager(object):
    _instance = None
    def __new__(cls, *a):
        if cls._instance is None:
            pygame.init()
            cls._instance = super(ResourceManager, cls).__new__(cls, *a)
        return cls._instance

    def set_resource_path(cls, s):
        import __main__


    def get_resource_path(cls, s):
        pass



__all__ = ["Resource", "ResourceManager"]
