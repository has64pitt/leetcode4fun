class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        start at 0, 0, facing N
        run through the instruction once
        what is the position now (i, j, facing)
        
        if i == j == 0, True
        if facing = N: False
        
                    |   x (facing N = false, facing S = True, facing E = True)
        ------------|---------
                    |
                
        """
        
        # dirarr = N, E, S, W                
        dxs = [0, 1, 0, -1]
        dys = [1, 0, -1, 0]
        
        def goOneStep(cx, cy, cdir, ins):
            if ins == 'G':
                dx = dxs[cdir]
                dy = dys[cdir]
                return (cx + dx, cy + dy, cdir)
            elif ins == 'L':
                cdir += 3
                cdir %= 4
                return (cx, cy, cdir)
            else:
                cdir += 1
                cdir %= 4
                return (cx, cy, cdir)
                
            
        
        def go(cx, cy, cdir):            
            for ins in instructions:
                cx, cy, cdir = goOneStep(cx, cy, cdir, ins)
                
            return cx, cy, cdir
        
        
        cx = cy = cdir = 0
        for _ in range(4):
            cx, cy, cdir = go(cx, cy, cdir)        
            if cx == cy == 0:
                return True
        
        return False
        