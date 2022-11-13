class StackObj:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.__length = 0


    def __getitem__(self, indx: int) -> StackObj:
        if isinstance(indx, int) and (0 <= indx < self.__length):
            curr_obj = self.top
            while indx:
                curr_obj = curr_obj.next
                indx -= 1

            return curr_obj
        else:
            raise IndexError('неверный индекс')


    def __setitem__(self, indx: int, new_obj: StackObj):
        if indx: # if indx > 0 we sholud set new refrence for prev.obj.next and new_obj.next
            new_obj.next = self[indx].next # new_obj.next = replaceable_obj.next
            self[indx-1].next = new_obj # previous_obj.next = new_obj
        else:
            new_obj.next = self.top.next
            self.top = new_obj


    def push(self, obj: StackObj):
        if self.__length:
            self[self.__length-1].next = obj # last_obj.next = next
        else:
            self.top = obj

        self.__length += 1


    def pop(self) -> StackObj:
        if self.__length > 1:
            deleted_obj = self[self.__length-1] # deleted_obj = last_obj
            self[self.__length-2].next = None # prev_obj.next = None

        else:
            deleted_obj = self.top
            self.top = None

        self.__length -= 1
        return deleted_obj
