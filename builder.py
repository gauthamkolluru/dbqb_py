
def get_columns(columns=[]):
    return " ".join(columns) if columns else "*"


def get_clauses(clause=[]):
    return " and ".join(clause) if len(clause) > 1 else clause[-1] if clause else ""


def create(query="", table_name="", columns=[], clause_type="", clause=[]):
    qs = ""
    if query:
        qs += " "+query
        qs += " " + get_columns(columns)
        qs += " from"
        if table_name:
            qs += " " + table_name
        if clause_type:
            qs += " " + clause_type
            qs += " " + get_clauses(clause)
    return qs


if __name__ == "__main__":
    print(create(query="select", table_name="users",
                 clause_type="where", clause=["id > 100", "id < 10000"]))
