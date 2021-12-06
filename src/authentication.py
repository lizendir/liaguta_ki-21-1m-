import requests

access_token = input("Enter access token: ")

url = 'https://webexapis.com/v1/people/me'

headers = {
 'Authorization': 'Bearer {}'.format(access_token)
}

userInfo = requests.get(url, headers=headers).json()

print("")
print("<<< User info >>>")
print("Your name: {}".format(userInfo['displayName']))
print("Your email: {}".format(userInfo['emails'][0]))
print("<<< --- >>>")
print("")

