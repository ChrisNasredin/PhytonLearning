class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr
class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
class MotherBoard:
    def __init__(self, name, cpu, mem_slots):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots
        self.total_mem_slots = 4

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: {"; ".join([obj.name + " - " + str(obj.volume) for obj in self.mem_slots])}']

mb = MotherBoard('Asus', CPU('Celeron', 1400), [Memory('Kingston', 8), Memory('Corsair', 1)])

cpu = CPU('asus', 1333)
mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
mb = MotherBoard('Asus', cpu, [mem1, mem2])
print(mb.get_config())
