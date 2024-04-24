def complement_char(c):
  # Write your code here
  nucleobase = {"A":"T","T":"A","G":"C","C":"G"}
  if not c in ("A","T","G","C"):
      return ""
  return nucleobase[c]

def complement_string(s):
    # Write your code here
    new_string = ""
    for i in s:
        new_string = new_string + complement_char(i)
    return new_string

def longestGap(ln, lst):
    # Write your code here
    gap_lst = []
    if lst == []:
        return 0
    if len(lst) == 1:
        return 0
    for i in range(0,len(lst)-1):
        count = 0
        for j in range(lst[i]+ln,lst[i+1]):
          count = count + 1
        gap_lst = gap_lst + [count]
    return max(gap_lst)

def binding(s, t):
    # Write your code here
    
    complement_t = complement_string(t)
    bind_sites = []
    i = 0
    trav_lst = s

    while trav_lst != "":
      comp_str = ""

      for j in range(0,len(t)):
        comp_str += trav_lst[j]
      
      #print(comp_str)
      #print("-",complement_t)
      if complement_t == comp_str:
        bind_sites += [i]
        
      i = i + 1
      trav_lst = s[i:]
      if len(trav_lst) < len(t):
        break
    #print(bind_sites)

    if len(bind_sites) == 0:
      return -1
    elif len(bind_sites) == 1:
      return bind_sites[0]
    else:
      return longestGap(len(t),bind_sites)
    
      








