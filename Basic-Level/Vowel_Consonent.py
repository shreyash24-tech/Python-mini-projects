string =input("Enter the Srting=")

string =string.lower()
vowel="aeiou"
v_cnt=0
c_cnt=0

for ch in string:
    if ch in vowel:
        v_cnt=v_cnt+1
    else:
        c_cnt=c_cnt+1
    
print("Number of vowels in String =",v_cnt)
print("Number of consonents in Sting=",c_cnt)