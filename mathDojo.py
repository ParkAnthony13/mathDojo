class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        # your code here
        for n in nums:
            num += n
        self.result = num
        return self
    def subtract(self, num, *nums):
        # your code here
        for n in nums:
            num += n
        self.result = num
        return self
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

test = MathDojo()
y = test.add(2,2,2,2,2).subtract(1,1,1,1,1,1,1).result
print(y)