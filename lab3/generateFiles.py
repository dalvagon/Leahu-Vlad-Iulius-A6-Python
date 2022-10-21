for i in range(1, 10):
    file = open("./lab3/ex" + str(i) + ".py", "w")
    file.write("def function_name():\n")
    file.write("    return 0 \n\n\n")
    file.write('if __name__ == "__main__":\n')
    file.write("    print(function_name())")
    file.close()
