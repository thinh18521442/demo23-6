def DocFile():
    f1 = open("Rules.txt", "r")
    f2 = open("Hypthesis.txt", "r")
    f3 = open("Goal.txt", "r")

    Program = f1.readlines()
    facts = f2.readlines()
    goals = f3.readlines()

    f1.close()
    f2.close()
    f3.close()
    return Program, facts, goals


def CreateRules(Program, facts, goals):
    P = []
    m = len(Program)
    for i in range(0, m):
        rule = []
        a = Program[i].split()
    GT = []
    for j in range(0, len(a) - 1):
        GT.append(int(a[j]))
        rule.append(GT)
        KL = [int(a[len(a) - 1])]
        rule.append(KL)
        P.append(rule)


    Hypo = []
    n = len(facts)
    for i in range(0, n):
        a = facts[i].split()
        Hypo.append(int(a[0]))

    Goals = []
    n = len(goals)
    for i in range(0, n):
        a = goals[i].split()
        Goals.append(int(a[0]))
    return P, Hypo, Goals


def BackwardChaining(P, Hypo, Goal):
    ok = True
    for t in Goal:
        if t not in Hypo:
            ok = False
    if ok:
        return True
    d = 0
    for i in Goal:
        if i in Hypo:
            d += 1
        else:
            for j in P:
                if j[1][0] == i:
                    ok = BackwardChaining(P, Hypo, j[0])
                    if ok:
                        Hypo.append(i)
                        d += 1
                        break
    if d == len(Goal):
        return True
    else:
        return False


if __name__ == '__main__':
    Program, facts, goals = DocFile()
    P, Hypo, Goals = CreateRules(Program, facts, goals)
    print(BackwardChaining(P, Hypo, Goals))