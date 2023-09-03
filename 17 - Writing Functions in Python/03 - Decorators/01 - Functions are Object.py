# Add the missing function references to the function map
function_map = {
  'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input()

# Check if func_name is a valid key in the function_map dictionary
if func_name in function_map:
    # Call the chosen function and pass "data" as an argument
    function_map[func_name](data)
else:
    print("Invalid function name")