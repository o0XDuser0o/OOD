class node:
    def __init__(self,data):
        self.data = data
        self.slink = link()
        self.next = None

class Snode:
    def __init__(self,data):
        self.data = data
        self.next = None

class link:
    def __init__(self):
        self.head = self.tail = None

    def next_node(self,data):
        n = node(data)
        if self.head == None:
            self.head = self.tail = n
            return
        if self.search(data) == None:
            self.tail.next = n
            self.tail = n

    def search(self,data):
        n = self.head
        while n.next != None:
            if n.data == data:
                return n
            n = n.next
        if n.data == data:
            return n
        return None

    def next_secondary_node(self,n,data):
        myn = self.search(n)
        sn = Snode(data)
        if myn.slink.head == None:
            myn.slink.head = myn.slink.tail = sn
            return
        myn.slink.tail.next = sn
        myn.slink.tail = sn


    def show_all(self):
        n,txt = self.head,str(self.head.data)+" : "
        while n.next != None:
            sn = n.slink.head
            if sn != None:
                txt += str(sn.data) + ","
                while sn.next != None:
                    txt += str(sn.next.data) + ","
                    sn = sn.next
            txt = txt+"\n"+str(n.next.data)+" : "
            n = n.next
        return txt

def main():
    ml = link()
    for i in input("input : ").split(","):
        act,item = i.split(" ")
        if act == "ADN":
            ml.next_node(item)
        elif act == "ADSN":
            n,sn = item.split("-")
            ml.next_secondary_node(n,sn)
    print(ml.show_all())

main()