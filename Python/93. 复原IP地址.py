def restoreIpAddresses(self, s: str) -> List[str]:
    res = []
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                for d in range(1, 4):
                    if a + b + c + d == len(s):
                        n1 = int(s[:a])
                        n2 = int(s[a:a+b])
                        n3 = int(s[a+b:a+b+c])
                        n4 = int(s[a+b+c:])
                        if n1 < 256 and n2 < 256 and n3 < 256 and n4 < 256:
                            ip = str(n1) + '.' + str(n2) + '.' + str(n3) + '.' + str(n4)
                            if len(ip) == len(s) + 3:
                                res.append(ip)
    return res