import psutil as p
import GPUtil
import platform
import os

def get_mainboard():
    if platform.system() == "Windows":
        os.system("powershell.exe Get-CimInstance -ClassName Win32_baseboard")
    elif platform.system() == "Linux":
        os.system("sudo dmidecode -t 2")



info = platform.uname()

cpu = platform.processor()
phys_cores = p.cpu_count(logical=False)
log_cores = p.cpu_count(logical=True)

gpus = GPUtil.getGPUs()

disks = p.disk_usage('/')

mem = p.virtual_memory()


print(f"Інформація про систему")
print(f"Система: " + info.system + " " + info.release)
print(f"Версія: " + info.version)


print("\nІнформація про процесор")
print(f"Процесор: " + cpu)
print(f"Логічних ядер: " + str(log_cores))
print(f"Фізичних ядер: " + str(phys_cores))


if not gpus:
    print("Відеокарта відстуня")
else:
    for i, gpu in enumerate(gpus):
        print(f"Інформація про відеокарту")
        print(f"Назва: {gpu.name}")
        print(f"Driver: {gpu.driver}")
        print(f"Загальна відеопам'ять: {gpu.memoryTotal} MB")
        print(f"Вільна відеопамя'ть: {gpu.memoryFree} MB")
        print(f"Температура: {gpu.temperature}°C")

print("\nІнформація про диски:")
print(f"Загальна пам'ять: {(disks.total)/1000000000} гігабайт")
print(f"Зайнята пам'ять: {disks.used/1000000000} гігабайт")
print(f"Вільна пам'ять: {disks.free/1000000000} гігабайт")

print("\nІнформація про оперативну пам'ять:")
print(f"Загальна кількість пам'яті(+virtual): {mem.total/1000000000} гігабайт")
print(f"Вільно: {mem.available/1000000000} гігабайт")
print(f"Зайнято: {mem.used/1000000000} гігабайт")

print(f"\nІнформація про материнську плату")
get_mainboard()
