import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        # Determine the absolute path for the log file
        log_dir = os.path.join(os.path.abspath(os.curdir), 'logs')
        log_file = os.path.join(log_dir, 'automation.log')

        print(f"Log directory: {log_dir}")
        print(f"Log file path: {log_file}")

        # Ensure the logs directory exists
        os.makedirs(log_dir, exist_ok=True)

        # Create and configure logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # Create handlers if they do not already exist
        if not logger.handlers:
            # File handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(
                logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))

            print("File handler created")

            # Stream handler for console output
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(message)s'))

            print("Console handler created")

            # Add handlers to the logger
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

            print("Handlers added to logger")

        return logger

# Example usage
# logger = LogGen.loggen()
# logger.info("This is an info message")
# logger.error("This is an error message")
