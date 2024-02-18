def my_function(n):
  output = []
  for i in range (0,n,2):
    output.append(i + (i + 1))
    
  return output

print(my_function(8))
