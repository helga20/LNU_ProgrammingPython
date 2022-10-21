class C:

    instances = 0

    def __init__(self):
        C.instances += 1

    # @staticmethod
    def get_instances():
        print(C.instances)


c1, c2 = C(), C()
c1.get_instances()
C.get_instances()