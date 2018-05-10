
def disable_cache(response):
    response.headers.add('Cache-Control', 'no-cache, no-store, max-age=0')
    return response


def cache_response(response, max_age):
    if max_age is not None:
        response.headers.add('Cache-Control', 'public, max-age=' + str(max_age))
    return response
