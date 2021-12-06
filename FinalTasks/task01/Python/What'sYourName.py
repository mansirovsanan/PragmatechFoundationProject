# string: 'Hello firstname lastname! You just delved into python' where firstname and lastname are replaced with  and .

def print_full_name(first, last):
    
     print("Hello " + first_name + " " +last_name + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)