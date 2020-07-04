def DocFile():
    f1 = open("Rules.txt", "r");
    f2 = open("Hypothesis.txt", "r");

    Program = f1.readlines();
    facts = f2.readlines();

    f1.close();
    f2.close();

    return Program, facts;


def CreateRules(Program, facts):
    P = [];
    m = len(Program);

    for i in range(0, m):
        rule = [];
        a = Program[i].split();
        GT = [];
        for j in range(0, len(a) - 1):
            GT.append(int(a[j]));
        rule.append(GT);

        KL = [int(a[len(a) - 1])];
        rule.append(KL);

        P.append(rule);

    Hypo = [];
    n = len(facts);
    for i in range(0, n):
        a = facts[i].split();
        Hypo.append(int(a[0]));

    return P, Hypo;


def SubSet(A, B):
    if len(A) <= len(B):
        for t in A:
            if not (t in B):
                return 0;

        return 1;
    return 0;


def ForwardChaining(P, Hypo):
    Known = Hypo;

    flag = 1;
    while (flag == 1):
        flag = 0;
        for rule in P:
            # rule = [[],[kl]];
            if not (rule[1][0] in Known) and SubSet(rule[0], Known) == 1:
                flag = 1;
                Known.append(rule[1][0]);

    return Known;


if __name__ == '__main__':
    Program, facts = DocFile();
    P, Hypo = CreateRules(Program, facts);
    Known = ForwardChaining(P, Hypo);
    print(Known);

