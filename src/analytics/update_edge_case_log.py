import pandas as pd

edge_cases = pd.read_csv("output/ratio_edge_cases.log", sep="|", engine="python")

def classify(issue):
    issue = str(issue).lower()

    if "source" in issue:
        return "Data Source Issue"

    elif "formula" in issue:
        return "Formula Difference"

    else:
        return "Version Difference"

edge_cases["category"] = edge_cases.iloc[:, 0].apply(classify)

edge_cases.to_csv(
    "output/ratio_edge_cases_categorized.csv",
    index=False
)

print("Edge case categorization completed.")
print(edge_cases.head())