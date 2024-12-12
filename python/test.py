open_object = open("9.txt", "r")
open_list = open_object.readlines()

# print(open_list[0][121:123])

write_object = open("new_9.txt", "w")


for line in open_list:
    new_line = line[:121] + line[123:]
    write_object.write(new_line)
    # write_object.write('\n')
    # print(line[:122])
    # print(line[123:])

open_object.close()
write_object.close()