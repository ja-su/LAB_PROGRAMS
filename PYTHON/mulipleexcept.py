#wap which will handlle multiple exceptions
#multiple excep blocks

try:
    num=int(input("Enter a number: "))
    print(num ** 2)
except (KeyboardInterrupt):
    print("keyboard interrupting...")
except (ValueError):
    print("wrong value entered")
#except:
#    print("exception occurred")
