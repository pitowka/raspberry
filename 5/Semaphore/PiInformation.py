from typing import cast, Any

from gpiozero import Device, PiBoardInfo, PinInfo, HeaderInfo

Device.ensure_pin_factory()
info: PiBoardInfo = Device.pin_factory.board_info

# does not work
# print(f'{info}')
# print(f'{info:full}')
# print(f'{info:board}')

print("Basic info")
print(f'{info:specs}')
print()

print("Headers")
print(f'{info:color headers}')
print()

print("Pins")
for _, hi in cast(dict[Any, HeaderInfo], info.headers).items():
    for _, pin in cast(dict[Any, PinInfo], hi.pins).items():
        print(f"{pin}")
print()









