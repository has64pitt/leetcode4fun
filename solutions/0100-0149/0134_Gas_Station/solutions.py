class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        
        mintank = 0
        mintankindex = -1
        tank = 0
        
        for index, (add, sub) in enumerate(zip(gas, cost)):            
            tank += add - sub

            if tank < mintank:
                mintank = tank
                mintankindex = index

        
        return (mintankindex + 1) % n
        
            