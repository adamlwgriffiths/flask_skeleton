from __future__ import absolute_import, print_function


def extract_ip_address(request):
    # http://stackoverflow.com/a/916157/1591957
    # http://www.grantburton.com/2008/11/30/fix-for-incorrect-ip-addresses-in-wordpress-comments/"HTTP_X_FORWARDED"
    for key in [
        'HTTP_CLIENT_IP',
        'HTTP_X_FORWARDED_FOR',
        'HTTP_X_FORWARDED'
        'HTTP_X_CLUSTER_CLIENT_IP'
        'HTTP_FORWARDED_FOR'
        'HTTP_FORWARDED'
    ]:
        value = request.headers.get(key)
        if value:
            # some values are comma-separated lists
            return value.split(',')[0]
    return request.remote_addr
