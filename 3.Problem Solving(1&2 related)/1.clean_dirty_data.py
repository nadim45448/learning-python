""" clean the data and get a string output 'a e i o u'
 """
data="aNtEriOur\n\t>>"
result=""

new_data=data.lower()
for small in new_data:
    if (small=='a')or(small=='e') or (small=='i') or (small=='o') or (small=='u'):
         result+=small+" " 
   
print(result)
