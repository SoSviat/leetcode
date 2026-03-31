class Solution:
    def interpret(self, command: str) -> str:

        res = ''

        for i in range(len(command)):
            if(command[i] == '(' and command[i+1] == ')'):
                res += 'o'
                i += 2
            elif(command[i] != '(' and command[i] != ')'):
                res += command[i]

        return res