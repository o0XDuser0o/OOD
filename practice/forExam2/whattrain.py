class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        final_str = ''
        current_node = self.head

        while current_node is not None:
            final_str += str(current_node.data)
            if current_node.next is not None:
                final_str += '->'
            current_node = current_node.next

        if self.size() == 0:
            return "List is empty"

        return final_str

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        r_size = 0
        current_node = self.head
        while current_node is not None:
            r_size += 1
            current_node = current_node.next
        return r_size

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def insert(self, index, data):
        if int(index) < 0 or int(index) > self.size():
            print("Data cannot be added")
        elif int(index) == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            #print(f"index = {index} and data = {data}")
        else:
            current_node = self.head
            linked_index = 0
            while linked_index < int(index) - 1:
                current_node = current_node.next
                linked_index += 1
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
            #print(f"index = {index} and data = {data}")

    def is_in(self, data):
        current_node = self.head
        while current_node is not None:
            if str(current_node) == str(data):
                return True
            current_node = current_node.next
        return False
    
    def find_index(self, data):
        count = 0
        current_node = self.head
        while current_node is not None:
            if str(current_node) == str(data):
                return count
            count += 1
            current_node = current_node.next

    def clear(self):
        self.head = None

    def peek_head(self):
        return self.head.data
        
input_value = input("Enter input: ")
input_value = input_value.split()
if len(input_value) == 1:
    for i in range(int(input_value[0])):
        print(f'{i+1}: {i+1}')
    print(f"Number of train(s): {int(input_value[0])}")    
else:
    num_of_train, train_infrom = input_value
    train_infrom = train_infrom.split(",")
    #print(num_of_train, train_infrom)
    Bookie1 = LinkedList()
    Bookie2 = LinkedList()
    Bookie3 = LinkedList()
    Bookie4 = LinkedList()
    Bookie5 = LinkedList()
    Bookie6 = LinkedList()
    Bookie7 = LinkedList()
    Bookie8 = LinkedList()
    Bookie9 = LinkedList()
    Bookie10 = LinkedList()
    Bookie_list = []

    history_number = LinkedList()
    for i in train_infrom:
        check_head = 'Not'
        check_tail = 'Not'
        head, tail = i.split("-")
        if not history_number.is_in(head):
            history_number.append(head)
        else:
            check_head = 'Have'
        if not history_number.is_in(tail):
            history_number.append(tail)
        else:
            check_tail = 'Have'
        #print(check_head, check_tail)
        if check_head == 'Not' and check_tail == 'Not':
            new_linklist = LinkedList()
            new_linklist.append(head)
            new_linklist.append(tail)
            Bookie_list.append(new_linklist)

        elif check_head == 'Have' and check_tail == 'Not':
            #print("pass2")
            for j in Bookie_list:
                if j.is_in(head):
                    j.append(tail)
        elif check_head == "Not" and check_tail == 'Have':
            #print("pass3")
            for j in Bookie_list:
                if j.is_in(tail):
                    j.insert(0, head)
        elif check_head == 'Have' and check_tail == 'Have':
            #print("pass4")
            for j in Bookie_list:
                if j.is_in(head):
                    head_link = j
                if j.is_in(tail):
                    tail_link = j
            current = tail_link.head
            while current is not None:
                #print(f"current is: {current}")
                head_link.append(current)
                current = current.next
            tail_link.clear()
            #print(head_link)

    for i in range(int(num_of_train)):
        if not history_number.is_in(i+1):
            new_linklist = LinkedList()
            new_linklist.append(i+1)
            history_number.append(i+1)
            Bookie_list.append(new_linklist)

    count = 0
    #print(type(Bookie_list[0].head))

    for i in range(len(Bookie_list)):
        for j in range(i + 1, len(Bookie_list)):
            if (not Bookie_list[i].isEmpty() and 
                not Bookie_list[j].isEmpty() and 
                int(Bookie_list[i].peek_head()) > int(Bookie_list[j].peek_head())):
                
                Bookie_list[i], Bookie_list[j] = Bookie_list[j], Bookie_list[i]

count = 1
for i in range(len(Bookie_list)):
    if not Bookie_list[i].isEmpty():
        print(f'{count}: {Bookie_list[i]}')
        count += 1
print(f"Number of train(s): {count-1}")