open_object = open("11.txt", "r")
open_list = open_object.readlines()

# print(open_list[0][121:123])

write_object = open("new_11.txt", "w")


for line in open_list:
    new_line = line[:33] + 'b' + line[34:]
    write_object.write(new_line)
    # write_object.write('\n')
    # print(line[:33])
    # print(line[34:])

open_object.close()
write_object.close()