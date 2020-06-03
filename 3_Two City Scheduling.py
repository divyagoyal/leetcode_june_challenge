class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff_costs = {}
        for i,item in enumerate(costs):
            diff_costs[i]=(abs(item[0]-item[1]))

        new_diff_costs = {k:v for k,v in sorted(diff_costs.items(), key = lambda item: item[1], reverse = True)}
        len_city = int(len(costs)/2)
        a=0
        sum =0
        b=0

        for i,key in enumerate(new_diff_costs.keys()):
            if a!=len_city and b!=len_city:
                if costs[key][0] <costs[key][1]:
                    a+=1
                    sum+=costs[key][0]
                else:
                    b+=1
                    sum+=costs[key][1]
            else:
                break

        if a==len_city and b!=len_city:
            for j,key in enumerate(new_diff_costs.keys()):
                if j>=i:
                    b+=1
                    sum+=costs[key][1]
        if a!=len_city and b==len_city:
            for j,key in enumerate(new_diff_costs.keys()):
                if j>=i:
                    a+=1
                    sum+=costs[key][0]
        if a==len_city and b==len_city:
            return sum
        
