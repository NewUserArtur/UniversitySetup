import sys
import yaml_func

if len(sys.argv) == 2:
    print(yaml_func.read(sys.argv[1]))
elif len(sys.argv) == 3:
    print(yaml_func.read_line(sys.argv[1], sys.argv[2]))
else:
    print("Invalid number of arguments")
