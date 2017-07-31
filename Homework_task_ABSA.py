

# Hello

import requests
URL = 'https://za.pinterest.com/login/?referrer=home_page'
PARAMS = {'Email or phone number': 'heenab27@hotmail.com', 'Password': 'Absa123'}
requests.get(url=URL, params=PARAMS)
print ('Server Operational')


#Registration

def users_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        pwd_1 = request.POST.get('password1')
        pwd_2 = request.POST.get('password2')
        if pwd_1 == pwd_2:
             user = User.objects.create_user(
                                              username=username,
                                              email=email,
                                              password=pwd_1,
                                             )
             return HttpResponseRedirect("/")
        else:
             error = " Passwords do not match "
             return render(request, 'https://za.pinterest.com/login/?referrer=home_page',{"error":error})
    else:
         return render(request, 'https://za.pinterest.com/login/?referrer=home_page')


#Login

		
with requests.Session() as c:
    c.get(URL)
    csrftoken = c.cookies['csrftoken']
    payload = {
        'csrfmiddlewaretoken': 'csrftoken',
        'Username': 'heenab27@hotmail.com',
        'Password': 'Absa123'
}
    p = c.post('https://za.pinterest.com/login/?referrer=home_page', data=payload, headers={"Referer":"https://za.pinterest.com/"})
    print ('csrftoken is', csrftoken)
    print ('Status Code Login', p)
    

#Authentication
from requests.auth import HTTPDigestAuth
url = 'https://za.pinterest.com/heenabhoora/'
x = requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
print ('Status Code Authentication', x)
