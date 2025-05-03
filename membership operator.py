s1="make a lot money"
s2="buy now"
s3="subscribe this"
s4="click this"
msg=input("enter the message:")
if((s1 in msg)or(s2 in msg)or(s3 in msg)or (s4 in msg)):
    print("this is a spam message")
else:
    print("no spam alert")