from django.shortcuts import render
from facepy import GraphAPI
import urllib
from nothing.settings import FACEBOOK_APPLICATION_ID, FACEBOOK_APPLICATION_SECRET_KEY
from nothing.settings import FACEBOOK_APPLICATION_DOMAIN, FACEBOOK_APPLICATION_NAMESPACE
from nothing.settings import FACEBOOK_APPLICATION_INITIAL_PERMISSIONS


def authorize_application(request):
    
    query = {
        'client_id': FACEBOOK_APPLICATION_ID,
        'redirect_uri': 'http://%s/%s' % (FACEBOOK_APPLICATION_DOMAIN, FACEBOOK_APPLICATION_NAMESPACE),
    }

    query['scope'] = ', '.join(FACEBOOK_APPLICATION_INITIAL_PERMISSIONS)

    return render(
        request = request,
        template_name = 'authorize_application.html',
        dictionary = {
            'url': 'https://www.facebook.com/dialog/oauth?%s' % urllib.urlencode(query)
        },
        status = 401
    )



def get_token(request):
    
    code = request.GET.get('code', '')

    query = {
        'client_id': FACEBOOK_APPLICATION_ID,
        'redirect_uri': 'http://%s/%s' % (FACEBOOK_APPLICATION_DOMAIN, FACEBOOK_APPLICATION_NAMESPACE),
        'client_secret': FACEBOOK_APPLICATION_SECRET_KEY,
        }

    query['code'] = ', '.join(code)

    return render(
        request = request,
        template_name = 'authorize_application.html',
        dictionary = {
            'url': 'https://graph.facebook.com/oauth/access_token?%s' % urllib.urlencode(query)
            }, 
        )
    
'''def manage_pages(request):
    user_access_token = 
    profile_id = request.facebook.user.facebook_id
    graph = GraphAPI(user_access_token)
    app_path = "%d/feed" %profile_id
    graph.post(path = app_path, message = 'hellllooo')
    return HttpResponse("Posted on walll")'''

