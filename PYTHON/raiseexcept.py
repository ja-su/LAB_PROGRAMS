#wap to delibrately raisa an excception

try:
    num=10
    print(num)
    #raise ValueError
except:
    print("exception occurred")
finally:
    print("cleaning up in finally block")
