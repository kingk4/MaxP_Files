# # Exception Handling for Various Error Types
# try:
#     # ValueError: Invalid conversion from string to integer
#     num = str(input("Enter a number: "))
    
#     # TypeError: Attempting to concatenate a string and an integer
#     result = num+3

#     # KeyError: Accessing a non-existent key in a dictionary
#     data = {"name": "Saqib", "age": 30}
#     print("Country:", data["name"])
    
#     # IndexError: Accessing an invalid index in a list
#     items = [10, 20, 30]
#     print("Item:", items[5])
    
# except ValueError:
#     print("ValueError: Please enter a valid number.")
# except TypeError:
#     print("TypeError: Unsupported operation between different data types.")
# except KeyError:
#     print("KeyError: The specified key does not exist in the dictionary.")
# except IndexError:
#     print("IndexError: The specified index is out of range.")
# else:
#     print("All operations completed successfully.")
# finally:
#     print("Execution completed.")



class CustomError(Exception):
    """Custom exception class."""
    pass

try:
    num = int(input("Enter a number greater than 10: "))
    if num <= 10:
        raise CustomError("The number must be greater than 10!")
except CustomError as e:
    print(f"Custom Error: {e}")



# import sys
# try :
#     sys.exit (" Exiting ␣ program " )
# except SystemExit as e :
#     print(f" System ␣ exit ␣ with ␣ message : ␣{ e } ")


# import logging

# # Correcting the filename string and formatting
# logging.basicConfig(filename='app.log', level=logging.ERROR)

# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     logging.error(f"Exception occurred: {e}", exc_info=True)
