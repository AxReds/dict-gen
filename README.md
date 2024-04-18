# AxReds' Dictionary Generator

AxReds' Dictionary Generator is a Python script that generates all possible combinations of characters within a specified length range and writes them to a specified file. The script now also supports checkpointing, which means it can save its state and resume from where it left off in case of an interruption.

## Usage

You can run the script from the command line with the following arguments:

- `--min-length`: This argument specifies the minimum length of the combinations. Default value is `1`.
- `--max-length`: This argument specifies the maximum length of the combinations. Default value is `5`.
- `--filename`: This argument specifies the filename to write the combinations to. Default value is `combinations.txt`.

If no arguments are provided, the script will prompt you to enter the values interactively. If you simply press enter without providing a value, the default values will be used.

The script will automatically save its state to a checkpoint file after generating each combination. If the script is interrupted (for example, if you press Ctrl+C), it will save its current state before exiting. The next time you run the script, it will ask you if you want to continue from the last checkpoint.

### Examples

Here are some examples of how to use the script:

- To generate combinations with lengths from 1 to 5 and write them to `combinations.txt`, you can run the script without any arguments:

    ```bash
    python script.py
    ```

- To generate combinations with lengths from 2 to 6 and write them to `my_combinations.txt`, you can use the following command:

    ```bash
    python script.py --min-length 2 --max-length 6 --filename my_combinations.txt
    ```