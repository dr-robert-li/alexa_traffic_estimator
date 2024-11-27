import sys
import math
import argparse

def detect_delimiter(line):
    if '\t' in line:
        return '\t'
    elif ',' in line:
        return ','
    elif ' ' in line:
        return ' '
    else:
        return None

def estimate_traffic(alexa_rank):
    # Regression model coefficients
    m = -1.2336
    b = 4.873
    x = math.log10(alexa_rank)
    y = m * x + b
    traffic_million = 10 ** y  # Traffic in millions
    traffic = traffic_million * 1_000_000  # Traffic in units
    return max(0, int(traffic // 1000 * 1000))  # Round down to nearest 1000

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Detect delimiter
    for line in lines:
        line = line.strip()
        if not line:
            continue
        delimiter = detect_delimiter(line)
        if delimiter:
            break
    else:
        print("Unable to detect delimiter.")
        return

    results = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.strip().split(delimiter)
        if len(parts) < 2:
            print(f"Skipping line due to incorrect format: {line}")
            continue
        url = parts[0]
        try:
            alexa_rank = int(parts[1])
            if alexa_rank <= 0:
                raise ValueError
        except ValueError:
            print(f"Invalid Alexa Rank for URL {url}: {parts[1]}")
            continue
        traffic = estimate_traffic(alexa_rank)
        results.append((url, alexa_rank, traffic))

    with open(output_file, 'w') as outfile:
        for url, alexa_rank, traffic in results:
            outfile.write(f"{url}{delimiter}{alexa_rank}{delimiter}{traffic}\n")

    print(f"Processed {len(results)} entries. Results saved to {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Estimate website traffic from Alexa Rank.")
    parser.add_argument("input_file", help="Input file containing URLs and Alexa Ranks.")
    parser.add_argument("output_file", help="Output file to save estimated traffic.")
    args = parser.parse_args()

    process_file(args.input_file, args.output_file)