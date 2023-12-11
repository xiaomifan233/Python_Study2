class WashingMechine:
    def __init__(self, brandName, mondelName, serialNunber, capacity):
        self.brandName = brandName
        self.mondelName = mondelName
        self.serialNunber = serialNunber
        self.capacity = capacity

    def addClothes(self,list_Clothes,Clothes:str):
        list_Clothes.append(Clothes)
        print('加入衣物：{0}'.format(Clothes))
    def removeClothes(self,list_Clothes:list,Clothes:str):
        list_Clothes.remove(Clothes)
        print('移除衣物：{0}'.format(Clothes))
    def addDetegent(self,Detegent:int):
        print('添加洗衣粉：{0}ml'.format(Detegent))
    def turnOn(self,turnOn:bool):
        if turnOn:
            print('开机')
        if turnOn:
            print('关机')

