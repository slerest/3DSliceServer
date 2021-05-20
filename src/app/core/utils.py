from core.settings import settings

def get_queries(name_queries):
    with open(settings.path_queries + name_queries + '.sql') as f:
        return f.read()

#def decode_token(token):
