from time import sleep
from math import sqrt
from random import randint
class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    # only for debugging
    def show_state(self):
        print('-------')
        for i in range(len(self._list)):
            print(self._list[i], end=' ')
            if i == self._position:
                print(f'[{self._item}]', end=' ')
                if self._light == 'ON':
                    print('(☆ﾟ.*)')
                else:
                    print('(    )')
            else:
                print()


    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        '''
go right until you find the next unsorted
on-(hold) + None + right-space -> swap, move_right, light_off = off-(empty)
on-(hold) + None + right-border -> swap, END
on-(hold) + l>h -> swap, move_right

go left until you find its place
off-(empty) + None + left-space -> swap, move_left = off-(hold)
off-(empty) + None + left-border -> move_right = on-(hold)
off-(hold) + l>h -> move_left = off-(hold)
off-(hold) + l>h + left-border -> swap, light_on, move_right = on-(hold)
off-(hold) + l<=h -> light_on, move_right = on-(hold)
        '''
        x = 0
        message = 'init'
        def updoot(fun=None):
            if fun:
                fun()
            print('\n' * 30)
            print(message)
            self.show_state()
            num = max(150 - (6 * x), 7)
            sleep(num / 100)

        while True:
            if self.light_is_on():
                if self.compare_item() is None:
                    if self.can_move_right():
                        message = '--> reached partition, move it forward'
                        updoot()
                        updoot(self.swap_item)
                        updoot(self.move_right)
                        updoot(self.set_light_off)
                    else:
                        message = '--> final insertion'
                        updoot()
                        updoot(self.swap_item)
                        return
                else:
                    message = '--> shift forward'
                    updoot()
                    updoot(self.swap_item)
                    updoot(self.move_right)
            else:
                if self.compare_item() is None:
                    if self.can_move_left():
                        message = '--> create the partition'
                        updoot()
                        updoot(self.swap_item)
                        updoot(self.move_left)
                    else:
                        message = '--> beginning of list'
                        updoot()
                        updoot(self.move_right)
                else:
                    if self.compare_item() == -1:
                        if self.can_move_left():
                            message = '--> not right place yet'
                            updoot()
                            updoot(self.move_left)
                        else:
                            message = '--> none remaining to be smaller, start shifting'
                            updoot()
                            updoot(self.swap_item)
                            updoot(self.set_light_on)
                            updoot(self.move_right)
                    else:
                        message = '--> correct place! start shifting forward'
                        updoot()
                        updoot(self.set_light_on)
                        updoot(self.move_right)
            x += 1

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot([randint(0, 99) for n in range(18)])

    robot.sort()
    print(robot._list)
