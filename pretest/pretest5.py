class MyInt:
    def __init__(self,number):
        self._number = number

    def toRoman(self):
        num = self._number
        roman_list = []
        while num >= 1000:
            roman_list.append("M")
            num -= 1000
        while num >= 900:
            roman_list.append("CM")
            num -= 900
        while num >= 500:
            roman_list.append("D")
            num -= 500
        while num >= 400:
            roman_list.append("CD")
            num -= 400
        while num >= 100:
            roman_list.append("C")
            num -= 100
        while num >= 90:
            roman_list.append("XC")
            num -= 90
        while num >= 50:
            roman_list.append("L")
            num -= 50
        while num >= 40:
            roman_list.append("XL")
            num -= 40
        while num >= 10:
            roman_list.append("X")
            num -= 10
        while num >= 9:
            roman_list.append("IX")
            num -= 9
        while num >= 5:
            roman_list.append("V")
            num -= 5
        while num >= 4:
            roman_list.append("IV")
            num -= 4
        while num >= 1:
            roman_list.append("I")
            num -= 1
        return ''.join(roman_list)
    
    def __add__(self,number):
        result = self._number + number._number
        return int(result + (result/2))

print(" *** class MyInt ***")
x,y = input("Enter 2 number : ").split(" ")
a = MyInt(int(x))
b = MyInt(int(y))

print(a._number,"convert to Roman :",a.toRoman())
print(b._number,"convert to Roman :",b.toRoman())
print(a._number,"+",b._number,"=",a+b)