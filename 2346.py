#풍선 터뜨리기
# class FunEvent:
#     def __init__(self,tags,year):
#         self.tags=tags
#         self.year=year
#     def __str__(self):
#         return f"FunEvent(tags={self.tags},year={self.year})"

# tags=["google","ml"]
# year=2022
# bootcamp=FunEvent(tags, year)
# tags.append("bootcamp")
# year=2023
# print(bootcamp)
def sqsum1():
	return sum(x**2 if x > 0 for x in nums)

nums=5

# def sqsum2():
#   	return sum(x^2 for x in nums if x > 0)

# def sqsum3():
#   	return sum(for x in nums if x > 0 then x^2)

def sqsum4():
  	return sum(x**2 for x in nums if x > 0)

# def sqsum5():
#   	return sum(x^2 if x > 0 for x in nums)
print(sqsum4())