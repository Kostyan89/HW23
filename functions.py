def build_query(f, query):
    query_items = query.split("|")
    res = map(lambda x: x.strip(), f)
    for item in query_items:
        split_item = item.split(":")
        cmd = split_item[0]
        if cmd == "filter":
            arg = split_item[1]
            res = filter(lambda v, txt=arg: txt in v, res)
        if cmd == "map":
            arg = int(split_item[1])
            res = map(lambda v, idx=arg: v.split(" ")[idx], res)
        if cmd == "unique":
            arg = split_item[1]
            res = set(res)
        if cmd == "sort":
            arg = split_item[1]
            if arg == "desc":
                reverse = True
            else:
                reverse = False
            res = sorted(res, reverse=reverse)
        if cmd == "limit":
            arg = int(split_item[1])
            res = list(res)[:arg]
        return res







