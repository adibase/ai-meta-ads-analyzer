import csv

def analyze_campaigns(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"Campaign: {row['campaign_name']}")
            print(f"CTR: {row['ctr']}%")
            print(f"CPL: {row['cpl']} EUR")
            print(f"Leads: {row['leads']}")

            ctr = float(row['ctr'])
            cpl = float(row['cpl'])

            if ctr < 1.0:
                print("- Warning: CTR is low. Creative may need improvement.")
            if cpl > 30:
                print("- Warning: CPL is high. Review targeting and offer clarity.")

            print("- Suggested action: test a stronger hook and a more focused message.")
            print()

if __name__ == "__main__":
    analyze_campaigns("sample_data.csv")
