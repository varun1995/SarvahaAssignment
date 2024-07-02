from utilities.customLogger import LogGen
import os

def test_logging():
    logger = LogGen.loggen()
    logger.info("Test logging info message")
    logger.error("Test logging error message")

    # Check if the log file is created
    log_file_path = os.path.join(os.path.abspath(os.curdir), '\\logs', '\\automation.log')
    assert os.path.exists(log_file_path), "Log file was not created"

    # Check the log file content
    with open(log_file_path, 'r') as log_file:
        log_content = log_file.read()
        assert "Test logging info message" in log_content
        assert "Test logging error message" in log_content
