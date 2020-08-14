#vWrite a Python script that will sum all the even numbers and odd numbers separately.
#At the end the program should print to terminal the absolute value of the difference between the
#two sums of odd and even numbers.
#Example of how the script should work:
# -We have a list of numbers: [1,2,3,4,5,6,7,8]
# -Now we will sum all the even numbers and the result store in the variable even = 2 + 4 + 6 + 8
# -Then we will sum all the odd numbers and the result store in the variable odd = 1 + 3 + 5 + 7
# -Finally we want to get the difference among the two sums
#We should make sure that the difference will not be negative number (you may want to look at
#built-in function for numeric data types in the lesson 1)
#Of course your task is to find out, how to iterate over each item of the number sequence and not to
#write the summation manually.
#For your script, please use the following list of numbers:

nums = [ 386, 462, 47, 418, 907, 344, 236, 375, 823,
        566, 597, 978, 328, 615, 953, 345, 399, 162,
        758, 219, 918, 237, 412, 566, 826, 248, 866,
        950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
        24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
        742, 717, 958,743, 527]

#Example of running the script:
#~/PythonBeginner/Lesson2 $ python diff_odd_even.py
#The difference is: 96

odd = 0
even =0

while nums:
    num =nums.pop()
    if  num % 2 == 0:
        even += num
    else:
        odd += num

diff = abs(even - odd)
print('he difference is:', diff)

nums1 = [ 386, 462, 47, 418, 907, 344, 236, 375, 823,
        566, 597, 978, 328, 615, 953, 345, 399, 162,
        758, 219, 918, 237, 412, 566, 826, 248, 866,
        950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
        24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
        742, 717, 958,743, 527]

sums = [0, 0]
while nums1:
    num = nums1.pop()
    index = num % 2
    sums[index] += num

print('The difference is:', abs(sums[0] - sums[1]))
