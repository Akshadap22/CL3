import Pyro4

# Take user input for the server URI
uri = input("Enter the server URI (e.g., PYRO:obj_123@localhost:9090): ")

try:
    with Pyro4.Proxy(uri) as remote_object:
        # Take user input for the strings to concatenate
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")

        result = remote_object.concatenate_strings(str1, str2)
        print("Concatenated string:", result)
except Pyro4.errors.CommunicationError as e:
    print("Error connecting to the server:", e)
except Exception as e:
    print("An error occurred:", e)
