# -*- coding: utf-8 -*-
import sys
import io,os
from tqdm import *
import math
from line import LineClient, LineGroup, LineContact

from time import strftime
import time
user_Pos=0  #user position normal
def Select_user_send(TotalUser,MsgLen):
	lenNum=0
	Msg_Encode=""
	for i in tqdm(range(0,TotalUser)):
		if i<MsgLen:  #use this way to protect array outrange except cause
			user_Pos=i
			Msg_Encode=Msg_Str_contant[i].encode("utf-8")
			try:
				client.contacts[user_Pos].sendMessage(Msg_Encode)
			except:
				pass
		else:
			user_Pos=i
			msg_pos=user_Pos%MsgLen  #get now user array position and Message array len to remainder to select array element
			Msg_Encode=Msg_Str_contant[msg_pos].encode("utf-8")
			try:
				client.contacts[user_Pos].sendMessage(Msg_Encode)
			except:
				pass
		lenNum=lenNum+1



file_array=[]  #input floder all content txt element
Msg_Str_contant=[]  #the txt content append this array to use
lenNum=0  #user friend len
lenGroup=0 #user group len
def Read_Txt():
	global all_friend,Len_Msg_Arr,file_array,Msg_Str_contant,lenNum,lenGroup
	SendMsg_Loca=str(os.path.dirname(os.path.abspath(__file__)))
	Txt_floder="\\\xb0T\xae\xa7\xb8\xea\xae\xc6\xa7\xa8"
	SendMsg_Loca+=Txt_floder
	for dirPath, dirNames, fileNames in os.walk(SendMsg_Loca):  #use os.walk to add the same floder txt file
		for f in fileNames:
			file_array.append(os.path.join(dirPath, f))  #append the file name to array save to next time for use


	File_len=len(file_array)  #the file array len in this variable
	for i in range(File_len):
		Msg_Str=io.open(file_array[i], 'r',encoding = 'utf-8') #the Txt location
		Msg_Str_contant.append(Msg_Str.read())




Read_Txt()

#client = LineClient(authToken="E8KgMu44vmkA7m4Nhv30.YscyjjrBJvRwlj43Q3diOa./6pH4n6MhuUtN11JzTvHSUbFcbiNrf+s+ojB5x0ne7Q=")
print u"請輸入Line帳號: "
Line_user=raw_input()
print u"請輸入Line密碼: "
Line_pass=raw_input()
client = LineClient(Line_user,Line_pass)
#print client.authToken  #print the Line access token
#client.contacts[13].sendMessage("Test")  #Send message to user



Len_Msg_Arr=len(Msg_Str_contant) #User want to send message array

all_friend=len(client.contacts)  #total user friend

Select_user_send(all_friend,Len_Msg_Arr) #send all friend
