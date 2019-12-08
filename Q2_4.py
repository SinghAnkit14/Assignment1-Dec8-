'''
Q2_4)Write a Python Program to print the given string in the format specified in the sample output.
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens
'''
string = "WE, THE PEOPLE OF INDIA,{}having solemnly resolved to constitute India into a SOVEREIGN,{}SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC{}and to secure to all its citizens{}"
print(string.format('\n\t','!\n\t\t','\n\t\t',':'))
