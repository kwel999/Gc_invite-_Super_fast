import os
import aminofix, concurrent.futures,getpass
import os
print("\t\033[1;31m GCINVITEBOT\n\n")
print("\t\033[1;32m Script by \033[1;36mMr.COMRADE \n\n")
print("\t\033[1;32m Again fixed by: \033[1;36mPRINCE OF PERSIA \n\n")

client = aminofix.Client()
email = input("Email  >> ")
password = getpass.getpass("password >> ")
client.login(email=email, password=password)
clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Select the community: "))-1]
sub_client = aminofix.SubClient(comId=communityid, profile=client.profile)
chats = sub_client.get_chat_threads(size=150)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chatx = chats.chatId[int(input("Select the chat: "))-1]
def inviteonlineusers():
	with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
		for i in range(0, 20000, 250):
			onlineusers = sub_client.get_online_users(start=i, size=5000).profile.userId
			if onlineusers:
				for userId in onlineusers:
					print(f"{userId} Invited/")
					_ = [executor.submit(sub_client.invite_to_chat, userId, chatx)]
			else:
				break
		for i in range(0, 20000, 250):
			publichats = sub_client.get_public_chat_threads(type="recommended", start=i, size=5000).chatId
			chatsuin = sub_client.get_chat_threads(start=i, size=100).chatId
			chats = [*publichats, *chatsuin]
			if chats:
				for chatid in chats:
					for u in range(0, 1000, 50):
						users = sub_client.get_chat_users(chatId=chatid, start=u, size=100).userId
						if users:
							for userId in users:
								try:
									print(f"{userId} Invited/....")
									_ = [executor.submit(sub_client.invite_to_chat, userId, chatx)]
								except:
									pass
						else:
							break
							print("Invited All Online Users")
def inviteuserfollowers():
	userlink=input("Type user link: ")
	user=client.get_from_code(userlink)
	userx=user.objectId
	with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
		for i in range(0, 20000, 250):
			followers = sub_client.get_user_followers(userId=userx, start=i, size=100).profile.userId
			if followers:
				for userId in followers:
					try:
						print(f"{userId} Invited/....")
						_ = [executor.submit(sub_client.invite_to_chat, userId, chatx)]
					except:
						pass
			else:
				break
				print("Invited User Followers/....")

def inviterecentbannedusers():
	with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
		for i in range(0, 20000, 250):
			recentusers = sub_client.get_all_users(type="recent", start=i, size=100).profile.userId
			bannedusers = sub_client.get_all_users(type="banned", start=i, size=100).profile.userId
			users = [*recentusers, *bannedusers]
			if users:
				for userId in users:
					print(f"{userId} Invited/.....")
					_ = [executor.submit(sub_client.invite_to_chat, userId, chatx)]
			else:
				break
				print("Invited Recent & Banned Users")

def inviteallusers():
	with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
		for i in range(0, 20000, 250):
			onlineusers = sub_client.get_online_users(start=i, size=100).profile.userId
			recentusers = sub_client.get_all_users(type="recent", start=i, size=100).profile.userId
			bannedusers = sub_client.get_all_users(type="banned", start=i, size=100).profile.userId
			users = [*onlineusers, *recentusers, *bannedusers]
			if users:
				for userId in users:
					print(f"{userId} Invited/....")
					_ = [executor.submit(sub_client.invite_to_chat, userId, chatx)]
			else:
				break
		for i in range(0, 20000, 250):
			publichats = sub_client.get_public_chat_threads(type="recommended", start=i, size=100).chatId
			chatsuin = sub_client.get_chat_threads(start=i, size=100).chatId
			chats = [*publichats, *chatsuin]
			if chats:
				for chatid in chats:
					for u in range(0, 1000, 50):
						users = sub_client.get_chat_users(chatId=chatid, start=u, size=100).userId
						if users:
							for userId in users:
								try:
									print(f"{userId} Invited/....")
									_ = [executor.submit(sub_client.invite_to_chat, userId, chatx)]
								except:
									pass
						else:
							break
							print("Invited All Online Users:")
print("1.Invite Online Users:")
print("2.Invite User Followers:")
print("3.Invite Recent & Banned Users:")
print("4.Invite All Users:")
inviteselect = input("Type Number: ")
if inviteselect == "1":
	inviteonlineusers()

elif inviteselect == "2":
	inviteuserfollowers()

elif inviteselect == "3":
	inviterecentbannedusers()

elif inviteselect == "4":
	inviteallusers()
