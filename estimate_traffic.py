import sys
import math
import argparse
import os

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
    # Power model coefficients
    if alexa_rank <= 0:
        return 0
    traffic = 7.881e10 / (alexa_rank ** 1.257) * 10
    return int(traffic)

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

    # Determine output format based on file extension
    _, ext = os.path.splitext(output_file)
    output_delimiter = ',' if ext.lower() == '.csv' or not ext else ','
    
    with open(output_file, 'w') as outfile:
        # Write header
        outfile.write(f"url{output_delimiter}alexa_rank{output_delimiter}estimated_traffic\n")
        # Write data
        for url, alexa_rank, traffic in results:
            outfile.write(f"{url}{output_delimiter}{alexa_rank}{output_delimiter}{traffic}\n")

    print(f"Processed {len(results)} entries. Results saved to {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Estimate website traffic from Alexa Rank.")
    parser.add_argument("input_file", help="Input file containing URLs and Alexa Ranks.")
    parser.add_argument("output_file", default="output_file.csv", nargs='?', help="Output file to save estimated traffic (default: output_file.csv)")
    args = parser.parse_args()

    process_file(args.input_file, args.output_file)