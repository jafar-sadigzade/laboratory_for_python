# analyzing web server log files to detect potential security incidents
# such as failed login attempts, SQL injection attempts, and suspicious IP addresses.


# Step 1
# open the sample.log file

# Step 2
# Parsing the sample log

# Step 3 define the pattern for 401 http code

# print the result like this:
# This {ip address} get {http code} from {this url} using {methods} at {time}

def to_analyze_log_file_for_http_code(pattern, source, destination):
    import re
    file_to_open = open(source, "r")
    create_new_file = open(destination, "w")
    log_list = file_to_open.readlines()
    http_code_pattern = re.compile(pattern)

    for line in log_list:
        if http_code_pattern.search(line):
            create_new_file.write(line)


to_analyze_log_file_for_http_code(r"\Slogin\S", "sample.log", "result.log")  # calling the function
