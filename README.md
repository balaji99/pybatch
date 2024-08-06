# Generic Batch Processor

This Python script provides a flexible framework for batch processing operations. It allows users to define custom iterators and item processors, making it adaptable to various batch processing needs.

## Key Components

1. **ITER_FUNCTION**: A function that generates an iterable of items to process.
2. **ITEM_FUNCTION**: A function that processes each item from the iterable.
3. **ITER_FUNCTION_CONFIG**: A dictionary of configuration options for the ITER_FUNCTION.

## Default Functionality

By default, the script is set up to list files in a directory and display information about each file:

- `list_files`: Lists files in a specified directory (ITER_FUNCTION)
- `display_file_information`: Displays detailed information about each file (ITEM_FUNCTION)

## Customizing the Batch Processor

To add your own custom iterators and item processors:

1. Define your custom functions in the section marked "Custom iterators and item processors".
2. Update the global variables `ITER_FUNCTION`, `ITEM_FUNCTION`, and `ITER_FUNCTION_CONFIG` as needed.

### Creating a Custom Iterator

A custom iterator should:
- Take at least one parameter for configuration options
- Use the `yield` keyword to return items one at a time
- Handle any necessary logging

Example:

```python
def custom_iterator(config):
    # Your iteration logic here
    for item in your_data_source:
        yield item
```

### Creating a Custom Item Processor

A custom item processor should:
- Take one parameter (the item to process)
- Return `True` to continue processing, or `False` to stop the batch
- Handle any necessary logging or error handling

Example:

```python
def custom_processor(item):
    try:
        # Your processing logic here
        print(f"Processed: {item}")
        return True
    except Exception as e:
        logging.error(f"Error processing item: {str(e)}")
        return False
```

## Usage

1. Define your custom functions if needed.
2. Set the global variables:

   ```python
   ITER_FUNCTION = your_custom_iterator
   ITEM_FUNCTION = your_custom_processor
   ITER_FUNCTION_CONFIG = {"your_config_key": "your_config_value"}
   ```

3. Run the script:

   ```bash
   python generic-batch-processor.py
   ```

The script will log its operations to both the console and a log file named `batch-ops-{timestamp}.log`.

## Note

Ensure that your custom functions handle exceptions appropriately and use the logging module to record important information or errors.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Support

If you encounter any problems or have any questions, please open an issue in the GitHub repository.
