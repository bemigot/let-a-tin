
from typing import TypeAlias, Iterable

CnSans: TypeAlias = dict[str, list[str]]
DynRecords: TypeAlias = dict[str, list[CnSans]]

def queue_jobs(multiline: Iterable) -> DynRecords:
    """
    Read multi-line iterable line by line and return a map
    domain: -> listOf(CN -> list of SANs, maybe empty)
    e.g. 5-line file
    prod.ex.org  www.ex.org api.ex.org
    test.ex.org  www.ex.org api.ex.org
    omy.ex.org   www.ex.org api.ex.org
    ian.ex.org   www.ex.org api.ex.org
    gitlab.ex.org

    is read as

    {"ex.org": [
      {"prod.ex.org":["www.ex.org", "api.ex.org"]},
      {"test.ex.org":["www.ex.org", "api.ex.org"]},
      {"omy.ex.org":["www.ex.org", "api.ex.org"]},
      {"ian.ex.org":["www.ex.org", "api.ex.org"]},
      {"gitlab.ex.org":[]}
    ]}
    
    Limitation: currently all CNs and SANs must belong to a single domain.
    """
    jobs = []
    domain = None
    for line in multiline:
        line = line.strip()
        if not line: continue

        parts = line.split()
        cn = parts[0]
        sans = parts[1:]

        if domain is None:
            # Extract domain from first CN, e.g. ex.org from www.ex.org
            domain_parts = cn.split('.')
            if len(domain_parts) < 2:
                domain = cn
            else:
                domain = '.'.join(domain_parts[-2:])

        jobs.append({cn: sans})

    if not jobs:
        return {}

    return {domain: jobs}
