from typing import List
import collections

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        very similar to course schedule
        """
        
        n = len(recipes)       
        cando = []
        
        inDict = collections.defaultdict(int)
        outDict = collections.defaultdict(list)
        for i in range(n):
            for ingredient in ingredients[i]:
                if ingredient not in supplies:
                    inDict[recipes[i]] += 1
                    outDict[ingredient].append(recipes[i])
        
        stack = []
        for rec in recipes:
            if inDict[rec] == 0:
                stack.append(rec)
        
        while stack:
            current = stack.pop()
            cando.append(current)
            
            for nxt in outDict[current]:
                inDict[nxt] -= 1
                if inDict[nxt] == 0:
                    stack.append(nxt)
        
        return cando

sol = Solution()

recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast","flour","corn"]
print(sol.findAllRecipes(recipes, ingredients, supplies))

recipes = ["bread","sandwich"]
ingredients = [["yeast","flour"],["bread","meat"]]
supplies = ["yeast","flour","meat"]
print(sol.findAllRecipes(recipes, ingredients, supplies))

recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
print(sol.findAllRecipes(recipes, ingredients, supplies))
