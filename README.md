# Alexa Traffic Estimator

A Python script that estimates website traffic based on Alexa Rank using a regression model.

## Features

• Processes files containing URLs and Alexa Ranks

• Automatically detects delimiters (tab, comma, or space)

• Estimates traffic using a logarithmic regression model

• Outputs results in the same format as input with traffic estimates

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with input and output file parameters:

```bash
python estimate_traffic.py input_file.txt output_file.txt
```

### Input File Format

The input file should contain two columns:

• Website URL

• Alexa Rank

For CSV files, use these headers:
```csv
url,alexa_rank
example.com,1000
google.com,1
```

The script supports text files with any delimiter (comma, tab, or space).

### Output Format

The output file will contain three columns:

• Website URL

• Alexa Rank

• Estimated Traffic

## Notes

• Traffic estimates are rounded down to the nearest 1000

• Invalid entries are skipped and reported during processing

• Supports CSV, TXT, or any text file with consistent delimiters


## 🤝 Contributing

1. Fork the repository
2. Create your feature branch:
    ```bash
    git checkout -b feature/AmazingFeature
    ```

3. Commit your changes:
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```

4. Push to the branch:
    ```bash
    git push origin feature/AmazingFeature
    ```

5. Open a Pull Request

## 📝 License

MIT License

Copyright (c) 2024 Robert Li

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.