import asyncio


# 被 async 关键字修饰的方法被调用时不会立即被执行，而是返回一个 coroutine 协程对象
async def execute(x):
    print('Number:', x)


coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')

loop = asyncio.get_event_loop()
# 将协程注册到事件循环中，然后启动
loop.run_until_complete(coroutine)
print('After calling loop')
