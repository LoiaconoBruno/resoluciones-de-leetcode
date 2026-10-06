# 929. Unique Email Addresses (Fácil)
# https://leetcode.com/problems/unique-email-addresses/
#
# Idea: normalizo cada mail (en la parte local corto en el '+' y saco los puntos) y cuento cuántos
#       distintos quedan en un set.
# Tiempo: O(n · m), con m el largo de un mail · Espacio: O(n · m)

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unicos = set()
        for email in emails:
            local, dominio = email.split("@")
            local = local.split("+")[0].replace(".", "")
            unicos.add(local + "@" + dominio)
        return len(unicos)


if __name__ == "__main__":
    s = Solution()
    assert s.numUniqueEmails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
                              "testemail+david@lee.tcode.com"]) == 2
    assert s.numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]) == 3
    print("OK")
