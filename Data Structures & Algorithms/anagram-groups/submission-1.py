class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            st=defaultdict(list)
            for i in strs:
                key="".join(sorted(i))
                st[key].append(i)
            return list(st.values())


                    

            
            
               
            
                    
                    

        