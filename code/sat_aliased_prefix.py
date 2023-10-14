import os
import numpy as np
import pandas as pd
import glob, ast, math



def get_shortest_prefix(ipv6_prefix):
   ipv6_prefix = set(ipv6_prefix)
   ipv6_prefix = sorted(ipv6_prefix)
   shortest_prefixes = []
   for address in ipv6_prefix:
      flag = True
      for i in shortest_prefixes:
         if address.startswith(i):
               flag = False
      if flag:
         shortest_prefixes.append(address)
   return shortest_prefixes



def sat_all_aliased_prefix(filenames):

   print("file number: ",len(filenames))

   list_alias = []

   for file in filenames:
      df = pd.read_csv(file)
      list_alias = list_alias + df.iloc[:-1,4].to_list()

   my_list = list(set(list_alias))
   my_list.remove('[]')
   # print(my_list)
   newlist = []

   for list_alias in my_list:
      if str(list_alias) != 'nan':
         if str(list_alias).startswith('['):
            newlist =  newlist + ast.literal_eval(list_alias)
         else:
            newlist =  newlist + list_alias.split(",")


   shortest_prefixes = get_shortest_prefix(newlist)
   shortest_prefixes = list(set(shortest_prefixes))
   print("-----------------alias prefix-----------------")
   print('alias prefix number:',len(shortest_prefixes))

   new_shortest_prefixes = []
   for prefix in shortest_prefixes:
      temp_prefix = prefix.replace(':', '')
      sub_str = prefix.split(":")[-1]
      prefix = prefix + (4-len(sub_str))*'0' + '::/' + str(len(temp_prefix)*4)
      new_shortest_prefixes.append(prefix)


   shortest_prefixes = sorted(new_shortest_prefixes)
   df_short_alias_prefix = pd.DataFrame(shortest_prefixes)
   df_short_alias_prefix.to_csv("aliased_prefix.txt", index = False, header = False)

# main 

def main():
   filenames = glob.glob("../result/result_seeded_prefix/zmap_result/*_iter_prob_info.txt")
   sat_all_aliased_prefix()

   filenames = glob.glob("../result/result_unseeded_prefix/zmap_result/*_iter_prob_info.txt")
   sat_all_aliased_prefix()
    

if __name__ == '__main__':
    main()