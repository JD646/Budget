# Bank Statement Processor

This script processes bank statements in CSV format, and generates cleaned-up versions of the files. The script uses the `os` and `shutil` modules to read and manipulate files, and the `pandas` module to clean up the data.

## Requirements

-   Python 3.x
-   The `pandas` module (can be installed using `pip install pandas`)

## Usage

To run the script, simply run the `main` function:

    from bank_processor import main
    
    main()

This will search for CSV files in the `bank` folder, and use the appropriate class to clean up the data in each file. The cleaned-up data will be saved to a new CSV file in the `bank` folder, with a filename that reflects the original file and the processing that was applied. For example, a file called `Scotia_Visa.csv` will be processed by the `scotia_visa` class, and the resulting file will be called `visa_processed.csv`.

After the files have been processed, the script will move them to the `/mnt/d/banking_files` folder.

## Output

The `bank` folder will contain the processed CSV files, with names that reflect the original file and the processing that was applied. For example, a file called `Scotia_Visa.csv` will be processed by the `scotia_visa` class, and the resulting file will be called `visa_processed.csv`.

The processed files will also be moved to the `/mnt/d/banking_files` folder. The files will contain cleaned-up versions of the original data, with consistent date and transaction formats, and added columns for expenditure, description, category, account, and amount.

The processed data includes columns for the date, expenditure type, description, category, account, and amount. The values in these columns are cleaned up and formatted consistently, making it easier to analyze and manage the data