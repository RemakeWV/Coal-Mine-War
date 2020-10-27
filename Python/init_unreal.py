import unreal
import sys

unreal.log_warning("Hello Unreal!")

file = open("C:\Users\Cory\Desktop\Mine Wars Museum\Python\Test.txt", "a+")

file.write(sys.argv[1])

file.close()
