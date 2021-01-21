import unreal
import sys



file = open("C:\Users\Cory\Desktop\Mine Wars Museum\Python\Test.txt", "a+")
file.write(sys.argv[1])

unreal.log_warning("Log has been updated. Opening README for change dev logs")
os.startfile("C:\Users\Cory\Desktop\Mine Wars Museum\README.md")

file.close()
