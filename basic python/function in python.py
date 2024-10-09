# print("sachin")

# arr[5]={1,2,3,4,5}
# print(arr[1])



# def fun1( ) :
#     print('Reached fun1')
#     def fun2( ) : # nested definition
#         print('Inner avatar')
#     print('Outer avatar')
#     fun2( )



# def fun(i, j, k) :
#     print(i + j,end=" ")
#     print(k.upper( ))
# fun(10, 3.14, 'Rigmarole')

# def print_it(i, a, str) :
#     print(i, a, str)
# print_it(a = 3.14, i = 10, str = 'Sicilian') # keyword, ok
# print_it(str = 'Sicilian', a = 3.14, i = 10) # keyword, ok
# print_it(str = 'Sicilian', i = 10, a = 3.14) # keyword, ok
# # print_it(s = 'Sicilian', j = 10, a = 3.14) # error, keyword name


# def print_it(*args) :
#     print( )
#     for var in args:
#         print(var, end = ' ')
# print_it(10) # 1 arg, ok
# print_it(10, 3.14) # 2 args, ok
# print_it(10, 3.14,'Sicilian') # 3 args, ok
# print_it(10, 3.14, 'Sicilian', 'Punekar') 


# def print_it(**kwargs) :
#     print( )
#     for name, value in kwargs.items( ) :
#         print(name, value, end = ' ')
# print_it(a = 10) # keyword, ok
# print_it(a = 10, b = 3.14) # keyword, ok
# print_it(a = 10, b = 3.14, s = 'Sicilian') # keyword, ok
# dct = {'Student' : 'Ajay', 'Age' : 23}
# print_it(**dct) 


def print_it(name = 'Sanjay', marks = 75) :
    print(name, marks)
d = {'name' : 'Anil', 'marks' : 50}
print_it(*d)
print_it(**d)
