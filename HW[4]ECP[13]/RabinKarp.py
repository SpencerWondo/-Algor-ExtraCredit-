def separate_and_operate(number, p):
  # Convert the number to a string
  num_str = str(number)
  pairs = []

  # Separate the number into pairs of digits
  for i in range(len(num_str) - 1):
      pair = int(num_str[i] + num_str[i + 1])
      pairs.append(pair)

  # Perform a math operation on each pair
  results = []
  for pair in pairs:
      # Module operation
      result = pair % q_value
      results.append(result)

  # Print the substrings, the hash values, if p was found
  print("================================================= \n")
  print(f"Input:         {input_number}")
  print(f"P-Value:       {p_value}")
  print(f"Q-Value:       {q_value} \n")
  print(f"SubStrings:    {pairs}")
  print(f"Hash Value:    {results} \n")

  # Look through the results for a number that matches p
  found = False
  for result in results:
      if result == p:
          found = True
          break

  if found:
      print(f"Found a matching SubString: {p} \n")
  else:
      print(f"No matching SubString: {p} \n")

  return found

# Test Case
input_number = 583413
p_value = 13
q_value = 35
result_found = separate_and_operate(input_number, p_value)

input_number = 47324134
p_value = 12
q_value = 25
result_found = separate_and_operate(input_number, p_value)

input_number = 647328194
p_value = 19
q_value = 35
result_found = separate_and_operate(input_number, p_value)

print("================================================= \n")

# This is to show ken 