from urllib.parse import urlparse


# get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


def get_homepage_name(url):
    try:
        result = str(get_domain_name(url))
        return result[:-4]

    except:
        return ''
