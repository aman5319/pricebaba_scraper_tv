from collections import Iterable
import re

def pre_process_header(s):
    if s is not None:
        return re.sub("[\(\)]","",s.lower()).strip().replace(" ","_")

def pre_process_value(s):
    return  s.strip() if s is not None else None

def pre_process_date(s):
    if s is not None:
        a = re.search("[A-Z][a-z]*\s*\d{2}(\W)?\s*\d{4}",s)
        if a is not None:
            return a.group()
