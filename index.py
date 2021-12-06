from authentication import access_token
import requests

headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params={'max': '100'}
roomsInfo = requests.get('https://webexapis.com/v1/rooms', headers=headers, params=params).json()

roomsItems = roomsInfo['items']


print("")
print("<<< Rooms info >>>")

print("You have {} rooms".format(len(roomsItems)))
for counter, room in enumerate(roomsItems): 
    print("Room {}: \"{}\" with ID: {}".format(counter + 1, room["title"], room['id']))

print("<<< --- >>>")
print("")

newRoomTitle = input("Enter title for new room: ")

isRoomExist = False
for room in roomsItems: 
    if room['title'] == newRoomTitle:
        isRoomExist = True

if(isRoomExist):
    print("")
    print("<<< Room with same title already exist >>>")
    print("<<< --- >>>")
    print("")
else:
    params={'title': newRoomTitle}
    newRoom = requests.post('https://webexapis.com/v1/rooms', headers=headers, json=params).json()

    print("")
    print("<<< Create new room >>>")

    print("You created new room")
    print("ID: " + newRoom['id'])
    print("Title: " + newRoom['title'])

    print("<<< --- >>>")
    print("")


deleteRoomId = input("Enter Room id which will deleted: ")
url = 'https://webexapis.com/v1/rooms/{}'.format(deleteRoomId)
deleteResponse = requests.delete(url, headers=headers)

if deleteResponse.status_code < 400:
    print("")
    print("<<< --- >>>")
    print("Room is deleted")
    print("<<< --- >>>")
    print("") 
else:
    print("")
    print("<<< --- >>>")
    print("Something went wrong during deleting room :(")
    print("<<< --- >>>")
    print("") 

