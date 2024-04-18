import xmlrpc.client

# Prompt the user to enter a number
n = int(input("Enter a number to calculate its factorial: "))

# Establish connection with the XML-RPC server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/") 

# Call the factorial_rpc function on the server and print the result
print("Factorial of %d is: %s" % (n, str(proxy.factorial_rpc(n))))