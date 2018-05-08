from linepy import *

client = LINE('AUTHTOKEN')
print(client.authToken)
tracer = OEPoll(client)

def NOTIFIED_READ_MESSAGE(op):
	try:
		gid = op.param1
		mid = op.param2
		name = client.getContact(mid).displayName
		client.sendMessage(to=gid, text=name)
	except Exception as e:
		print(e)

tracer.addOpInterruptWithDict({
	OpType.NOTIFIED_READ_MESSAGE: NOTIFIED_READ_MESSAGE
	})

while True:
	tracer.trace()