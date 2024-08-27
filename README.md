# PDF Cover Extractor

This Python script extracts the cover (first page) from PDF files and saves them as PNG images. It processes multiple PDFs in batch, shows a progress bar, and moves processed PDFs to a separate folder.

## Features

- Extracts the first page of each PDF as a cover image
- Processes multiple PDFs in a batch
- Displays a progress bar with status updates
- Moves processed PDFs to a separate folder
- Saves extracted covers as PNG images

## Requirements

- Python 3.6+
- Poppler (for pdf2image library)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Masozee/pdf-cover-extract.git
   cd pdf-cover-extractor
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Install Poppler:
   - On macOS (using Homebrew):
     ```
     brew install poppler
     ```
   - On Windows:
     1. Download the latest release from [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases/)
     2. Extract the downloaded file
     3. Add the `bin` directory to your system PATH
   - On Linux (Ubuntu):
     ```
     sudo apt-get install poppler-utils
     ```

## Usage

1. Place your PDF files in a folder named `data` in the same directory as the script.

2. Run the script:
   ```
   python main.py
   ```

3. The script will:
   - Create a `covers` folder with the extracted cover images
   - Create an `extracted` folder and move processed PDFs there
   - Show a progress bar with status updates for each file

## Customization

You can modify the following variables in the script to change the input and output directories:

```python
input_folder = 'data'  # Folder containing PDFs
output_folder = 'covers'  # Folder to save extracted covers
extracted_folder = 'extracted'  # Folder to move processed PDFs
```

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/pdf-cover-extractor/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
