from Message import Message
from Channel import Channel

test = Channel(1, "Test channel")
print(f"Channel id : {test.id} | Channel name : {test.name}")
print(f"Messages in channel when creating : {test.get_all_messages()}")
test.add_message(0, "This is a test message for this channel")
test.add_message(0, "This is a test message for this channel lol")
test.add_message(0, "This is a test message for this channel lol")
test.add_message(0, "This is a test message for this channel lol")
test.add_message(0, "This is a test message for this channel lol")
test.add_message(0, "This is a test message for this channel lol")
print(f"Messages in channel after adding one : {test.get_all_messages()}")
msg = test.get_last_message()
print(f"Showing first message added : id={msg.id} | importance={msg.importance} | string={msg.string}")